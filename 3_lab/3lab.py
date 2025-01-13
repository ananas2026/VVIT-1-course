import math
import datetime
print(datetime.datetime.now())
i = int(input("Введите число"))
print(math.sqrt(i))


from my_module import add_numbers
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
result = add_numbers(x, y)
print(result)


from my_package.number_operations import add, multiply
from my_package.string_operations import concatenate, reverse_string

result_add = add(1000, 111)
result_multiply = multiply(5, 5)

print(result_add)
print(result_multiply)

result_concatenate = concatenate("Привет, ", "меня зовут Андрей")
result_reverse = reverse_string("заказ")

print(result_concatenate)
print(result_reverse)