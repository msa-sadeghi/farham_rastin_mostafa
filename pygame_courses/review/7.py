# x = (1,2)
# a = int(input("enter a number: "))
# x += (a,)
# print(x)

# names = ()
# for i in range(5):
#     n = input("enter a name:> ")
#     names += (n,)
    
# print(names[::2])

# name = input("enter a name:> ")
# print(name[::2])


# x = [1,3,2,66,4]
# maximum = x[0]
# for number in x:
#     if number > maximum:
#         maximum = number
        
# print(f"max is {maximum}")


student = {
    "name":"sara",
    "age" : 22,
    "country" : "IR",
    "nc" : "02500000",
}

print(f"student's name is {student['name']}")
print(f"student's age is {student['age']}")
print(f"student's country is {student.get('country')}")
print(f"student's country is {student.get('info')}")
student["weight"] = "176kg"
student.update({"height": 177, "blood_type":"A+"})
print(student)