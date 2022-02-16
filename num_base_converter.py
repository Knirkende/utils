def int_to_str(n: int, base: int) -> str:
    """
    accepts integer n and returns string representation of
    the integer in the given base.
    """
    string_forms = '0123456789ABCDEF'
    if n < base:
        return string_forms[n]
    return int_to_str(n // base, base) + string_forms[n % base]


if __name__ == '__main__':
    assert int_to_str(10, 2) == '1010'
    assert int_to_str(10, 10) == '10'