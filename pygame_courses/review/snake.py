from tkinter import *
from random import randint
class Snake:
    def __init__(self) -> None:
        self.body_count = 2
        self.coordinates =[]
        self.squares = []
        for i in range(self.body_count):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            snake_id = canvas.create_rectangle(x,y, x + SNAKE_BODY_SIZE,\
                y + SNAKE_BODY_SIZE, fill="orange", tag = "snake") 
            self.squares.append(snake_id)
            

class Food:
    def __init__(self) -> None:
        x = randint(0, window_width//SNAKE_BODY_SIZE - 1) * 50
        y = randint(0, window_height//SNAKE_BODY_SIZE - 1) * 50
        self.coordinate = [x,y]
        canvas.create_oval(x,y, x + SNAKE_BODY_SIZE,\
            y + SNAKE_BODY_SIZE, fill="green", tag="food")



WIDTH = 700
HEIGHT = 600
score = 0
SNAKE_BODY_SIZE = 50
window = Tk()

Label(window, text=f"Score:{score}", font=("arial", 22)).pack()
canvas = Canvas(window, bg="black", width=WIDTH, height=HEIGHT)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
x = window.winfo_screenwidth()//2 - window_width//2
y = window.winfo_screenheight()//2 - window_height//2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


snake = Snake()
food = Food()

window.mainloop()