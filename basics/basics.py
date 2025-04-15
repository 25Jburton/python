# Basics of Python coding

# Simple print statements
# print('Whatever you need')

# Functions
def myFunc():
    driver = 'Max V'
    team = 'Red Bull'
    full_message = f'{driver} currently races for the {team} team'
    print(driver+' currently races for the '+team+' team')
    print(full_message)
# Calling the function
# myFunc()

# No ending markers, uses white space and indents to structure the code
def myLongExample(a=True,b=False,c=True):
    # breaking the long line up with the \ 
    if (a == True) and (b == False) and \
   (c == True):
        # Inner code for statement needs to be indented 
        print("Continuation of statements")
    else:
        print("Else statement")
# Just like other langs can set defaults for passed params, when passed via the function call overwrites the matching default
# myLongExample(False)

# Ability to import modules
import keyword
# print(keyword.kwlist) 

# Strings 
raw_string = r'my_raw/string/'
one_liner = 'Just a simple string'
multi_liner = '''line1
line2 Longer string that spans multiple lines
line3 example
line4'''

# Ways to use vars within our strings
driver = 'Max V'
team = 'Red Bull'
# with f-string
full_message = f'{driver} currently races for the {team} team'
# with concatenation 
# print(driver+' currently races for the '+team+' team')

# Including quotes 
quote_string = 'As Max says, "Simply Lovely!"'
# Getting the length of the string with - len()
# print(len(quote_string))
# Slicing the string by indexes - [3:6]
# print(quote_string[3:6])

# Strings are immutable - can not be updated

# Variable Naming
my_variable_name = ''
my_number_variable = 1

#Numbers
my_int = 1
my_float = 1.1
long_number = 100_000_100_000
# exponents **
my_exponent = 2 ** 2
# print(my_exponent)

# Booleans 
valid = True #
invalid = False # 0, '', None, {}, ()

# No constants in python - name with all CAPITALS to denote

# Conversions 
# int(), float(), bool(), str(), type()

# Basic user input call
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

tax_amount = int(price) * float(tax) / 100
print(f'The tax amount is ${tax_amount}')
