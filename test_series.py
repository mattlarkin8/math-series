from series import fibonacci
import pytest

#test fibonacci function
def test_fibonacci_input_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_input_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_input_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_input_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_input_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_input_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

# # test lucas function
# def test_lucas_input_1():
#     lucas(1)
#
#
# def test_lucas_input_2():
#     lucas(2)
#
#
# def test_lucas_input_3():
#     lucas(3)
#
#
# def test_lucas_input_5():
#     lucas(5)
#
#
# def test_lucas_input_10():
#     lucas(10)
#
#
# # test sum_series function
# def test_sum_series_input_1():
#     sum_series(1)
#
#
# def test_sum_series_input_2():
#     sum_series(2)
#
#
# def test_sum_series_input_3():
#     sum_series(3)
#
#
# def test_sum_series_input_5():
#     sum_series(5)
#
#
# def test_sum_series_input_10():
#     sum_series(10)
