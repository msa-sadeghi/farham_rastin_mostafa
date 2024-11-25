# numbers = []

# i = 0
# while i < 5:
#     x = float(input("enter a number: "))
#     numbers.append(x)
#     i += 1
    
# print(sum(numbers))

# my_list = [1,3,3,4,"ss","ss", 123, "asdasd"]

# number_count = 0
# string_count = 0

# for item in my_list:
#     if type(item) == str:
#         string_count += 1
#     elif type(item) == int or type(item) == float:
#         number_count += 1
# print(f"we have {number_count} numbers and {string_count} string in our list")


# def is_prime_number(n):
#     res = True
#     if n <= 1:
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             res = False
#     return res
# for i in range(100):
#     print(f"{i} => {is_prime_number(i)}")



# import turtle
# sc = turtle.Screen()
# t = turtle.Turtle()
# t.shape("turtle")
# t.shapesize(3)
# t.color("orange")

# def draw_shape(x,y):
#     sides = int(sc.numinput("side", "enter sides number:"))
#     color = sc.textinput("color", "enter the color name")
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.color(color)
#     t.begin_fill()
#     for _ in range(sides):
#         t.forward(80)
#         t.left(360/sides)
#     t.end_fill()    
# sc.onclick(draw_shape)
# def f():
#     for i in range(5):
#         t.write(i)
#         t.fd(50)
# t.shape("arrow")
# f()
# t.stamp()
# t.home()
# t.left(90)
# f()

# turtle.done()
class Person:
    def __init__(self, n):
        self.name = n
    def eat(self):
        print(f"{self.name} is eating")
class Student(Person):
    def __init__(self, stu_code, a = "no name"):
        super().__init__(a)
        self.student_code = stu_code
    def learn(self):
        print(f"{self.name} with {self.student_code} is learnign")

class Teacher(Person):
    def __init__(self, teacher_code, n ):
        super().__init__(n)
        self.teacher_code = teacher_code
    
    def teach(self):
        print(f"{self.name} with {self.teacher_code} is teaching")
    
s1 = Student(1234, "sn1" )
s2 = Student(5678)
s1.eat()
s1.learn()
t1 = Teacher(123, "msa")
t1.eat()
t1.teach()