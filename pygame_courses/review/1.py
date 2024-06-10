# print((5).bit_length())
# print((12).bit_length())

# x = " 1 "
# print(float(x))

# name = input("enter a name: ")
# print(name[::-1])
all_words = []
with open("words.txt", "r") as f:
    all_words = f.read().split("\n")
print(all_words[:10])
all_words = []
with open("words.txt", "r") as f:
    all_words = f.readlines()
w = []
for word in all_words:
    w.append(word[:-1])
    
print(w[:10])

# numbers = input("enter some numbers: ")
# numbers = numbers.split(",")
# nums = []
# for number in numbers:
#     nums.append(int(number))
# print(nums)
# print(numbers)
    