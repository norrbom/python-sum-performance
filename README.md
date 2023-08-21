# Python number summarize experiment

Measuring the time to summarize one hundred million integers, using native Python, a C extension and NymPy.

## Usage

- Make sure you have the Python dev libraries installed, on Ubuntu: `sudo apt-get install python3-dev`
- You might need to change the CFLAGS=-I/usr/include/python3.10 in the Makefile to point to your Python libraries.

Build the C extension and run the experiment with:

```sh
make && make install run
```

## Results on WSL2 on a Intel i5 10400F CPU / 8GB ram assigned to the VM

```sh
single process              total_time      compute_time    malloc_time     summary
--------------------        ----------      ------------    -----------     -------
sum_list                    4.73            3.1             1.63            4999999950000000
sum_range                   3.99            3.99            0               4999999950000000
csum_sum_list               3.27            1.56            1.71            4999999950000000
csum_sum_int_list           2.29            0.87            1.43            4999999950000000
py_sum                      1.9             0.4             1.5             4999999950000000
sum_np_arange               0.12            0.05            0.07            4999999950000000

multi process               total_time      compute_time    malloc_time     summary
--------------------        ----------      ------------    -----------     -------
sum_list(12/12)             1.42            1.11            0.31            4999999950000000
sum_range(12/12)            0.72            0.72            0.0             4999999950000000
csum_sum_list(12/12)        1.17            0.86            0.31            4999999950000000
csum_sum_int_list(12/12)    1.19            0.82            0.37            4999999950000000
py_sum(12/12)               1.34            0.98            0.36            4999999950000000
sum_np_arange(12/12)        0.2             0.12            0.08            4999999950000000
sum_list(6/12)              1.82            1.42            0.41            4999999950000000
sum_range(6/12)             0.95            0.95            0.0             4999999950000000
csum_sum_list(6/12)         1.77            1.21            0.56            4999999950000000
csum_sum_int_list(6/12)     1.12            0.8             0.33            4999999950000000
py_sum(6/12)                1.56            1.13            0.43            4999999950000000
sum_np_arange(6/12)         0.2             0.12            0.08            4999999950000000
sum_list(3/12)              2.69            2.11            0.57            4999999950000000
sum_range(3/12)             1.62            1.62            0.0             4999999950000000
csum_sum_list(3/12)         2.32            1.62            0.7             4999999950000000
csum_sum_int_list(3/12)     1.77            1.2             0.58            4999999950000000
py_sum(3/12)                1.67            1.14            0.53            4999999950000000
sum_np_arange(3/12)         0.12            0.08            0.05            4999999950000000
```
