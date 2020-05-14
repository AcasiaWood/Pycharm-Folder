# class and objects

class Cake:
    pass
cake = Cake()

# arithmetic operations

class Calculation:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def subtract(self):
        return self.first - self.second
    def multiply(self):
        return self.first * self.second
    def divide(self):
        return self.first / self.second
calculation = Calculation(1, 2)
print(calculation.add(), calculation.subtract(), calculation.multiply(), calculation.divide())

# class inheritance

class Inheritance(Calculation):
    pass
inheritance = Inheritance(3, 4)
print(inheritance.add(), inheritance.subtract(), inheritance.multiply(), inheritance.divide())

# variable of class

class Grade:
    grade = 3
print(Grade.grade)
