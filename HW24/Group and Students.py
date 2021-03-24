class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        self.__grades = grades

    def add_grade(self, grade):
        self.__grades.append(grade)

    def __str__(self):
        return 'Name: {n}, age: {a}, grades: {g}'.format(
            n=self.__name,
            a=self.__age,
            g=', '.join(str(grade) for grade in self.__grades)
        )


class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_students(self, *students):
        for student in students:
            self.__students.append(student)

    def __str__(self):
        return 'Group: {g}\n{st}\n'.format(
            g=self.__name,
            st='\n'.join(str(s) for s in self.__students)
        )


st1 = Student('Dima', 24)
st1.grades = [5, 5, 5, 5, 5, 5]
st2 = Student('Vova', 11)
st2.grades = [5, 5, 5, 5, 5, 5]
st3 = Student('Anton', 90)
st3.grades = [5, 5, 5, 5, 5, 5]

g = Group('Group A')
g.add_students(st1, st2, st3)
print(g)