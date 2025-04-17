#try:
    # code that may cause error
#except: 
# Can catch a type of error with - except ValueError:
    # handle errors

# Optional finally clause always executes whether an exception occurs or not

# else:
    # code that executes when no exception occurs

try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print('Error! Please enter a number for net sales.')
except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')
except Exception as error:
    print(error)
else:
    print('No errors found')
finally:
    print('I always run!')
