from tkinter import *

def login(username, password):
    f = open("info.txt")
    print(username, password)
    username2 = f.readline().strip()
    password2 = f.readline().strip()
    print(username2, password2)
    if username == username2 and password == password2:
        print("ok")
    
    else:
        print("not ok")
        window.destroy()

window = Tk()
window.geometry("300x200")
window.resizable(False, False)
# Label(window, text="نام کاربری").place(x = 210, y= 10)

# name = Entry(window, width=15)
# name.place(x = 100, y= 10)

main_frame = Frame(window)
main_frame.pack(pady=10)
Label(main_frame, text="نام کاربری", width=15).pack(side="right", anchor="e")
name = Entry(main_frame, width=15)
name.pack(side="right")
main_frame = Frame(window)
main_frame.pack(pady=10)
Label(main_frame, text="پسورد", width=15).pack(side="right", anchor="e")
password = Entry(main_frame, width=15)
password.pack(side="right")


submit_button = Button(window, text="ورود", command=lambda :login(name.get(), password.get()))
submit_button.pack()

window.mainloop()