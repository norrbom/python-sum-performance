# Python number summarize experiment

Measuring the time to summarize one hundred million integers, using native Python, a C extension and NymPy.

## C reference

Single process naive C implementation wall clock time ~ 0.262s

```sh
make sum
time ./sum
```

## Usage

- Make sure you have the Python dev libraries installed, on Ubuntu: `sudo apt-get install python3-dev`
- You might need to change the CFLAGS=-I/usr/include/python3.10 in the Makefile to point to your Python libraries.

Build the C extension and run the experiment with:

```sh
make && make install run
```

## Results on WSL2 on a Intel i5 10400F CPU / 8GB ram assigned to the VM

```sh
single process              total_time      compute_time    malloc_time     result
--------------------        ----------      ------------    -----------     -------
sum_list                    5.02            3.11            1.91            5000000050000000
sum_range                   4.01            4.01            0               5000000050000000
csum_sum_list               3.74            1.68            2.06            5000000050000000
csum_sum_int_list           2.41            0.76            1.65            5000000050000000
py_sum                      1.97            0.41            1.56            5000000050000000
sum_np_arange               0.12            0.05            0.07            5000000050000000

multi process               total_time      compute_time    malloc_time     result
--------------------        ----------      ------------    -----------     -------
sum_list(12/12)             1.5             1.16            0.34            5000000050000000
sum_range(12/12)            0.94            0.94            0.0             5000000050000000
csum_sum_list(12/12)        1.55            1.09            0.45            5000000050000000
csum_sum_int_list(12/12)    1.46            1.06            0.41            5000000050000000
py_sum(12/12)               1.48            1.07            0.42            5000000050000000
sum_np_arange(12/12)        0.21            0.12            0.09            5000000050000000
sum_list(6/12)              2.01            1.52            0.49            5000000050000000
sum_range(6/12)             0.97            0.97            0.0             5000000050000000
csum_sum_list(6/12)         2.29            1.48            0.81            5000000050000000
csum_sum_int_list(6/12)     1.28            0.89            0.39            5000000050000000
py_sum(6/12)                1.3             0.94            0.36            5000000050000000
sum_np_arange(6/12)         0.18            0.1             0.07            5000000050000000
sum_list(3/12)              2.59            2.04            0.54            5000000050000000
sum_range(3/12)             1.63            1.63            0.0             5000000050000000
csum_sum_list(3/12)         2.79            1.88            0.9             5000000050000000
csum_sum_int_list(3/12)     2.49            1.58            0.91            5000000050000000
py_sum(3/12)                1.76            1.19            0.57            5000000050000000
sum_np_arange(3/12)         0.16            0.1             0.06            5000000050000000
```
