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