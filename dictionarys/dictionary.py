# Collection of key-value pairs where each key is associated with a value
# empty_dict = {}
new_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(new_dict['favorite_colors'][1])
print(new_dict.get('favorite_colors')[1])
# Using get allows checking for value not in dictionary without error
print(new_dict.get('bad_index'))

new_dict['new_index'] = 'just added'
print(new_dict)
# Removing from dictionary 
del new_dict['new_index']

# Looping the full dictionary with index & values .items()
print(new_dict.items())
# Printing the keys
for key in new_dict:
    print(key)
# Printing the values
for value in new_dict.values():
    print(value)

# Dictionary Comprehension - {key:value for (key,value) in dict.items() if condition}
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}
""" 
Iterates over items of a dictionary and allows you to 
create a new dictionary by transforming or filtering each item. 
"""
new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

print(new_stocks)