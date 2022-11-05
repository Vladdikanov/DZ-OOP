class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def mean_gr(self):
        all_gr = []
        for i in self.grades.values():
            all_gr += i
        res = sum(all_gr) / len(all_gr)
        return res
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self.mean_gr()}' \
              f'\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res
    def __lt__(self, stud):
        if not isinstance(stud, Student):
            print("Not a studend")
            return
        return self.mean_gr() < stud.mean_gr()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.courses_attached and course in lecturer.grades.keys():
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print("Ошибка")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ["Математика", "Физика", "Программирование"]
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def mean_gr(self):
        all_gr = []
        for i in self.grades.values():
            all_gr += i
        res = sum(all_gr) / len(all_gr)
        return res
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mean_gr()}'
        return res
    def __lt__(self, lec):
        if not isinstance(lec, Lecturer):
            print("Not a lecturer")
            return
        return self.mean_gr() < lec.mean_gr()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
# 1 Экземпляр студента
vova_st = Student("Vova", "Andreev", "man")
vova_st.courses_in_progress.append("Математика")
vova_st.courses_in_progress.append("Физика")
vova_st.courses_in_progress.append("Программирование")
# 2 Экземпляр студента
vika_st = Student("Vika", "Andreeva", "girl")
vika_st.courses_in_progress.append("Математика")
vika_st.courses_in_progress.append("Физика")
vika_st.courses_in_progress.append("Программирование")
# 1 Экземпляр проверяющего
victor_re = Reviewer("Victor","Nosov")
victor_re.rate_hw(vova_st, "Математика", 10)
victor_re.rate_hw(vova_st, "Физика", 9)
victor_re.rate_hw(vova_st, "Программирование", 7)
victor_re.rate_hw(vika_st, "Математика", 7)
victor_re.rate_hw(vika_st, "Физика", 6)
victor_re.rate_hw(vika_st, "Программирование", 10)
# 2 Экземпляр проверяющего(Первый проверяющий уже всен проверил у студета)
katya_re = Reviewer("Ekaterina","Nosova")
katya_re.rate_hw(vova_st, "Математика", 2)
katya_re.rate_hw(vova_st, "Физика", 4)
katya_re.rate_hw(vova_st, "Программирование", 5)
katya_re.rate_hw(vika_st, "Математика", 6)
katya_re.rate_hw(vika_st, "Физика", 7)
katya_re.rate_hw(vika_st, "Программирование", 8)
# 1 Экземпляр лектора
pavel_lec = Lecturer("Pavel", "Tichonov")
vova_st.rate_hw(pavel_lec,"Математика", 6)
vova_st.rate_hw(pavel_lec,"Программирование", 9)
vova_st.rate_hw(pavel_lec,"Физика", 7)
vika_st.rate_hw(pavel_lec,"Математика", 5)
vika_st.rate_hw(pavel_lec,"Программирование", 5)
vika_st.rate_hw(pavel_lec,"Физика", 4)
# 2 Экземпляр лектора
alex_lec = Lecturer("Alex", "Pritchet")
vova_st.rate_hw(alex_lec,"Математика", 9)
vova_st.rate_hw(alex_lec,"Программирование", 8)
vova_st.rate_hw(alex_lec,"Физика", 10)
vika_st.rate_hw(alex_lec,"Математика", 4)
vika_st.rate_hw(alex_lec,"Программирование", 7)
vika_st.rate_hw(alex_lec,"Физика", 7)
print(vika_st)
print(vova_st)
print(victor_re)
print(katya_re)
print(pavel_lec)
print(alex_lec)
print(pavel_lec < alex_lec)
print(vika_st > vova_st)
students = [vika_st, vova_st]
lecturers = [alex_lec, pavel_lec]
courses = ["Математика", "Физика", "Программирование"]
def mean_stud(stud_lst, cours_lst):
    mean_dict = {}
    for cours in cours_lst:
        mean = []
        for stud in stud_lst:
            mean += stud.grades[cours]
        mean_dict[cours] = sum(mean)/len(mean)
    return print(mean_dict)
mean_stud(students,courses)


def mean_lect(lect_lst, cours_lst):
    mean_dict = {}
    for cours in cours_lst:
        mean = []
        for lect in lect_lst:
            mean += lect.grades[cours]
        mean_dict[cours] = sum(mean)/len(mean)
    return print(mean_dict)
mean_lect(lecturers, courses)
