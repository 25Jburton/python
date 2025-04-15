# if condition:
#     if-block
def placeByAge():
    example_age = input('Enter your age:')
    example_age = int(example_age)
    if example_age >= 21:
        if example_age <= 44:
            print(f'User as fresh at {example_age}')
        elif example_age >= 44 and example_age <= 59:
            print(f'User as middle at {example_age}')
        elif example_age >= 60:
            print(f'User as above at {example_age}')
    else:
        print(f'User is lower than needed at {example_age}')

# Ternary operator
# value_if_true if condition else value_if_false
def ternaryExample():
    age = input('Enter your age:')
    ticket_price = 20 if int(age) >= 18 else 5
    print(ticket_price)

# For loops - range(start, stop), range(start, stop, step)
# for index in range(n):
#     statement
def exampleForLoop():
    for index in range(0, 18, 2):
        print(index)

# While statements 
# while condition:  
#    body
def exampleWhile():
    number = input('Enter your number:')
    number = int(number)
    while number <= 50:
        print(f'Number entered to small {number}')
        number += 25
        print(f'Number entered +25 = {number}')

# Break statements for exiting a loop or statement
def exampleBreak():
    for index in range(0, 10):
        print(index)
        if index == 3:
            break

# Continue statements for skipping the current iteration in a loop
def exampleContinue():
    for index in range(10):
        if index % 2:
            continue
            print('This print will be skipped')
        # Exits the if statement and continues code execution
        print(index)

# Pass statements for code that is coming in the future but allows execution/compiling without the error for a blank statement
def examplePass():
    example_age = input('Enter your age:')
    example_age = int(example_age)
    if example_age >= 21:
        if example_age <= 44:
            print(f'User as fresh at {example_age}')
        elif example_age >= 44 and example_age <= 59:
            print(f'User as middle at {example_age}')
        elif example_age >= 60:
            pass
            print('Will still render')
    else:
        pass
examplePass()