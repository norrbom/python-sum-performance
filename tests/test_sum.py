from pysum import sum
import csum

MIN = 1
MAX = 10
RESULT = 55

functions = [
    sum.sum_list,
    sum.sum_range,
    sum.csum_sum_list,
    sum.csum_sum_int_list,
    sum.py_sum,
    sum.sum_np_arange,
]


def test_all() -> None:
    for func in functions:
        assert (func(MIN, MAX)[2]) == RESULT
