class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def classify_triangle(self):
        """The method checks for the existence of a triangle and determines
        its type (equilateral, isosceles, or scalene),
        and then returns the appropriate description"""
        if (self.side_a >= self.side_b + self.side_c
                or self.side_b >= self.side_a + self.side_c
                or self.side_c >= self.side_a + self.side_b):
            return "Треугольник с данными сторонами не существует"
        elif self.side_a == self.side_b == self.side_c:
            return "Равносторонний треугольник"
        elif (self.side_a == self.side_b
              or self.side_b == self.side_c
              or self.side_a == self.side_c):
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"


side_a = int(input("Введите длину стороны a: "))
side_b = int(input("Введите длину стороны b: "))
side_c = int(input("Введите длину стороны c: "))

triangle = Triangle(side_a, side_b, side_c)

print(triangle.classify_triangle())
