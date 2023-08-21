import time
import inspect
import numpy as np
from multiprocessing import Pool, cpu_count
import csum

CORES = cpu_count()
NUMBER = 100000000
DECIMALS = 2

def print_header(method):
    print(f"\n{method:28}{'total_time':<16}{'compute_time':<16}{'malloc_time':<16}{'summary':<16}")
    print(f"{'--------------------':28}{'----------':<16}{'------------':<16}{'-----------':<16}{'-------':<16}")

def print_results(method: str, compute_time: int, malloc_time: int, summary: int):
    print(f"{method:28}{round(malloc_time+compute_time, DECIMALS):<16}{round(compute_time, DECIMALS):<16}{round(malloc_time, DECIMALS):<16}{summary:<16}")

def sum_list(start: int, end: int):
    method = inspect.currentframe().f_code.co_name
    start_time = time.time()
    py_list = list(range(start, end))
    compute_start_time = time.time()
    summary = 0
    for i in py_list:
        summary += i
    end = time.time()
    return (method, end - compute_start_time, compute_start_time - start_time, summary)

def sum_range(start: int, end: int):
    method = inspect.currentframe().f_code.co_name
    start_time = time.time()
    summary = 0
    for i in range(start, end):
        summary += i
    end = time.time()
    return (method, end - start_time, 0, summary)

def csum_sum_list(start: int, end: int):
    method = inspect.currentframe().f_code.co_name
    start_time = time.time()
    py_list = list(range(start, end))
    compute_start_time = time.time()
    summary = csum.sum_list(py_list)
    end = time.time()
    return (method, end - compute_start_time, compute_start_time - start_time, summary)

def csum_sum_int_list(start: int, end: int):
    method = inspect.currentframe().f_code.co_name
    start_time = time.time()
    py_list = list(range(start, end))
    compute_start_time = time.time()
    summary = csum.sum_int_list(py_list)
    end = time.time()
    return (method, end - compute_start_time, compute_start_time - start_time, summary)

def py_sum(start: int, end: int):
    method = inspect.currentframe().f_code.co_name
    start_time = time.time()
    py_list = list(range(start, end))
    compute_start_time = time.time()
    summary = sum(py_list)
    end = time.time()
    return (method, end - compute_start_time, compute_start_time - start_time, summary)

def sum_np_arange(start: int, end: int):
    method = inspect.currentframe().f_code.co_name
    start_time = time.time()
    np_array = np.arange(start, end)
    compute_start_time = time.time()
    summary = np.sum(np_array)
    end = time.time()
    return (method, end - compute_start_time, compute_start_time - start_time, summary)


functions = [sum_list, sum_range, csum_sum_list, csum_sum_int_list, py_sum, sum_np_arange]

print_header("single process")

for function in functions:
    print_results(*function(0, NUMBER))

print_header("multi process")

cores = CORES
while (cores > 1):
    slices = [( (i * NUMBER) // cores, ((i+1) * NUMBER) // cores ) for i in range(cores)]
    for function in functions:
        with Pool(processes=cores) as pool:
            start_time = time.time()
            summary = 0
            results = pool.starmap(function, slices)
            tot_malloc_time = 0
            for result in results:
                summary += result[len(result)-1]
                tot_malloc_time += result[2]
            end = time.time()
            print_results(f"{function.__name__}({cores}/{CORES})", end - start_time, tot_malloc_time/cores, summary)
    cores = cores // 2