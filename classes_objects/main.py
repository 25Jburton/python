from Class_person import *
from Class_child import *

my_new_person = Person('Bob', 'Belcher', '42', 'M')
my_person2 = Person('Linda', 'Belcher', '38', 'F')
print(Person.default_message)
Person.my_person_class_method('Reset the message')
my_person3 = Person('Linda', 'Belcher', '38', 'F')
print(Person.default_message)
print(Person.counter)

Person.my_static_function(int(10), int(5))

# Call to our child class 
my_child = Child('James', 'Burton', '30', 'M', 'Developer')
my_child.introduce_person()
# Call from child to parent function
my_child.welcome()