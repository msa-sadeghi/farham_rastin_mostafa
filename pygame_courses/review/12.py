from tkinter import *

window = Tk()
# window.title('Toplevel')

# Label(window, text='This is the main window').pack(pady=40)

# t1 = Toplevel(window)
# Label(t1, text='This is a child1 of window').pack(pady=40)

# t2 = Toplevel(window)
# Label(t2, text='This is a child2 of window').pack(pady=40)
# t2.transient(window)

# t3 = Toplevel(window, borderwidth=5, bg="blue")
# Label(t3, text='This is a child3 of window', bg="blue", fg="white").pack(pady=40)
# t3.geometry('200x70+250+150')
# t3.overrideredirect(1)

# FRAME
# for relief in (RAISED, SUNKEN, FLAT,RIDGE, GROOVE, SOLID):
#     f = Frame(window, borderwidth=2, relief=relief)
#     Label(f, text=relief, width=10).pack(side=LEFT)
#     f.pack(side=LEFT, padx=5, pady=5)

l1 = Label(window, text="Lorem ipsum odor amet, "
           "consectetuer adipiscing elit. Lobortis auctor sagittis quis sapien accumsan. Et gravida sagittis consectetur eu torquent quisque vehicula nulla. Taciti commodo augue quam suspendisse augue porttitor vitae. Accumsan tempor pretium eleifend quam semper netus aptent. Torquent auctor curae pulvinar litora ex sociosqu nisi amet? Pharetra tristique nibh aliquet laoreet sollicitudin morbi. Vel vulputate eros odio, condimentum justo taciti dui.", wraplength=300, justify="left")
l1.pack()

f1 = Frame(window)
Label(f1, text="It's not working, we need more", relief=RAISED).pack(side="left", padx=5)
f1.pack()


Button(window, text="تایید", state="disabled").pack(side="left")
Button(window, text="خروج", command=window.destroy).pack(side="right")

window.mainloop()
