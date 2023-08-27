CC     ?=gcc
CFLAGS ?=-I$$(find /usr/include/ -name Python.h | head -n 1 | sed 's|/[^/]*$$||')

csum: csum.c
	$(CC) csum.c -o csum.so -shared -fPIC $(CFLAGS)

sum: sum.c
	$(CC) sum.c -o sum

.PHONY: install
install:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	pip install numpy pytest black mypy

.PHONY: test
test:
	. ./venv/bin/activate && python -m pytest

.PHONY: fmt
fmt:
	. ./venv/bin/activate && black .

.PHONY: mypy
mypy:
	. ./venv/bin/activate && mypy --strict --ignore-missing-imports .

.PHONY: run
run:
	. ./venv/bin/activate && python3 main.py

.PHONY: clean
clean:
	rm -rf csum.so venv