from Class_person import *
# Inherits from parent class Person
class Child(Person):
    def __init__(self, first_name, last_name, age, sex, title):
        super().__init__(first_name, last_name, age, sex)
        self.title = title

    def introduce_person(self):
        """ Basic overwrite function for child class to send a greeting """
        message = f'Starting as a {self.title}.'
        print(super().introduce_person() + message)

    @property
    def title(self):
        """ Getter function for the title attribute """
        return self._title

    @title.setter
    def title(self, value):
        """ Setter function for title attribute """
        if len(value) <= 3:
            raise ValueError('The title must be more than 3 chars long')
        self._title = value

    @title.deleter
    def title(self):
        del self._title

    """ The property() class, can add a property to a class while maintaining backward compatibility """
    #title = property(fget=get_title, fset=set_title) - deprecated from above