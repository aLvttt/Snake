import tkinter as tk
from tkinter.messagebox import showinfo, ERROR, OK
from core import Snake, Food, Field


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg="#bfd2c4")
        self.pack(fill="both", expand=True)

        self.snake = None
        self.food = None
        self.check_start = False
        self.movement_dir = "right"
        
        self.start_button = tk.Button(self, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(anchor="center", expand=1)

        self.movement_info = tk.Label(self, text="Use the arrows for control the snake", bg="#bfd2c4", fg="black")
        self.movement_info.pack(pady=20)

        self.field = Field(self.canvas)
        self.field.spawn_field()

        self.snake = Snake(self.field, self.canvas)
        self.snake.spawn_snake()

        self.food = Food(self.field, self.canvas)

        self.canvas.bind_all("<KeyPress>", self.movement)


    def start_game(self):
        if not self.check_start:
            self.check_start = True
            self.start_button.config(state="disabled")
            self.update_position()
            self.food.spawn_food()


    def loose_game(self):
        showinfo(title="Oops...", message="You loose.", detail="Press 'OK' to restart", icon=ERROR, default=OK)
        self.snake.spawn_snake()


    def movement(self, event):
        if event.keysym == "Up" and self.movement_dir != "down":
            self.movement_dir = "up"

        elif event.keysym == "Down" and self.movement_dir != "up":
            self.movement_dir = "down"
            
        elif event.keysym == "Right" and self.movement_dir != "left":
            self.movement_dir = "right"
            
        elif event.keysym == "Left" and self.movement_dir != "right":
            self.movement_dir = "left"


    def update_position(self):
        coords = self.canvas.coords(self.snake.snakehead)

        if self.movement_dir == "up" and coords[1] > self.snake.snake_size:
            self.canvas.move(self.snake.snakehead, 0, -self.snake.snake_size)

        elif self.movement_dir == "down" and coords[3] < 500:
            self.canvas.move(self.snake.snakehead, 0, self.snake.snake_size)

        elif self.movement_dir == "right" and coords[2] < 500:
            self.canvas.move(self.snake.snakehead, self.snake.snake_size, 0)


        elif self.movement_dir == "left" and coords[0] > self.snake.snake_size:
            self.canvas.move(self.snake.snakehead, -self.snake.snake_size, 0)

        else:
            self.canvas.move(self.snake.snakehead, 0, 0)
            self.check_start = False
            self.start_button.config(state="active")
            self.canvas.delete("snake")
            self.loose_game()

        if self.check_start:
            self.canvas.after(100, self.update_position)



root = tk.Tk()
root.title("Snake")
root.geometry("600x600")
root.iconbitmap(default="favicon.ico")
root.resizable(False, False)
root.config(bg="#bfd2c4")

myapp = App(master=root)
myapp.mainloop()
