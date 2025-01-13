class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


user = UserAccount("kiborg777", "2024ghbts@mail.ru", "password1")

user.set_password("098765432")
print("Пароль успешно изменен")

if user.check_password("098765432"):
    print("Пароль верный")
else:
    print("Пароль неверный")


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"


vehicle = Vehicle("BMW", "530i")
print(vehicle.get_info())

car = Car("Tesla", "S", "Электричество")
print(car.get_info())