### this data does not append. It overrides the existing data. 
### old way
f = open('new1.txt', 'w')
f.write('Lorem ipsum dolor sit amet, consecteturadipiscing elit.')
f.close()

## using Context Manager 'with' statement
with open('new1.txt', 'w') as f:
    f.write('This one is using Context Manager. Check it out')
    
### you can use Context Manager "with" statement 2 ways:
##### 1) Using "Class"
##### 2) Using "Generators/Decorators"

### Using Class 
class Open_file():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_file('new1.txt', 'w') as f:
    f.write("Testing Yasmine")
print(f.closed)

### Using "Generators/Decorators" import "contextlib" module

from contextlib import contextmanager

@contextmanager
def Open_file1(file, mode):
    f = open(file, mode)
    yield f
    f.close()
    
with Open_file1("new1.txt", "w") as f:
    f.write("This is contextlib module import")
print(f.closed)
