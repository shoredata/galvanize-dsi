def least_common_multiple(a, b):
    """A good a docstring!"""
    for i in range(1, a*b):
        if _is_multiple(i, a) and _is_multiple(i, b):
            return i
    return a*b

def _is_multiple(bigger, smaller):
    return bigger % smaller == 0
