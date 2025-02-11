class Teacher: 
    teachers = []
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        Teacher.teachers.append(self.__name)
    
    def get_name(self):
        return self.__name
    
    def get_education(self):
        return self.__education
    
    def get_experience(self):
        return self.__experience
    
    def set_experience(self, new_experience):
        self.__experience = new_experience
    
    def get_teacher_data(self):
        data = f'{self.__name}, образование {self.__education}, опыт работы {self.__experience} года.'
        return data
    
    def add_mark(self, name_student, rate_student):
        self.name_student = name_student
        self.rate_student = rate_student
        rate = f'{self.__name} поставил оценку {rate_student} студенту {name_student}.'
        return rate
    
    def remove_mark(self, name_student, rate_student):
        self.name_student = name_student
        self.rate_student = rate_student
        rate = f'{self.__name} удалил оценку {rate_student} студенту {name_student}.'
        return rate
    
    def give_a_consultation(self, consultations):
        self.consultations = consultations
        consultation = f'{self.__name} провел консультацию в классе {self.consultations}.'
        return consultation
    
    @staticmethod
    def dismissal_teachers(teach):
        if teach in Teacher.teachers:
            Teacher.teachers.remove(teach)
            return f'Учитель {teach} был уволен'
        else:
            return f'Учителя {teach} уже уволили'
        
    
class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title
    
    def get_discipline(self):
        return self.__discipline
    
    def get_job_title(self):
        return self.__job_title
    
    def set_job_title(self, job_title):
        self.__job_title = job_title
    
    def get_teacher_data(self):
        data = super().get_teacher_data()
        data1 = f'Предмет {self.__discipline}, должность {self.__job_title}'
        return data, data1   
    
    def add_mark(self, name_student, rate_student):        
        rate_old = super().add_mark(name_student, rate_student)
        rate1 = f'Предмет: {self.__discipline}'
        return rate_old, rate1
    
    def remove_mark(self, name_student, rate_student):
        rate_old = super().remove_mark(name_student, rate_student)
        rate1 = f'Предмет: {self.__discipline}'
        return rate_old, rate1
    
    def give_a_consultation(self, consultations):
        consultation_old = super().give_a_consultation(consultations)
        consultation = f'По предмету {self.__discipline} как {self.__job_title}'
        return consultation_old, consultation   

#используем подкласс  
   
teacher1 = DisciplineTeacher('Иван Петров', 'РГУ', 4, 'Химия', 'Учитель 1 категории')
teacher2 = DisciplineTeacher('Глеб Орлов', 'МГУ', 10, 'География', 'Завуч')
teacher3 = DisciplineTeacher('Юлия Савина', 'РГРТУ', 1, 'Физика', 'Учитель')

# print(teacher1.get_name())
# print(teacher1.get_education())
# print(teacher1.get_experience())
# teacher1.set_experience(2)

# print(*teacher1.get_teacher_data(), sep = '\n')
# print(*teacher1.add_mark('Николай Попов', 5), sep = '\n')
# print(*teacher1.remove_mark('Ангелина Скрябина', 3), sep = '\n')
# print(*teacher1.give_a_consultation('9Б'), sep = '\n')

#Проверка,что функция удаления работает
# print(Teacher.teachers)
# print(Teacher.dismissal_teachers('Иван Петров'))
# print(Teacher.teachers)
