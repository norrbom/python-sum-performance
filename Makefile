CC=gcc
CFLAGS=-I/usr/include/python3.10

all: csum.c
	$(CC) csum.c -o csum.so -shared -fPIC $(CFLAGS)

test:
	python3 -c "import csum; print(csum.sum_int_arr([1, 3]))"
	python3 -c "import csum; print(csum.sum_float_arr([0.01, 0.03]))"
	python3 -c "import csum; print(csum.sum_arr([1, 3]))"
	python3 -c "import csum; print(csum.sum_arr([0.01, 0.03]))"
	python3 -c "import csum; print(csum.sum_arr([0.01, 0.03, 1, 3]))"
	python3 -c "import csum; print(csum.sum_arr([1, 3, 0.01, 0.03]))"

run:
	python3 run.py