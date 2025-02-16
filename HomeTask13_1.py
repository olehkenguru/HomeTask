class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student {self.first_name} {self.last_name} has {self.record_book} books'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def find_student(self, last_name):
        find_student = next((s for s in self.group if s.last_name == last_name), None)
        if find_student:
            return find_student

    def delete_student(self, last_name):
        deleted_student = self.find_student(last_name)
        if deleted_student:
                self.group.remove(deleted_student)
                print(f'The student {last_name} had deleted')
        # else:
        #     print(f'The student {last_name} is not defined in the group {self.number}')

    def __str__(self):
        all_students = ''.join(f'\n{s.first_name} {s.last_name}' for s in self.group)
        return f'Number:{self.number}{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!