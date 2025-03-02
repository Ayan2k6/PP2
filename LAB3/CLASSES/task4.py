import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def newxy(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Создание точки
x = float(input("Введите x: "))
y = float(input("Введите y: "))
point1 = Point(x, y)
point2 = Point(x, y)

# Показать координаты
point1.show()

# Перемещение точки
new_x = float(input("Введите новое x: "))
new_y = float(input("Введите новое y: "))
point1.newxy(new_x, new_y)
point1.show()

# Вычисление расстояния
print("Расстояние между точками:", point1.distance_to(point2))
