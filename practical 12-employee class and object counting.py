class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Aman", 30000)
e2 = Employee("Riya", 40000)
e3 = Employee("Neha", 35000)

e1.display()
e2.display()
e3.display()

print("Total employees:", Employee.count)
