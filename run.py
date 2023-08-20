import time
import numpy as np
import csum

range = range(100000000)
py_list = list(range)
arrange = np.arange(100000000)

def print_result(method: str, summary: int, result: int):
    print(f"{method:16}\t{result}\t{summary}")

summary = 0
start = time.time()
for i in py_list:
    summary += i
end = time.time()
print_result("py_list_sum", end - start, summary)

start = time.time()
summary = csum.sum_arr(py_list)
end = time.time()
print_result("csum.sum_arr", end - start, summary)
start = time.time()
summary = csum.sum_int_arr(py_list)
end = time.time()
print_result("csum.sum_int_arr", end - start, summary)

start = time.time()
summary = sum(py_list)
end = time.time()
print_result("py_sum", end - start, summary)

start = time.time()
summary = np.sum(arrange)
end = time.time()
print_result("np.sum_arrange", end - start, summary)