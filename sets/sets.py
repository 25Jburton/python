# Sets are unordered immutable lists with unique values(Case sensitive)
# Empty sets must use set() due to {} reading as an empty dictionary
empty_set = set()

skills = {'Python programming', 'Databases', 'Software design'}

# Creating a set from from a list
new_set = set(['item1','item2','item3','item4','item5'])
print(new_set)

# Creating a set from chars, will remove all duplicates to keep set unique
char_set = set('myStringgg')
print(char_set)

# Checking if value is in a set
target_value = 'g'
if target_value in char_set:
    print('Found')

# Checking if not in set
bad_target_value = 'x'
if bad_target_value not in char_set:
    print('Not found')

# Adding to the set, if value is already in will have no effect
char_set.add('z')
print(char_set)

# Removing from the set, if value is not present will throw an error
char_set.remove('z')
print(char_set)

# If not sure the value to be removed is present 
if 'x' in char_set:
    char_set.remove('x')
else:
    print('Value not in set')

# Better way for sets is with set.discard(element)
char_set.discard('x')

# Clearing a set - set.clear()
char_set.clear()
char_set.add('A')
char_set.add('a')
char_set.add('B')
char_set.add('b')
char_set.add('C')
char_set.add('c')
print(char_set)

# Make set immutable
char_set = frozenset(char_set)
print(type(char_set))

# Create new set with comprehension 
tags = {'Django', 'Pandas', 'Numpy'}
# {expression for element in set if condition}
lowercase_tags = {tag.lower() for tag in tags}

print(lowercase_tags)

# Use union() to get a new set that contains distinct elements from both sets
# new_set = set.union(another_set, ...) OR new_set = set1 | set2
set1 = set(['item1','item2','item3','item4','item5'])
set2 = set(['Item1','item2','Item3','item4','Item5'])
union_set = set1 | set2 # only allows sets, not iterables
set3 = ['item1','item2','item3','item4','item5'] # iterable list not a set, use union()
set4 = {'item2', 'Item6'}
union_set = set4.union(set3)

print(union_set)

# Getting values in both sets with intersection()
# new_set = set1.intersection(set2, set3)
# new_set = set1 & set2 & set3
intersection_set = set1 & set2 & set4
# use intersection() for sets and iterables
intersection_set = set1.intersection(set2 , set3)
print(intersection_set)

# Getting the differences from sets
# difference() or set - set
difference_set = set1 - set2 - set4
print(difference_set)

# Symmetric Difference - set of elements that are in all sets, but not in their intersections
# new_set = set1.symmetric_difference(set2, set3,...)
# new_set = set1 ^ set2

# Checking if subset()
# Set A is a subset of set B if all elements of A are also elements of B. 
# Then, set B is a superset of set A
subset_set = set1.issubset(set2)
# Subset with operator <=
subset_set = set1 <= set2
print(subset_set)

# Checking if superset()
subset_set = set1.issuperset(set2)
# Subset with operator <=
subset_set = set1 >= set2
print(subset_set)

# disjoint when they have no elements in common
disjoint_set = set1.isdisjoint(set2)
print(disjoint_set)