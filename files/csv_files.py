import csv

with open('./files/myFile.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the first row
    next(csv_reader)

    # show the data
    for line in csv_reader:
        # print(line)
        pass

# With DictReader
with open('./files/myFile.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    next(csv_reader)
    for line in csv_reader:
        print(f"{line}")


# Writing to CSV - will OVERWRITE contents if the csv already exists 
#  newline='' will ensure no blank lines
header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('./files/myNewFile.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

# Writing to using DictWriter - will OVERWRITE contents if the csv already exists 
# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code4']

# csv data
rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code4': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code4': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code4': 'ASM'}
]

with open('./files/myNewFile.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Removing file
import os

try:
    os.remove('./files/myNewFile2.csv')
except FileNotFoundError as e:
    print(e)

# renaming a file 
import os

try:
    os.rename('./files/myNewFile.csv', './files/notes.csv')
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)