CC     ?=gcc
CFLAGS ?=-I$$(find /usr/include/ -name Python.h | head -n 1 | sed 's|/[^/]*$$||')

all: csum.c
	$(CC) csum.c -o csum.so -shared -fPIC $(CFLAGS)

.PHONY: install
install:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	pip install numpy

.PHONY: test
test:
	. ./venv/bin/activate && python3 -c "import csum; print(csum.sum_int_list([1, 3]))"
	. ./venv/bin/activate && python3 -c "import csum; print(csum.sum_float_arr([0.01, 0.03]))"
	. ./venv/bin/activate && python3 -c "import csum; print(csum.sum_list([1, 3]))"
	. ./venv/bin/activate && python3 -c "import csum; print(csum.sum_list([0.01, 0.03]))"
	. ./venv/bin/activate && python3 -c "import csum; print(csum.sum_list([0.01, 0.03, 1, 3]))"
	. ./venv/bin/activate && python3 -c "import csum; print(csum.sum_list([1, 3, 0.01, 0.03]))"

.PHONY: run
run:
	. ./venv/bin/activate && python3 run.py

.PHONY: clean
clean:
	rm -rf csum.so venv