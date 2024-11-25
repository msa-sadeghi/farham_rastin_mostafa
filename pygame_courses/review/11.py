# try:
#     x = int(input("enter a number:> "))
#     y = int(input("enter a number:> "))
#     print(x/y)
#     print(z)
# except ValueError:
#     print("Value must be number!!!")
# except ZeroDivisionError:
#     print("second number can not be zero")
# except NameError:
#     print("variable not defined")
try:  
    f = open("students.txt", "w")
except (FileNotFoundError, ValueError):
    print("error")
else:
    print("no error")
finally:
    print("finally")
    f.close()