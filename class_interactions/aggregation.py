from typing import List


class Department:
    def __init__(self, name):
        self.name = name

    def show_department(self):
        print(f"Department: {self.name}")


class University:
    def __init__(self, name):
        self.name = name
        self.departments: List[Department] = []

    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        print(f"University: {self.name}")
        for department in self.departments:
            department.show_department()


department1 = Department("Computer Science")
department2 = Department("Mathematics")

university = University("Oxford University")

university.add_department(department1)
university.add_department(department2)
university.show_departments()
