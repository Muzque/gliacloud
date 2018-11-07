def anonymous(x):
    """
    :type x: float
    :rtype: float
    """
    return x**2 + 1


def integrate(fun, start, end):
    """
    :type fun: func
    :type start: int
    :type end: int
    :rtype: float
    """
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        area += fun(intercept)*step
    return area


def main():
    print(integrate(anonymous, 0, 10))


if __name__ == '__main__':
    main()
