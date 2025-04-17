from Class_person import *
# Inherits from parent class Person
class Child(Person):
    def __init__(self, first_name, last_name, age, sex, title):
        super().__init__(first_name, last_name, age, sex)
        self.title = title

    def introduce_person(self):
        message = f'Starting as a {self.title}.'
        print(super().introduce_person() + message)