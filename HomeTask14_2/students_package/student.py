from students_package.human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student {self.first_name} {self.last_name}, book record: {self.record_book}'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __hash__(self):
        return hash(str(self))