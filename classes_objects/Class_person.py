class Person:
    counter = 0
    default_message = 'Testing'
    def __init__(self, first_name, last_name, age, sex = 'N/A'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.sex = sex
        Person.counter += 1

    @classmethod
    def my_person_class_method(cls,new_value):
        """
            First argument of a class method is the class itself - cls
            Allows the method to access and modify class-level attributes, create factory methods, and interact with the class itself
        """
        cls.default_message = new_value

    # Static can be called without needing instance of class itself
    @staticmethod
    def my_static_function(arg1,arg2):
        print(arg1 * arg2)
    
    def welcome(self):
        print('Welcome to the show!')

    def introduce_person(self):
        """ Function that takes all persons data and returns an introduction message based on the provided age. """
        if self.age <= 20:
            return f"""
                Hello, {self.first_name} {self.last_name}, welcome to the application.
                Unfortunately, due to your age of {self.age} we can't allow you to proceed any further.
            """
        elif(self.sex == 'M' or self.sex == 'm'):
            return f"""
                Hello, {self.first_name} {self.last_name}, welcome to the application.
                We are glad to welcome another man to join the team.
            """
        elif(self.sex == 'F' or self.sex == 'f'):
            return f"""
                Hello, {self.first_name} {self.last_name}, welcome to the application.
                We are glad to welcome another female to join the team.
            """