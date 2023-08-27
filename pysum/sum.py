import time
import inspect
import numpy as np
import csum


def sum_list(start: int, end: int) -> tuple[float, float, int]:
    time_start = time.time()
    py_list = list(range(start, end + 1))
    time_compute_start = time.time()
    result = 0
    for i in py_list:
        result += i
    time_end = time.time()
    return (time_end - time_compute_start, time_compute_start - time_start, result)


def sum_range(start: int, end: int) -> tuple[float, float, int]:
    time_start = time.time()
    result = 0
    for i in range(start, end + 1):
        result += i
    time_end = time.time()
    return (time_end - time_start, 0, result)


def csum_sum_list(start: int, end: int) -> tuple[float, float, int]:
    time_start = time.time()
    py_list = list(range(start, end + 1))
    time_compute_start = time.time()
    result = csum.sum_list(py_list)
    time_end = time.time()
    return (time_end - time_compute_start, time_compute_start - time_start, result)


def csum_sum_int_list(start: int, end: int) -> tuple[float, float, int]:
    time_start = time.time()
    py_list = list(range(start, end + 1))
    time_compute_start = time.time()
    result = csum.sum_int_list(py_list)
    time_end = time.time()
    return (time_end - time_compute_start, time_compute_start - time_start, result)


def py_sum(start: int, end: int) -> tuple[float, float, int]:
    time_start = time.time()
    py_list = list(range(start, end + 1))
    time_compute_start = time.time()
    result = sum(py_list)
    time_end = time.time()
    return (time_end - time_compute_start, time_compute_start - time_start, result)


def sum_np_arange(start: int, end: int) -> tuple[float, float, int]:
    time_start = time.time()
    np_array = np.arange(start, end + 1)
    time_compute_start = time.time()
    result = np.sum(np_array)
    time_end = time.time()
    return (time_end - time_compute_start, time_compute_start - time_start, result)
