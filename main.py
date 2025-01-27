import tkinter as tk

def start_game():
    global check_start
    
    if not check_start:
        check_start = True
        start_button.config(state="disabled")
        update_position()

def update_position():
    if movement_mark == "up":
        canvas.move(snakehead, 0, -10)

    elif movement_mark == "down":
        canvas.move(snakehead, 0, 10)

    elif movement_mark == "right":
        canvas.move(snakehead, 10, 0)

    elif movement_mark == "left":
        canvas.move(snakehead, -10, 0)
    
    root.after(100, update_position)

def movement(event):
    global movement_mark

    if event.keysym == "Up":
        if movement_mark != "down":
            movement_mark = "up"

    elif event.keysym == "Down":
        if movement_mark != "up":
            movement_mark = "down"
        
    elif event.keysym == "Right":
        if movement_mark != "left":
            movement_mark = "right"
        
    elif event.keysym == "Left":
        if movement_mark != "right":
            movement_mark = "left"
        

# инициализация 
root = tk.Tk()
root.title("Snake the game")
root.geometry("600x600")
root.iconbitmap(default="favicon.ico")
root.resizable(False, False)

check_start = False
start_button = tk.Button(text="Start", command=start_game)
start_button.pack()

# инициализация canvas
canvas = tk.Canvas(bg="black", width=550, height=550)
canvas.pack(anchor="center", expand=1)

movement_info = tk.Label(text="Use the arrows for control the snake")
movement_info.pack()

snakehead = canvas.create_rectangle(260, 260, 280, 280, fill="#006400", outline="black", tags="snake")

# управление
root.bind("<Up>", movement)
root.bind("<Down>", movement)
root.bind("<Right>", movement)
root.bind("<Left>", movement)
movement_mark = "right"

root.mainloop()
