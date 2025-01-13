with open('example.txt', 'r') as file:
    content = file.read()
print(content)



def append_to_file(file_name):
    i = input("Введите текст: ")
    with open(file_name, 'a') as file:
        file.write(i + '\n')
    print("Текст успешно добавлен")


append_to_file('user_input.txt')


i = input("Введите имя файла")
x = input("Введите режим")
def read_file(i, x):
    try:
        with open(i, 'r') as file:
            if x == 'all':
                content = file.read()
                print(content)
            elif x == 'line_by_line':
                for line in file:
                    print(line)
            else:
                print("Выберите режим all или line_by_line")
    except FileNotFoundError:
        print(f"Файл не найден")
print(read_file(i,x))