def print_user_data(**user_data) -> None:
    """
    Распечатывает в одну строку данные пользователя
    :param user_data: данные пользователя
    """
    print(f'Имя: {user_data.get("name")}, Фамилия: {user_data.get("surname")},'
          f' Год рождения: {user_data.get("birth_year")}, Город проживания: {user_data.get("city")},'
          f' email: {user_data.get("email")}, Телефон: {user_data.get("phone")}')


if __name__ == '__main__':
    user = {
        'name': 'Ivan',
        'surname': 'Ivanov',
        'birth_year': '1999',
        'city': 'Saint-Petersburg',
        'email': 'mail@mail.ru',
        'zipcode': '111111',
        'phone': '+79119111111',
    }

    print_user_data(**user)
