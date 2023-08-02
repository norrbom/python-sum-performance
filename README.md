# Python number summarize experiment
Meassuring the time to summarize one hundred million integers in a python list using native Python, a C extension and NymPy.

## Methods:

### py_simple_sum
Looping through the list with python

### np.sum
Using the NumPy np.sum()

### csum.sum_arr
Using a custom C extension that does type checking and can summarize a combination of floats and integers in a list.

### csum.sum_int_arr
Using a custom C extension to summarize integers in a list.

### py_sum
Using the built in Python sum() method

## Usage

- Make sure you have the Python dev libraries installed, on Ubuntu: `sudo apt-get install python3-dev`
- You might need to change the CFLAGS=-I/usr/include/python3.10 in the Makefile to point to your Python libraries.

Build the C extension and run the experiment with:

```sh
make && make install run
```

## Results on WSL2 on a Intel i5 10400F CPU

```sh
py_simple_sum    5.694443464279175   seconds
np.sum           3.121760368347168   seconds
csum.sum_arr     1.1044163703918457  seconds
csum.sum_int_arr 0.6375510692596436  seconds
py_sum           0.43586254119873047 seconds
```
