.PHONY: all clean distclean venv test figdata gates data

PY := .venv/bin/python

all:
	latexmk

clean:
	latexmk -c

distclean:
	latexmk -C
	rm -rf build

# The Python side: the figure-data scripts (figdata/), their tests and the
# shared data builders (figdata/shared/, tools/fetch_data.py). System python3 has no numpy, and this machine's
# python3 has no ensurepip, hence the bootstrap through the user's pip.
venv:
	python3 -m venv --without-pip .venv
	pip --python $(PY) install -r requirements.txt

# Y=<year> scopes test and figdata to one year (what a book writer runs while
# another book is being written in the same tree): make test Y=bachelor-1
# Without Y, each year runs in its own pytest process: two years may own
# figdata modules of the same name (hypsometry, prem_profiles), and one
# process would import the first one it meets for both.
test:
ifdef Y
	$(PY) -m pytest -q tests/test_gates.py tests/shared $(wildcard tests/$(Y))
else
	@$(PY) -m pytest -q tests/test_gates.py tests/shared || exit 1; \
	for d in $$(ls -d tests/*/ | grep -v -e '/shared/$$' -e '__pycache__'); do \
	  echo "  $$d"; $(PY) -m pytest -q $$d || exit 1; done
endif

# Regenerate every figure table under figdata/out/ -- must leave no diff.
figdata:
	@d=figdata/$(Y); [ -d "$$d" ] || { echo "  (no $$d)"; exit 0; }; \
	for f in $$(find "$$d" -name '*.py' ! -name 'test_*' ! -name '_*' | sort); do \
	  echo "  $$f"; $(PY) $$f || exit 1; done

# Every chapter-level gate over every year (tools/gates.sh <year> for one).
gates:
	@for y in $$(ls parts); do bash tools/gates.sh $$y || exit 1; done

# Rebuild data/derived/ from data/raw/ (network: tools/fetch_data.py fetch).
# figdata reads only data/derived/, so `make figdata` stays offline.
data:
	$(PY) tools/fetch_data.py derive
