# Playing with AST in python

This repo contains the solutions for two programming challenges designed to get hands-on experience with AST's in Python

## Challenge 1
Write a code that reads a python file, transforms and saves it as a new python file.  
We need these transformations for all ​functions​ and ​public methods​*: 
- Rename: Append ‘_1’. 
- Change all integer values: Make them negative.  

### Example
input1.py (original)
```python
def func(x):
    return x + 4


class Foo(object):
    def __init__(self):
        self.x = 2

    def bar(self):
        self.x += 1


func(10)
f = Foo()
f.bar()
```
output1.py (transformed)
```python
def func_1(x):
    return x + -4


class Foo(object):
    def __init__(self):
        self.x = 2

    def bar_1(self):
        self.x += -1


func(10)
f = Foo()
f.bar()
```

## Challenge 2
Write a wrapper function to print the name, the value of the arguments and the return value of the wrapped function. 
Then read a python file, parse it to AST and add this wrapper dynamically to all functions.  Then run the modified ast. 

### Example
input2.py (input)
```python
def get100():
    return 100

def func1(x, y):
    return get100() + x + y + 1 

func1(4, 6) 
```
Program output
```
get100: () -> 100
func1: (4,6) -> 111 
```
