# class Dog:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender


#     def eat(self):
#         print(f"{self.name} is eating")

#     def bark(self):
#         print(f"{self.name} is barking")


# class Beagle(Dog):
#     def __init__(self, name, age, gender, gun_shy):
#         super().__init__(name, age, gender)
#         self.gun_shy = gun_shy
#     def hunt(self):
#         print(f"{self.name} is hunting")

# b1 = Beagle("jessi", 12, "girl", True)
# b1.eat()
# b1.bark()
# b1.hunt()

"""
Person
        name
        age
        weight
        height
        ...

        eat()
        walk()
        talk()
        ...
Student
        child of Person
            class_number
            ...
        exam() 
        ...       

Teacher
        child class Person
            grade
            ... 
        teaching()
        ...

"""