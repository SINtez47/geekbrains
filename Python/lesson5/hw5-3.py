firm = {'Сотрудник1': 11000, 'Сотрудник2': 20000, 'Сотрудник3': 35000, 'Сотрудник4': 9000, 'Сотрудник5': 15000, 'Сотрудник6': 10000, 'Сотрудник7': 1000, 'Сотрудник8': 50000, 'Сотрудник9': 7000, 'Сотрудник10': 15000}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"averate: {result}")
