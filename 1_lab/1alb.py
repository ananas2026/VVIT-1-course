i = input("Введите ваше имя ")
def greet(name):
    return f"Привет, {name}!"
print(greet(i))


i = input("Введите имя")
def describe_person(name, age = 30):
    return f"Имя: {name}, Возраст: {age}"
print(describe_person(i))


n = int(input("Введите число"))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(n))