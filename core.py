import tkinter as tk
from random import randrange


class Field():
    def __init__(self, canvas):
        self.canvas = canvas

    def spawn_field(self):
        self.canvas.config(bg="#1b1c1d", width=500, height=500)
        self.params = [self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()]


class Snake():
    def __init__(self, field, canvas):
        self.canvas = canvas
        self.field = field
        self.snakehead = None
        self.snake_size = 20


    def spawn_snake(self):
        canvas_width = self.field.params[0]
        canvas_height = self.field.params[1]

        center_x = (canvas_width - self.snake_size) // 2
        center_y = (canvas_height - self.snake_size) // 2
        
        self.snakehead = self.canvas.create_rectangle(center_x, center_y, center_x + self.snake_size, center_y + self.snake_size, fill="#006400", outline="black", tags="snake")


class Food():
    def __init__(self, field, canvas):
        self.canvas = canvas
        self.field = field
        self.food = None
        self.food_size = 20


    def spawn_food(self):
        canvas_width = self.field.params[0]
        canvas_height = self.field.params[1]

        food_x = randrange(0, canvas_width, 20)
        food_y = randrange(0, canvas_height, 20)

        self.food = self.canvas.create_rectangle(food_x, food_y, food_x + self.food_size, food_y + self.food_size, fill="#B22222", outline="black")

    def delete_food(self):
        pass