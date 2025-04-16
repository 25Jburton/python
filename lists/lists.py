# Lists are similar to arrays in other langs
my_list = ['item1', 'item2', 'item3', 'item4']

# similar to the multi dimensional arrays
my_nested_list = [[1,2],[1,3],[7,6],5]
# Updating current item by index
my_nested_list[-1] = [5,6]
# Adding to the end of list
my_nested_list.append([3,3])
# Adding to any index of list
my_nested_list.insert(2,[2,2])
print(my_nested_list)

# Removing from the list by index
del my_nested_list[0]
# Pop to remove and return the removed index
popped_index = my_nested_list.pop(1)
print(popped_index)
print(my_nested_list)
# Remove by value (Only takes one argument and removes first instance ONLY)
my_nested_list.remove([1,3])
print(my_nested_list)

# Tuples - List that don't change
# Single item tuple requires trailing comma
my_single_tuple = (4,)
my_tuple = ('Cyan', 'Magenta', 'Yellow', 'black')
# Only way to alter would be creating a new tuple with the same name to overwrite 
my_tuple = ('Cyan', 'black')

# Sorting lists
my_sort_list = [10,5,7,8,6,4,5,3,1]
# smallest to largest .sort()
my_sort_list.sort()
print(my_sort_list)
# largest to smallest .sort(reverse=True)
my_sort_list.sort(reverse=True)
print(my_sort_list)
# Sorting strings 
my_string_list = ['zebra', 'Cow', 'Apple', 'Lion']
# Alphabetical .sort()
my_string_list.sort()
print(my_string_list)
my_string_list.sort(reverse=True)
print(my_string_list)

# Sorting list of tuples 
companies = [
    ('Google', 2019, 134.81),
    ('Apple', 2019, 260.2),
    ('Facebook', 2019, 70.7)
]
# define a sort key based of index
def sort_key(company):
    return company[2]
# sort the companies by revenue
companies.sort(key=sort_key, reverse=True)
# show the sorted companies
print(companies)

# Sorting with lambda
companies.sort(key=lambda company: company[0])
print(companies)

# Sorted to not modify the original list but create a new one 
new_sorted_list = sorted(companies,reverse=True)
print(new_sorted_list)

# Slice to get partial list sub_list = list[begin: end: step]
sub_list = companies[0:2]
sub_list = companies[:2] # omitting the 1st will be treated as start till index provided 
print(sub_list)

sub_list = companies[-2:] # omitting the last will be treated as end till index provided 
print(sub_list)

# reversing with step 
sub_list = companies[::-1]
print(sub_list)

# Overwriting from indexes
my_string_list[0:1] = ['New Item in spot'] # if new item is 1 index but the call is to more the other indexes will be removed
print(my_string_list)

# Removing multiple indexes 
del my_string_list[0:2]
print(my_string_list)

# Packing a list
colors = ['red', 'blue', 'green', 'purple', 'yellow']
# Assign element of a list to a var
# *other assigned to remaining 
firstElement, secondElement, *other = colors
# Based on the index not matching text value
print(firstElement)
print(secondElement)
print(other)

# Looping list items for item in list:
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for city in cities:
    print(city)

# Adding index and turning list into tuple with enumerate()
for city in enumerate(cities):
    print(city)

# Unpack tuple to use the index
for index, city in enumerate(cities):
    print(f"{index}: {city}")
print()
# Unpack tuple to use the index at given index enumerate(list, index)
for index, city in enumerate(cities, 2):
    print(f"{index}: {city}")

# Getting the index of item by value
targetIndex = cities.index('Mumbai') # Will throw error if value is not in the list
print(targetIndex)

# Checking if value is in list 
value_to_find = 'not in list'
if value_to_find in cities:
    print('Found item')
else:
    print('Not in the list')

# Iterating numbers
for index in range(3):
    print(index)
# Iterating strings
str = 'Iterables'
for ch in str:
    print(ch)

# Turning a list into an iterator 
colors = ['red', 'green', 'blue']
# Use iter to convert
colors_iter = iter(colors)
# Use next to get the next value
color = next(colors_iter)
print(color)

color = next(colors_iter)
print(color)

color = next(colors_iter)
print(color)

# Or just loop over the created iterator
colors_iter = iter(colors)
for color in colors_iter:
    print(color)

# Iteration with .map() - iterator = map(fn, list) 
# fn = the function to be called for each element of the list
new_map = map(lambda name: name.capitalize(), colors)
# Convert the iterator result back into a list
new_map = list(new_map)
print(new_map)

# filter(fn, list)
example_scores = [77,81,99,72,65,22,100,98,32]
good_numbers = filter(lambda score: score > 75, example_scores)
print(list(good_numbers))

# Turn list into single value with reduce(fn,list)
from functools import reduce
reduced_list = reduce(lambda scoreA, scoreB: (scoreA + scoreB), example_scores)
average_score = reduced_list / len(example_scores)
print(average_score)

# List Comprehension [output_expression for element in list]
print([score*2 for score in example_scores])
# List Comprehension [output_expression for element in list if condition]
print([score*2 for score in example_scores if score >= 75])