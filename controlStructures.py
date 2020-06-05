# While loop
a = 0
while a < 10:
    print("{} is the new value.".format(a))
    a += 1

# If else ladder
x = 10
y = 20
z = 44 or int(input("Enter a number: "))
if x > y and x > z:
    print("{} is greatee than {} and {}".format(x, y, z))
elif y > z and y > x:
    print("{} is greatee than {} and {}".format(y, x, z))
else:
    print("{} is greatee than {} and {}".format(z, x, y))

# for statement
for i in range(10):
    print(i, end='')
print()

a = [1, 2, 3, 4, 6, "one", "two"]
for i in a:
    print(i, end='')
print()


print(sum(range(1, 55)))
print(list(range(2, 10, 2)))

# To loop over two or more sequences at the same time , use zip()

list_a = ['abc', 'efg', 'hij']
list_b = ['xyz', 'ijkl', 'zxcv']

for a, b in zip(list_a, list_b):
    print("This is {} and {}".format(a, b))
