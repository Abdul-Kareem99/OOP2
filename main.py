class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grades(self):
        res = sum(sum(list(self.grades.values()), [])) / len(self.grades)
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_grades()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Пройденные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grades() < other.average_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        res = sum(sum(list(self.grades.values()), [])) / len(self.grades)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_grades()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grades() < other.average_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


john = Student("John", "Smith", "male")
john.courses_in_progress += ["Python"]
john.finished_courses += ["Git", "Введение в программирование"]

beth = Student("Beth", "Hawkins", "female")
beth.courses_in_progress += ["Git"]
beth.finished_courses += ["Введение в программирование", "Python"]

ruoy = Student("Ruoy", "Eman", "male")
ruoy.courses_in_progress += ["Python", "Git"]
ruoy.finished_courses += ["Введение в программирование"]

zoey = Student("Zoey", "Grin", "female")
zoey.courses_in_progress += ["Введение в программирование"]
zoey.finished_courses += ["Git", "Python"]


peter = Lecturer("Peter", "Mustang")
peter.courses_attached += ["Введение в программирование"]

oleg = Lecturer("Oleg", "Bulygin")
oleg.courses_attached += ["Git", "Python"]


scarlett = Reviewer("Scarlett", "Fox")
scarlett.courses_attached += ["Введение в программирование"]

bruce = Reviewer("Bruce", "Wayne")
bruce.courses_attached += ["Python", "Git"]


bruce.rate_hw(john, "Python", 7)
bruce.rate_hw(beth, "Git", 5)
bruce.rate_hw(ruoy, "Python", 9)
bruce.rate_hw(ruoy, "Git", 6)
scarlett.rate_hw(zoey, "Введение в программирование", 7)

john.rate_hw(oleg, "Python", 9)
beth.rate_hw(oleg, "Git", 6)
ruoy.rate_hw(oleg, "Python", 10)
ruoy.rate_hw(oleg, "Git", 8)
zoey.rate_hw(peter, "Введение в программирование", 8)

# john.__str__()
# beth.__str__()
# ruoy.__str__()
# zoey.__str__()
# oleg.__str__()
# peter.__str__()
# bruce.__str__()
# scarlett.__str__()

# print(john.grades)
# print(beth.grades)
# print(ruoy.grades)
# print(zoey.grades)
# print(oleg.grades)
# print(peter.grades)


# print(bruce.__str__())
# print(oleg.__str__())
# print(ruoy.__str__())
# print(beth < john)
# print(beth > john)
# print(peter < oleg)
# print(peter > oleg)
# print(peter > john)
# print(peter < john)

students = [john, beth, ruoy, zoey]
lecturers = [oleg, peter]


def avg_hw_for_course(students, course):
    sum_hw = 0
    count = 0
    for student in students:
        if course in student.grades:
            sum_hw += sum(student.grades[course]) / len(student.grades[course])
            count += 1
    return sum_hw / count


def avg_lectures_for_course(lecturers, course):
    sum_hw = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            sum_hw += sum(lecturer.grades[course]) / len(lecturer.grades[course])
            count += 1
    return sum_hw / count


print(avg_hw_for_course(students, "Python"))
print(avg_hw_for_course(students, "Git"))
print(avg_hw_for_course(students, "Введение в программирование"))

# print(avg_lectures_for_course(lecturers, "Python"))
# print(avg_lectures_for_course(lecturers, "Git"))
# print(avg_lectures_for_course(lecturers, "Введение в программирование"))

# print(ruoy.grades)
# print(sum(list(ruoy.grades.values()), []))
# print(sum(sum(list(ruoy.grades.values()), [])) / len(ruoy.grades))