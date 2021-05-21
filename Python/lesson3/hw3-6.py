from sys import argv


def int_func(word: str) -> str:
    if not word.isascii() and not word.isalpha():
        raise ValueError(f'Слово {word} содержит не ASCII символы, или латинские символы')

    if not word.islower():
        raise ValueError(f'Слово {word} содержит не только строчные символы')

    return word.title()


def run_help():
    print(f"Usage: python3 {argv[0]} 'word1 word2'")
    exit(0)


if __name__ == '__main__':
    try:
        words = argv[1].split()
        if len(words) < 2:
            raise RuntimeError()
    except (IndexError, RuntimeError):
        print('Неверный параметр запучска')
        run_help()

    print(' '.join([int_func(item) for item in words]))
