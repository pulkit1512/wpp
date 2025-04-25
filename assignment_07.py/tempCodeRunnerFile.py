class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

# Example usage
emp1 = Employee("Alice", 5000)
emp2 = Employee("Bob", 4000)
print(emp1 + emp2)
print(emp1 - emp2)