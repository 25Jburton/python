user_name = input('Enter your name: ')

def greet(name):
    """ Describe the function """
    return f"Hi {name}"
# print(greet(user_name))

def greet2(name, message='Hi'):
    """ Required and default set params """
    return f"{message} {name}"
#print(greet2(user_name, 'Would you look at that its'))

def greet3(name='Default', message='Hi'):
    """ Required and default set params """
    return f"{message} {name}"
#print(greet3(message='Would you look at that its old no name'))

# All the arguments after the first keyword argument must also be keyword arguments too.
output_result = greet3(name=user_name ,message='Would you look at that its')
#print(output_result)

user_number = input('Enter your number: ')
# Recursion 
def sum(n):
    if n > 0:
        return n + sum(n-1)
    return 0

result = sum(int(user_number))
print(result)


# lambda Expressions for 1 time functions
# lambda parameters: expression
def times(n):
    return lambda x: x * n
# Call the main function
double = times(2)
# Call the lambda returned function
result = double(int(user_number))
print(result)

# Example in loop
callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())

# Doc stings
# Call to built in help() to describe the function
help(greet)
""" 
Output 

Help on function greet in module __main__:

greet(name)
    Describe the function
"""
# Directly return the doc string of the function - functionName.__doc__
print(greet.__doc__)
"""
Output 
Describe the function
"""