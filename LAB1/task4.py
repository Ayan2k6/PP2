# Python Variables
x = 5
y = 154
y = "Max" # y is now of type str
print(x)
print(y) 

a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0
print(a)
print(b)
print(c)

n = 5
m = "John"
print(type(n))   # will be <class 'int'>
print(type(m))   # will be <class 'str'>

x = 4
X = "Sally"
#A will not overwrite a
print(x)
print(X)

# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Assign Multiple Values
q, w, e = "Orange", "Banana", "Cherry"
print(q)
print(w)
print(e)

r = t = u = "Orange"
print(r)
print(t)
print(u)

fruits = ["apple", "banana", "cherry"]
i, o, p = fruits
print(i)
print(o)
print(p)

# Output Variables
qq = "Python is awesome"
print(qq)

s = "Python"
d = "is"
f = "awesome"
print(s, d, f)

g = "Python "
h = "is "
j = "awesome"
print(g + h + j)

k = 5
l = 10
print(k + l)

# Global Variables
v = "awesome"
def myfunc():
    v = "fantastic"
    print("Puthon is " + v)
myfunc()
print("Puthon is " + v)

ww = "awesome"
def myfunc():
  global ww
  ww = "fantastic"

myfunc()
print("Python is " + ww)
