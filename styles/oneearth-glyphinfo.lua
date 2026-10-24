-- Work around a heap overflow in LuaTeX's tprint() (Arabic editions only;
-- loaded from styles/onechemistry.sty, "Arabic runtime fixes", item 5).
--
-- When LuaTeX reports an underfull or overfull box it prints every glyph of
-- the box through the glyph_info callback, which luaotfload registers as
-- 'luaotfload.glyphinfo'. That callback returns the glyph's character as a
-- raw byte, so cmsy's \times (slot 2) comes back as the one-byte string "\2".
-- tprint() (texk/web2c/luatexdir/tex/printing.c) allocates strlen*3 bytes,
-- writes the control byte to the terminal as "^^B" (3 bytes) and then appends
-- a '\0': four bytes in a three-byte buffer. glibc's padding hides the
-- overflow. musl's allocator, used by Alpine and so by our CI image
-- ghcr.io/xu-cheng/texlive-full, notices it, and the next free() segfaults.
-- The Arabic Book 1 release build died this way at page 377, during the
-- underfull report for "-0.050 \times 5.0" in the grade-12 reaction-rates
-- solutions (runs for v0.0.2 and v0.0.3), with no error in the log.
--
-- The overflow needs a string made only of escaped control bytes, so
-- returning those bytes already escaped, in TeX's own ^^ notation (the
-- form luaotfload already uses for slot 0, "^^@"), removes the case
-- altogether. The log text is unchanged.

local name = 'luaotfload.glyphinfo'
local present = false
for _, description in ipairs(luatexbase.callback_descriptions('glyph_info')) do
  if description == name then present = true end
end
if not present then
  -- A future luaotfload may rename the callback. Say so instead of silently
  -- running unprotected.
  texio.write_nl('term and log',
    'onechemistry: glyph_info callback ' .. name .. ' not found;'
    .. ' the musl tprint() workaround is NOT active')
  return
end

local original = luatexbase.remove_from_callback('glyph_info', name)

-- tprint escapes every byte below 0x20 except tab, line feed and carriage
-- return (needs_escaping() in printing.c), as '^^' followed by byte + 64.
local function escape(byte)
  if byte < 0x20 and byte ~= 0x09 and byte ~= 0x0A and byte ~= 0x0D then
    return '^^' .. string.char(byte + 64)
  end
end

luatexbase.add_to_callback('glyph_info', function(n)
  local s = original(n)
  if type(s) == 'string' then
    s = s:gsub('[\0-\31]', function(c) return escape(c:byte()) end)
  end
  return s
end, name)
