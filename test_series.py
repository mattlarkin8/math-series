from series import fibonacci, lucas, sum_series
import pytest


#test fibonacci function
# def test_fibonacci_input_0():
#     actual = fibonacci(0)
#     expected = 0
#     assert actual == expected
#
# def test_fibonacci_input_1():
#     actual = fibonacci(1)
#     expected = 1
#     assert actual == expected
#
# def test_fibonacci_input_2():
#     actual = fibonacci(2)
#     expected = 1
#     assert actual == expected
#
# def test_fibonacci_input_3():
#     actual = fibonacci(3)
#     expected = 2
#     assert actual == expected
#
# def test_fibonacci_input_5():
#     actual = fibonacci(5)
#     expected = 5
#     assert actual == expected
#
# def test_fibonacci_input_10():
#     actual = fibonacci(10)
#     expected = 55
#     assert actual == expected


#test lucas function
# def test_lucas_input_0():
#     actual = lucas(0)
#     expected = 2
#     assert actual == expected
#
# def test_lucas_input_1():
#     actual = lucas(1)
#     expected = 1
#     assert actual == expected
#
# def test_lucas_input_2():
#     actual = lucas(2)
#     expected = 3
#     assert actual == expected
#
# def test_lucas_input_3():
#     actual = lucas(3)
#     expected = 4
#     assert actual == expected
#
# def test_lucas_input_5():
#     actual = lucas(5)
#     expected = 11
#     assert actual == expected
#
# def test_lucas_input_10():
#     actual = lucas(10)
#     expected = 123
#     assert actual == expected

#test sum_series function with fibonacci numbers
def test_sum_series_for_fib_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_for_fib_1():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_for_fib_2():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_series_for_fib_3():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_series_for_fib_5():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sum_series_for_fib_10():
    actual = sum_series(10)
    expected = 55
    assert actual == expected

#test sum_series function with lucas numbers
def test_sum_series_for_lucas_0():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

# def test_sum_series_for_lucas_1():
#     actual = sum_series(1, 2, 1)
#     expected = 1
#     assert actual == expected
#
# def test_sum_series_for_lucas_2():
#     actual = sum_series(2, 2, 1)
#     expected = 3
#     assert actual == expected
#
# def test_sum_series_for_lucas_3():
#     actual = sum_series(3, 2, 1)
#     expected = 4
#     assert actual == expected
#
# def test_sum_series_for_lucas_5():
#     actual = sum_series(5, 2, 1)
#     expected = 11
#     assert actual == expected
#
# def test_sum_series_for_lucas_10():
#     actual = sum_series(10, 2, 1)
#     expected = 123
#     assert actual == expected
