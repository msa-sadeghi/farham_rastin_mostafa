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
direction = "down"

def change_direction(new_dir):
    global direction
    if new_dir == "down":
        if direction != "up":
            direction = "down"
    elif new_dir == "up":
        if direction != "down":
            direction = "up"
    elif new_dir == "left":
        if direction != "right":
            direction = "left"
    elif new_dir == "right":
        if direction != "left":
            direction = "right"

def next_step(snake, food):
    global score
    x,y = snake.coordinates[0]
    if direction == "up":
        y -= SNAKE_BODY_SIZE
    elif direction == "down":
        y += SNAKE_BODY_SIZE
    elif direction == "left":
        x -= SNAKE_BODY_SIZE
    elif direction == "right":
        x += SNAKE_BODY_SIZE
        
    snake.coordinates.insert(0,[x,y])
    snake_id = canvas.create_rectangle(x,y, x + SNAKE_BODY_SIZE,\
                y + SNAKE_BODY_SIZE, fill="orange", tag = "snake") 
    snake.squares.insert(0,snake_id)
    if x == food.coordinate[0] and y == food.coordinate[1]:
        score += 1
        score_label.config(text=f"Score:{score}")
        canvas.delete('food')
        food.coordinate = []
        food = Food()
    else:
        canvas.delete(snake.squares[-1])
        del snake.coordinates[-1]
        del snake.squares[-1]
    if if_game_over()    :
        game_over()
    else:
        window.after(200, next_step, snake, food)


def if_game_over():
    x,y = snake.coordinates[0]
    if x < 0 or x > WIDTH or y <0 or y > HEIGHT:
        return True
    
    return False
        

def game_over():
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width()//2, canvas.winfo_height()//2,fill="red",font=("arial", 32), text="Game Over")


window = Tk()
score_label = Label(window, text=f"Score:{score}", font=("arial", 22))
score_label.pack()
canvas = Canvas(window, bg="black", width=WIDTH, height=HEIGHT)
canvas.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = window.winfo_screenwidth()//2 - window_width//2
y = window.winfo_screenheight()//2 - window_height//2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind("<Up>", lambda e:change_direction("up"))
window.bind("<Down>", lambda e:change_direction("down"))
window.bind("<Left>", lambda e:change_direction("left"))
window.bind("<Right>", lambda e:change_direction("right"))

snake = Snake()
food = Food()
next_step(snake, food)
window.mainloop()

# TODO
# if snake head collides with snake bodies then we should game over
# check if new food position collides with any parts of snake bodies then ou must generate another 