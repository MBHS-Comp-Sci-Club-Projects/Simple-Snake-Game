# snake.py

import random
from tkinter import *
from settings import *

def create_snake(canvas):
    return [[100, 100]], [canvas.create_rectangle(100, 100, 120, 120, fill=SNAKE_COLOR)]

def create_food(canvas):
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    canvas.delete("food")
    canvas.create_oval(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=FOOD_COLOR, tag="food")
    return [x, y]
