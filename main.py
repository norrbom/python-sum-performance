import time
from multiprocessing import Pool, cpu_count
from pysum import sum

CORES = cpu_count()
MIN = 1
MAX = 100000000
DECIMALS = 2


def print_header(method: str) -> None:
    print(
        f"\n{method:28}{'total_time':<16}{'compute_time':<16}{'malloc_time':<16}{'result':<16}"
    )
    print(
        f"{'--------------------':28}{'----------':<16}{'------------':<16}{'-----------':<16}{'-------':<16}"
    )


def print_results(
    method: str, compute_time: float, malloc_time: float, result: int
) -> None:
    print(
        f"{method:28}{round(malloc_time+compute_time, DECIMALS):<16}{round(compute_time, DECIMALS):<16}{round(malloc_time, DECIMALS):<16}{result:<16}"
    )


if __name__ == "__main__":
    functions = [
        sum.sum_list,
        sum.sum_range,
        sum.csum_sum_list,
        sum.csum_sum_int_list,
        sum.py_sum,
        sum.sum_np_arange,
    ]

    print_header("single process")

    for func in functions:
        print_results(func.__name__, *func(MIN, MAX))

    print_header("multi process")

    cores = CORES
    while cores > 1:
        slices = [
            ((i * MAX) // cores + 1, ((i + 1) * MAX) // cores) for i in range(0, cores)
        ]
        for func in functions:
            with Pool(processes=cores) as pool:
                time_start = time.time()
                result = 0
                results_tuple = pool.starmap(func, slices)
                time_total_mem_init = 0.0
                for tup in results_tuple:
                    result += tup[2]
                    time_total_mem_init += tup[1]
                time_total = time.time() - time_start
                print_results(
                    f"{func.__name__}({cores}/{CORES})",
                    time_total,
                    time_total_mem_init / cores,
                    result,
                )
        cores = cores // 2
