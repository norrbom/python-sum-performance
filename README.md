# Python number summarize experiment
Meassuring the time to summarize one hundred million integers in a python list using native Python, a C extension and NymPy.

## Methods:

### py_list_sum
Looping through the list with python

### csum.sum_arr
Using a custom C extension that does type checking and can summarize a combination of floats and integers in a list.

### csum.sum_int_arr
Using a custom C extension to summarize integers in a list.

### py_sum
Using the built in Python sum() method

### np.sum_arrange
Using the NumPy np.sum() and np.arrange

## Usage

- Make sure you have the Python dev libraries installed, on Ubuntu: `sudo apt-get install python3-dev`
- You might need to change the CFLAGS=-I/usr/include/python3.10 in the Makefile to point to your Python libraries.

Build the C extension and run the experiment with:

```sh
make && make install run
```

## Results on WSL2 on a Intel i5 10400F CPU

```sh
py_list_sum             4999999950000000        6.1064629554748535
csum.sum_arr            4999999950000000        1.5754830837249756
csum.sum_int_arr        4999999950000000        0.7434167861938477
py_sum                  4999999950000000        0.4117319583892822
np.sum_arrange          4999999950000000        0.04780292510986328
```
