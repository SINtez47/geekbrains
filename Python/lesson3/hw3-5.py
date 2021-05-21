from my_functions import my_sum

stop_index = None
result = 0


def convert_item(item: str) -> (int, float):
    try:
        float_item = float(item)
        int_item = int(item.split('.')[0])
    except ValueError:
        raise

    if float_item == int_item:
        return int_item
    else:
        return float_item


if __name__ == '__main__':
    while stop_index is None:
        data = input('Введите числа разделённые\n'
                     'пробелами (допускаются int, float): ').split()

        try:
            stop_index = data.index('q')
            data = data[:stop_index]
        except ValueError:
            pass

        try:
            data = [convert_item(i) for i in data]
        except ValueError:
            print("Введенные данные содержат неверный тип")
            continue

        result += my_sum(data)

        print(result)
