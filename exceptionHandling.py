

x = 3
try:
    x / 0
except ZeroDivisionError:
    print("Cannot divide by Zero.")
except:
    print("Some other error occurred.")
else:
    print("No error in expression.")
finally:
    print("This will always be an error.")
