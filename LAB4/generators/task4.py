def square(a, b):
    for i in range(a, b):
        yield i ** 2

a = int(input("Enter the a: "))
b = int(input("Print the b: "))

for x in square(a, b):
    print(x, end= ", ")