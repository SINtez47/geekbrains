from typing import Iterable, Callable

number_types = (int, float, complex)


def my_div(x: number_types, y: number_types) -> number_types:
    """
    Делит число на число
    :param x: Делимое
    :param y: Делитель
    :return: Частное
    """
    if not (isinstance(x, number_types) and isinstance(y, number_types)):
        raise TypeError(f"unsupported operand type(s) for my_div: "
                        f"'{x.__class__.__name__}' and '{y.__class__.__name__}'")

    return x / y


def my_sum(iterable: Iterable, start: number_types = 0) -> [int, float]:
    
    if not isinstance(iterable, Iterable):
        raise TypeError(f"'{iterable.__class__.__name__}' object is not iterable")

    if not isinstance(start, number_types):
        raise TypeError(f"my_sum() can't sum strings [use ''.join(seq) instead]")

    result = start

    for item in iterable:
        if not isinstance(item, number_types):
            raise TypeError(f"unsupported operand type(s) for +:"
                            f" 'int' and '{item.__class__.__name__}'")

        result += item

    return result


def my_sorted(iterable: Iterable, key: Callable = None, reverse: bool = False,) -> list:

    cmp: Callable = (
        lambda x, y: x > y,
        lambda x, y: x < y,
    )[reverse]

    key: Callable = key if isinstance(key, Callable) else lambda k: k
    result: list = [key(item) for item in iterable]

    for idx in range(1, len(result)):
        current: [int, float, str] = result[idx]
        position: int = idx

        while cmp(result[position - 1], current) and position > 0:
            result[position] = result[position - 1]
            position -= 1

        result[position] = current

    return result

