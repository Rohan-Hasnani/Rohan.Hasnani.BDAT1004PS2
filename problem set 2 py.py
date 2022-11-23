Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 0
def b():
    global a
    a = c(a)

    
def c(a):
    return a + 2

b()
b()
b()
a
6
def file_length(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        file.close()    print(len(contents))
        
SyntaxError: invalid syntax
def file_length(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        file.close()    print(len(contents))
        
SyntaxError: invalid syntax
def file_length(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        file.close()    print(len(contents))
        
SyntaxError: invalid syntax
def file_length(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        file.close()
        print(len(contents))
    except:
        print("File" + file_name + "not found.")

        
class marsupil:
    list = []
    def put_in_pouch(self, name):
        list.append(name)
    def pouch(self):
        print(list)

        
m = marsupil()
m.put_in_pouch('doll')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    m.put_in_pouch('doll')
  File "<pyshell#26>", line 4, in put_in_pouch
    list.append(name)
TypeError: descriptor 'append' for 'list' objects doesn't apply to a 'str' object

class marsupil:
    listl = []
    def put_in_pouch(self, name):
        listl.append(name)
    def pouch(self):
        print(list)

        
m = marsupil()
m.put_in_pouch('doll')
SyntaxError: multiple statements found while compiling a single statement
m = marsupil()

m = marsupil()
m.put_in_pouch('doll')
SyntaxError: multiple statements found while compiling a single statement
m.put_in_pouch('doll')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    m.put_in_pouch('doll')
  File "<pyshell#31>", line 4, in put_in_pouch
    listl.append(name)
NameError: name 'listl' is not defined. Did you mean: 'list'?




class marsupil:
    global listl = []
    def put_in_pouch(self, name):
        listl.append(name)
    def pouch(self):
        print(list)
        
SyntaxError: invalid syntax



global listl
class marsupil:
    listl = []
    def put_in_pouch(self, name):
        listl.append(name)
    def pouch(self):
        print(list)

        
m = marsupil()
m.put_in_pouch('doll')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    m.put_in_pouch('doll')
  File "<pyshell#46>", line 4, in put_in_pouch
    listl.append(name)
NameError: name 'listl' is not defined. Did you mean: 'list'?






class marsupil:
    def __init__(self):
        self.listl = []
    def put_in_pouch(self, name):
        listl.append(name)
    def pouch(self):
        print(list)

        
m = marsupil()
m.put_in_pouch('doll')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    m.put_in_pouch('doll')
  File "<pyshell#55>", line 5, in put_in_pouch
    listl.append(name)
NameError: name 'listl' is not defined. Did you mean: 'list'?




class marsupil:
    def __init__(self):
        self.listl = []
    def put_in_pouch(self, name):
        self.listl.append(name)
    def pouch(self):
        print(self.listl)

        
m = marsupil()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
m.pouch()
['doll', 'firetruck', 'kitten']


class kangaroo(marsupil):
    def __init__(self, x, y):
        marsupil.__init__(self)
        self.x = x
        self.y = y
    def jump(self, dx, dy):
        self.x += dx
        self.y += dy
    def __str__(self):
        return 'I am Kangaroo located at coordinates (' + str(self.x) + ',' + str(self.y) +').'

    
m = marsupil()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
m.pouch()
['doll', 'firetruck', 'kitten']

k = Kangaroo(0,0)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    k = Kangaroo(0,0)
NameError: name 'Kangaroo' is not defined. Did you mean: 'kangaroo'?
k = kangaroo(0,0)
print(k)
I am Kangaroo located at coordinates (0,0).
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
l.pouch()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    l.pouch()
NameError: name 'l' is not defined
k.pouch()
['doll', 'firetruck', 'kitten']
>>> k.jump(1,0)
>>> k.jump(1,0)
>>> k.jump(1,0)
>>> print(k)
I am Kangaroo located at coordinates (3,0).
>>> 
>>> 
>>> 
>>> def colatz(n):
...     print(n)
...     if n==1:
...         return
...     elif n%2 == 0:
...         return colatz(n//2)
...     else:
...         return colatz(n*3+1) #Recursive call
... 
...     
>>> colatz(1)
1
>>> colatz(10)
10
5
16
8
4
2
1
>>> 
>>> 
>>> def binary(number):
...     if n < 2:
... 
...         print n
...         
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> 
>>> 
>>> 
>>> def binary(number):
    if n < 2:
        print n
        
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?




def binary(number):
    if n < 2:
        print (n)
    else:
        binary (n/2)
        print(n % 2)

        
binary(0)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    binary(0)
  File "<pyshell#133>", line 2, in binary
    if n < 2:
NameError: name 'n' is not defined




def binary(number):
    if number < 2:
        print (number)
    else:
        binary (number/2)
        print(number % 2)

        
binary(0)
0
binary(1)
1
binary(3)
1.5
1
def binary(number):
    if number < 2:
        print (number)
    else:
        binary (number/2)
        print number % 2
        
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

def binary(number):
    if number < 2:
        print (number)
    else:
        binary (number//2)
        print number % 2
        
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?




def binary(number):
    if number < 2:
        print (number)
    else:
        binary (number//2)
        print (number % 2)

        
binary(0)
0
binary(1)
1
binary(3)
1
1
binary(9)
1
0
0
1



words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
lst = [i.upper() for in words]
SyntaxError: invalid syntax
lst = [i.upper() for i in words]
print(lst)
['THE', 'QUICK', 'BROWN', 'FOX', 'JUMPS', 'OVER', 'THE', 'LAZY', 'DOG']
lst = [i.lower() for i in words]
print(lst)
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
lst = [len(i) for i in words]
print(lst)
[3, 5, 5, 3, 5, 4, 3, 4, 3]
lst = [[i.upper(), i.lower(), len(i)] for in in words]
SyntaxError: invalid syntax
lst = [[i.upper(), i.lower(), len(i)] for i in words]
print(lst)
[['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]
lst = [i.lower() for i in words if len(i) > 4]
print(lst)
['quick', 'brown', 'jumps']
lst = [i.lower() for i in words if len(i) >= 4]
print(lst)
['quick', 'brown', 'jumps', 'over', 'lazy']

================= RESTART: E:/BDAT/Data Programming/problem7.py ================
Traceback (most recent call last):
  File "E:/BDAT/Data Programming/problem7.py", line 7, in <module>
    class HeadingParser(HParser):
NameError: name 'HParser' is not defined. Did you mean: 'HTMLParser'?

================= RESTART: E:/BDAT/Data Programming/problem7.py ================
Traceback (most recent call last):
  File "E:/BDAT/Data Programming/problem7.py", line 29, in <module>
    hp = HeadingParser(co)
NameError: name 'co' is not defined

================= RESTART: E:/BDAT/Data Programming/problem7.py ================
Traceback (most recent call last):
  File "E:/BDAT/Data Programming/problem7.py", line 29, in <module>
    hp = HeadingParser(content)
TypeError: HTMLParser.__init__() takes 1 positional argument but 2 were given

================= RESTART: E:/BDAT/Data Programming/problem7.py ================
1
W3C Mission

	
2
	Principles
	
 



	

