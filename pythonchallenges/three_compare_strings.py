def compare_strings(a, b):
    """Finding distanse of two string"""
    if a is None or b is None:
        raise TypeError('This method required 2 arguments but one/zero passed')
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError('This method required string arguments!!!')

    # Finding the minimum length
    min_size = min(len(a), len(b))
    count = 0

    for i in range(min_size):
        if a[i] == b[i]: continue
        count += 1

    return count

