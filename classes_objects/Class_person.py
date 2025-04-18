class Person:
    counter = 0
    default_message = 'Testing'
    def __init__(self, first_name, last_name, age, sex = 'N/A'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.sex = sex
        Person.counter += 1

    def __str__(self):
        """ String representation of the persons class. human-readable - print(my_new_person) """
        return f'({self.first_name},{self.last_name},{self.age},{self.sex})'
    
    def __repr__(self):
        """ method returns a string representation of an object that is machine-readable """
        return f'Person({self.first_name},{self.last_name},{self.age},{self.sex})'

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

    def __eq__(self, other):
        """ To define the equality logic for comparing two objects using the equal operator. \n
        Uses the is operator for comparisons """
        if isinstance(other, Person):
            return self.age == other.age
        return False
    
    def __hash__(self):
        """ Uses the id of objects """
        return hash(self.age)
    
    def __bool__(self):
        """ Implement the __bool__ method to override the default. The __bool__ method must return either True or False \n
        To return a boolean value for an object"""
        if self.age < 18 or self.age > 65:
            return False
        return True
    
    def __del__(self):
        """ To define behavior when an object is about to be destroyed by the garbage collector \n
        Python calls the __del__ method right before the garbage collector destroys the object """
        print(f'__del__ was called for {self.__dict__}')

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