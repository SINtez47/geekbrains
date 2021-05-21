numeric = (int, float, complex)


def my_pow1(base: numeric, exp: numeric, mod: numeric = None) -> numeric:
    if not isinstance(base, numeric) or not isinstance(exp, numeric):
        raise TypeError(f"unsupported operand type(s) for ** or pow(): "
                        f"'{base.__class__.__name__}' and '{exp.__class__.__name__}'")

    if mod and not isinstance(mod, numeric):
        raise TypeError(f"unsupported operand type(s) for pow(): "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")

    result = base ** exp

    if mod is None:
        return result
    else:
        return result % mod


def my_pow2(base: numeric, exp: numeric, mod: numeric = None) -> numeric:
    if not isinstance(base, numeric) or not isinstance(exp, numeric):
        raise TypeError(f"unsupported operand type(s) for ** or pow(): "
                        f"'{base.__class__.__name__}' and '{exp.__class__.__name__}'")

    if mod and not isinstance(mod, numeric):
        raise TypeError(f"unsupported operand type(s) for pow(): "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")

    result = 1

    while exp:
        result *= base
        exp -= 1

    if mod is None:
        return result
    else:
        return result % mod


if __name__ == '__main__':
    print(my_pow1(3, 4))
    print(my_pow2(3, 6, 4))
