# names = [
#     ['hira', 'mehrad'],
#     ['mostafa', 'farham', 'artin']
# ]
# x = 0
# for i in range(len(names)):
#     for j in range(len(names[i])):
#         x += len(names[i][j])
# print(x)
        
        
# lst = [
#     [1, 1],
#     [2, 3, 4]
# ]

# x = 0
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         x += lst[i][j]
# print(x)
    
with open("words.txt", "r") as file:
    all_words = file.read().split("\n")
    
print(all_words)
# تعداد کاکترهای موچود در لیست بلا را نمایش دهید
# تعداد کلمات را نمایش دهید
# لیستی بسازید که طول هر یک از کلمات را ذخیره کند
# برنامه ای بنویسید که یک کلمه را از کاربر بگیرد و
# از لیست بالا یعنی لیست کلمات تمامی کلماتی که از حروف یکسان با لمه وارد شده ساخته شدند را نمایش دهد
# stop   ->   pots, post, .....