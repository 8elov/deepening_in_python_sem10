import fractions


class FractionCalculator:
    def __init__(self):
        self.fraction1 = None
        self.fraction2 = None

    def find_gcd(self, a, b):
        """Finds the greatest common divisor of two numbers."""
        while b != 0:
            a, b = b, a % b
        return a

    def simplify_fraction(self, numerator, denominator):
        """Simplifies a fraction to its smallest manifest form."""
        common_divisor = self.find_gcd(numerator, denominator)
        return numerator // common_divisor, denominator // common_divisor

    def add_fractions(self):
        """Addition of two fractions."""
        num1, den1 = map(int, self.fraction1.split("/"))
        num2, den2 = map(int, self.fraction2.split("/"))

        common_denominator = den1 * den2
        new_num1 = num1 * den2
        new_num2 = num2 * den1

        sum_numerators = new_num1 + new_num2
        return self.simplify_fraction(sum_numerators, common_denominator)

    def multiply_fractions(self):
        """Multiplication of fractions."""
        num1, den1 = map(int, self.fraction1.split("/"))
        num2, den2 = map(int, self.fraction2.split("/"))

        product_numerator = num1 * num2
        product_denominator = den1 * den2
        return self.simplify_fraction(product_numerator, product_denominator)

    def input_fractions(self):
        """Gets user input for two fractions."""
        self.fraction1 = input("Введите первую дробь в формате a/b: ")
        self.fraction2 = input("Введите вторую дробь в формате a/b: ")

    def calculate(self):
        """Performs calculations for two fractions and
        displays the results on the screen."""
        self.input_fractions()
        sum_result = self.add_fractions()
        product_result = self.multiply_fractions()

        f1 = fractions.Fraction(int(self.fraction1[0]), int(self.fraction1[2]))
        f2 = fractions.Fraction(int(self.fraction2[0]), int(self.fraction2[2]))

        return (f"Сумма дробей: {sum_result[0]}/{sum_result[1]}, "
                f"Произведение дробей: {product_result[0]}/{product_result[1]}\n"
                f"Сумма дробей(проверка): {f1 + f2}, "
                f"Произведение дробей(проверка): {f1 * f2}")


calculator = FractionCalculator()
print(calculator.calculate())
