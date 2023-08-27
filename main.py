import time
from multiprocessing import Pool, cpu_count
from pysum import sum

CORES = cpu_count()
MIN = 1
MAX = 100000000
DECIMALS = 2


def print_header(method: str) -> None:
    print(
        f"\n{method:28}{'total(s)':<16}{'compute(s)':<16}{'memory init(s)':<16}{'result':<16}"
    )
    print(
        f"{'--------------------':28}{'----------':<16}{'------------':<16}{'-----------':<16}{'-------':<16}"
    )


def print_results(
    method: str, time_compute: float, time_mem: float, result: int
) -> None:
    print(
        f"{method:28}{round(time_mem + time_compute, DECIMALS):<16}{round(time_compute, DECIMALS):<16}{round(time_mem, DECIMALS):<16}{result:<16}"
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

    cores = CORES
    while cores > 1:
        print_header(f"multi process ({cores}/{CORES})")
        slices = [
            ((i * MAX) // cores + 1, ((i + 1) * MAX) // cores) for i in range(0, cores)
        ]
        for func in functions:
            with Pool(processes=cores) as pool:
                time_start = time.time()
                result = 0
                results_tuple = pool.starmap(func, slices)
                time_total_time_mem = 0.0
                for tup in results_tuple:
                    result += tup[2]
                    time_total_time_mem += tup[1]
                time_total = time.time() - time_start
                print_results(
                    f"{func.__name__}",
                    time_total,
                    time_total_time_mem / cores,
                    result,
                )
        cores = cores // 2
