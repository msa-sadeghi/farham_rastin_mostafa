# i = 1
# while i <= 5:
#     print(i)
#     i += 1

def add(a):
    s = 0
    for number in a:
        s += number
    return s
print(add([1,2,3,4,5,6,7,8,9,10]))
        
def my_func_1():
    for i in range(101, 1000, 2):
        print(i)
        
my_func_1()

def my_func_2(number):
    if number % 4 == 0:
        return "yes"
    return"no"
print(my_func_2(14))



def my_func_3():
    c= 0
    while True:
        n = int(input("enter a number:> "))
        if n < 0:
            break
        c += 1
    return c

print(my_func_3())