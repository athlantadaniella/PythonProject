class GroupOverflowError(Exception):
    pass


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupOverflowError("У групі не може бути більше 10 студентів")
        self.students.append(student)

    def __str__(self):
        return f"Group {self.group_name}: {[str(s) for s in self.students]}"


group = Group("Python-101")

try:
    for i in range(11):
        student = Student(f"Student_{i + 1}")
        group.add_student(student)
        print(f"Додано {student}")

except GroupOverflowError as e:
    print("Помилка:", e)

print(group)