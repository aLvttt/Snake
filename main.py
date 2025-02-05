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
        self.point_counter = 0
        self.best_score = 0
        
        self.start_info = tk.Label(self, text='Press "Enter" for start the game :)', bg="#bfd2c4", fg="black")
        self.start_info.pack(pady=2)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(anchor="center", expand=1)

        self.point_info = tk.Label(self, text=self.point_counter, bg="#bfd2c4", fg="black")
        self.point_info.pack(pady=2)

        self.best_score_info = tk.Label(self, text=f"Your best score: {self.best_score}", bg="#bfd2c4", fg="black")
        self.best_score_info.pack(pady=2)

        self.movement_info = tk.Label(self, text="Use the arrows for control the snake", bg="#bfd2c4", fg="red")
        self.movement_info.pack(pady=2)


        self.field = Field(self.canvas)
        self.field.spawn_field()

        self.snake = Snake(self.field, self.canvas)
        self.snake.spawn_snake()
        print("Snake:", self.canvas.coords(self.snake.snakehead))

        self.food = Food(self.field, self.canvas, self.snake)

        self.canvas.bind_all("<KeyPress>", self.movement)
        self.canvas.bind_all("<Return>", self.keyboard_start_game)
        # Create a menu widget for game controls
        menu_bar = tk.Menu(self.master)
        game_menu = tk.Menu(menu_bar, tearoff=0)
        game_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="Menu", menu=game_menu)
        self.master.config(menu=menu_bar)


    def keyboard_start_game(self, event):
        self.start_game()


    def start_game(self):
        if not self.check_start:
            self.check_start = True
            self.update_position()
            self.food.spawn_food()


    def loose_game(self):
        self.canvas.move(self.snake.snakehead, 0, 0)
        self.check_start = False
        self.canvas.delete("snake")

        showinfo(
            title="Oops...",
            message=f"You lose. Your score: {self.point_counter}",
            detail="Press 'OK' to restart",
            icon=ERROR,
            default=OK
        )
        self.snake.spawn_snake()
        self.canvas.delete("food")

        if self.best_score < self.point_counter:
            self.best_score = self.point_counter
            self.best_score_info.config(text=f"Your best score: {self.best_score}")

        self.point_counter = 0
        self.point_info.config(text=self.point_counter)


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
        
        if self.food.food:
            food_coords = self.canvas.coords(self.food.food)
            print("Food coords:", food_coords)

        print("Snake head coords:", coords)

        for i in range(len(self.snake.segments) -1, 0, -1):
            old_coords = self.canvas.coords(self.snake.segments[i - 1])
            self.canvas.coords(self.snake.segments[i], *old_coords)


        if self.movement_dir == "up" and coords[1] >= self.snake.snake_size:
            self.canvas.move(self.snake.snakehead, 0, -self.snake.snake_size)

        elif self.movement_dir == "down" and coords[3] < 500:
            self.canvas.move(self.snake.snakehead, 0, self.snake.snake_size)

        elif self.movement_dir == "right" and coords[2] < 500:
            self.canvas.move(self.snake.snakehead, self.snake.snake_size, 0)


        elif self.movement_dir == "left" and coords[0] >= self.snake.snake_size:
            self.canvas.move(self.snake.snakehead, -self.snake.snake_size, 0)

        else:
            self.loose_game()

        if self.check_snake_body_collision():
            self.loose_game()
            return


        if self.check_start:
            self.canvas.after(150, self.update_position)
            self.eating()


    def eating(self):
        if self.food.food and self.snake.snakehead:
            if self.canvas.coords(self.snake.snakehead) == self.canvas.coords(self.food.food):
                self.canvas.delete("food")
                self.food.spawn_food()
                self.add_segment()
                self.point_counter += 1
                self.point_info.config(text=self.point_counter)


    def add_segment(self):
        last_segment = self.snake.segments[-1]
        last_coords = self.canvas.coords(last_segment)

        new_segment = self.canvas.create_rectangle(*last_coords, fill="#006400", outline="black", tags="snake")
        self.snake.segments.append(new_segment)

        return last_segment, last_coords
    

    def check_snake_body_collision(self):
        snakehead_coords = self.canvas.coords(self.snake.snakehead)

        for segment in self.snake.segments[1:]:
            if self.canvas.coords(segment) == snakehead_coords:
                return True
            
        return False


    def restart_game(self):
        self.start_game()


root = tk.Tk()
root.title("Snake")
root.geometry("600x600+650+200")
root.iconbitmap(default="favicon.ico")
root.resizable(False, False)
root.config(bg="#bfd2c4")

myapp = App(master=root)
myapp.mainloop()
