class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        print("Название произведения:", self.title)
        print("Автор:", self.author)
        print("Год издания:", self.year)
books = [Book("Преступление и наказание", "Ф.М. Достоевский" ,1866), Book("Колобок", "Неизвестно", "до н.р."), Book("Мастер и Маргарита", "М. Булгаков", 1967)]
for b in books:
    b.get_info()


class Сircle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


circle = Сircle(5)
print("Начальный радиус", circle.get_radius())

circle.set_radius(10)
print("Новый радиус", circle.get_radius())