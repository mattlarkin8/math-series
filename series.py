def fibonacci(n):
    """
    In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, the Fibonacci sequence, in
    which each number is the sum of the two preceding ones. The sequence commonly starts from 0 and 1, although
    some authors omit the initial terms and start the sequence from 1 and 1 or from 1 and 2.
    Starting from 0 and 1, the next few values in the sequence are:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    - https://en.wikipedia.org/wiki/Fibonacci_number
    :param n:
    :return: nth value in the fibonacci sequence
    """

    #base case
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    The Lucas series has the same recursive relationship as the Fibonacci sequence, where each term is the sum
    of the two previous terms, but with different starting values. This produces a sequence where the ratios
    of successive terms approach the golden ratio, and in fact the terms themselves are roundings of integer
    powers of the golden ratio. The sequence also has a variety of relationships with the Fibonacci numbers,
    like the fact that adding any two Fibonacci numbers two terms apart in the Fibonacci sequence results in
    the Lucas number in between. The first few Lucas numbers are:
    2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349 ....
    - https://en.wikipedia.org/wiki/Lucas_number
    :param n:
    :return: nth value in the lucas numbers
    """

    #base case
    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)
