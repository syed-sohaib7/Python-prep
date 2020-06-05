
# Finally - The finally block will always be executed, no matter if the try block raises an error or not

#x = 5
try:
    x > 3
except:
    print("Something went wrong...")
else:
    print("Nothing went wrong...")
finally:
    print("The try..except block is finished...")

# Global - Declare a global variable inside a function, and use it outside the function after calling


def funct():
    global x
    x = 'Hello'


funct()

print(x)

# lambda - used to create small anonymous functions containing just one expression but can have any no of arguments

# a= lambda x: x + 10


def a(x): return x + 10


print(a(4))

# pass - nothing happens but avoid getting error, used as a placeholder

a = 33
b = 200

if b > a:
    pass
