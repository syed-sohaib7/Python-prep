print("Hello Python's World")
print('Hello Python\'s World')

s = "My name is\nazh"
s  # prints without exc sequence \n
print(s)  # witb \n
print(r"My name is\n azh")  # raw string

print(4*'uni' + 'con')  # repeated with * and concatinated with +

prefix = 'Py'
print(prefix + 'thon')

# Indexing of string

word = "Python"
print(word[0])
print(word[4])
print(word[-1])

# Slicing of string

print(word[0:3])
print(word[0:6])
print(word[:2])

s = 'supercalifragilisticexpialidocious'
print(len(s))


a = 20
b = 23

print("The sum of {} + {} is {}".format(a, b, a+b))
