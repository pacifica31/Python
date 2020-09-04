## 1) Ternary Operators/Conditional Expressions
## Long Way
condition = False
if condition: 
    x = 1
else:
    x =0
print(x)

### Short way
condition = False
x = 1 if condition else 0
print(x)

## 2) Working with Large Numbers
## Long way
num1 = 10000000000
num2 = 100000000
total = num1 + num2
print(total)

## Short way
num1 = 10_000_000_000
num1 = 10_000_000_000
total = num1 + num2
print(f'{total:,}')

## 3) Code smell/ Context Manager(contexlib)/ Manually Open & Close file
## Long way
f = open('new1.txt', 'r')
file_contents = f.read()
f.close()
words = file_contents.split(' ')
word_count = len(words)
print(word_count)

## short way
with open('new1.txt', 'r') as f:
    file_contents = f.read()
words = file_contents.split(' ')
word_count = len(words)
print(word_count)

### 4) Enumerate Function
## Long way
names = ["Corey", "Chris", "Dave", "Travis"]
index = 0
for name in names:
    print(index, name)
    index +=1 
## Short way
names= ["Corey", "Chris", "Dave", "Travis"]
for index, name in enumerate(names, start=1):
    print(index, name)
    
## 5) Zip / It allows you to loop over 2 lists at once
## Long way
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
hereos = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for index, name in enumerate(names):
    hero = hereos[index]
    print(f'{name} is actually {hero}')
    
## Short way
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
hereos = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for name, hereos in zip(names, hereos):
    print(f'{name} is actually {hero}')

## 6) Unpacking/ putting asterix infront of c will print the remaining numbers
a, b, *c, d= (1,2,3,4,5)
print(a)
print(b)
print(c)
print(d)
## if you want to ignore multiple/middle values
a, b, *_, d = (1,2,3,4,5,6,7)
print(a)
print(b)
print(d)

## 7) Setattr / Getattr
## Setattr
class Person():
    pass
person = Person()
first_key = 'first'
first_val = 'Corey'
setattr(person, first_key, first_val)
print(person.first)

## Getattr
class Person1():
    pass
first_key = 'first'
first_val = 'Corey'
first = getattr(person, first_key)
print(first)

## more example Setattr
#class Person():
#    pass
#person = Person()
#person_info = {'first': 'Corey', 'last': 'Shafer'}
#for key, value in person_info.items():
#   setattr(person, key, value)
#print(person.first)
#print(person.last)

## more example Getattr
#class Person():
#    pass
#person = Person()
#person_info = {'first': 'Corey', 'last': 'Shafer'}
#for key in person_info.keys():
#    print(getattr(person, key))
 
## 8) Getpass/ hides password/personal/secret information
## Long way without using getpass module.. you can see the password
username = input('Username: ')
password = input('Password: ')
print('Logging In..')

## Correct way using getpass module.. the function hides the sercret information
from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')
print('Logging In...')

## 9) Help/Dir  example: smtpd module is an example import to show the help/dir
import smtpd
help(smtpd)

from datetime import datetime
dir(datetime)