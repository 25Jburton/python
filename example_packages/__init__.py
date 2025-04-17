#  to initialize the package-level data
from example2 import function1 as mainFunc
# if nested in folder just use package.folder

# call all files in __all__ list 
__all__ = [
    'example1',
    'example2'
]


mainFunc()