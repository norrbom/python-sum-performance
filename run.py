import time
import numpy as np
import csum

py_list = list(range(100000000))

results = {
    "py_simple_sum": 0,
    "np.sum": 0,
    "csum.sum_arr": 0,
    "csum.sum_int_arr": 0,
    "py_sum": 0,
}


start = time.time()
py_loop_sum = 0
for i in py_list:
    py_loop_sum += i
end = time.time()
results["py_simple_sum"] = end - start

start = time.time()
np_sum = np.sum(py_list)
end = time.time()
results["np.sum"] = end - start

start = time.time()
sum_arr = csum.sum_arr(py_list)
end = time.time()
results["csum.sum_arr"] = end - start

start = time.time()
sum_int_arr = csum.sum_int_arr(py_list)
end = time.time()
results["csum.sum_int_arr"] = end - start

start = time.time()
py_sum = sum(py_list)
end = time.time()
results["py_sum"] = end - start

for r in results:
    print ("{:<16} {:<19} {:<7}".format(r, results[r], "seconds"))