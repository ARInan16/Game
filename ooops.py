class Member:
    no_of_leaves = 9

    def __init__(self, a, b, c, ):
        self.name = a
        self.age = b
        self.salary = c

    def identity(self):
        return f"the name is{self.name} age is {self.age} salary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.age / other.age

    def __repr__(self):
        return f"Employee('{self.name}' {self.age}  {self.salary})"

    def __str__(self):
        return f"the name is {self.name} age is {self.age} salary is {self.salary}"

