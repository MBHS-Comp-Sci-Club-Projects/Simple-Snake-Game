# main.py

from tkinter import *
from settings import *
from snake import create_snake, create_food

# this runs every turn to move the snake
def move():
    global snake_coords, snake_squares, food_coord, direction, score

    # get current head position
    x, y = snake_coords[0]

    # move head based on direction
    if direction == "Up": y -= CELL_SIZE
    elif direction == "Down": y += CELL_SIZE
    elif direction == "Left": x -= CELL_SIZE
    elif direction == "Right": x += CELL_SIZE

    new_head = [x, y]

    # check if snake hits wall or itself
    if (
        x < 0 or x >= WIDTH or
        y < 0 or y >= HEIGHT or
        new_head in snake_coords
    ):
        canvas.create_text(WIDTH//2, HEIGHT//2, text="game over", fill="red", font=("Arial", 24))
        return

    # add new head to front of list
    snake_coords.insert(0, new_head)
    square = canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=SNAKE_COLOR)
    snake_squares.insert(0, square)

    # check if snake eats the food
    if new_head == food_coord:
        score += 1
        label.config(text=f"score: {score}")
        food_coord = create_food(canvas)
    else:
        # this is quite complicated, but the snake will always be alternating between adding one block in front
        # and one block in the back
        canvas.delete(snake_squares.pop())
        snake_coords.pop()

    # schedule next move
    window.after(SPEED, move)

# direction is updated when arrow keys are pressed
def change_dir(e):
    global direction
    key = e.keysym
    opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    if key in opposite and direction != opposite[key]:
        direction = key

# setting up the window
window = Tk()
window.title("snake")
window.resizable(False, False)

# creating a label at the top of the window which will be used to display current score
label = Label(window, text="score: 0", font=("Arial", 16))
label.pack()

# creating the canvas in the window
canvas = Canvas(window, bg=BG_COLOR, width=WIDTH, height=HEIGHT)
canvas.pack()

# what direction the snake will start in, and starting score which is zero
direction = "Right"
score = 0

# create the snake and the first food
snake_coords, snake_squares = create_snake(canvas)
food_coord = create_food(canvas)

# function that allows the program to recieve user input for the arrow keys
window.bind("<Key>", change_dir)

# start the game loop
move()

# keep window open
window.mainloop()
