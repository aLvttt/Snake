import tkinter as tk
from tkinter.messagebox import OK, ERROR, showinfo


def start_game():

    global check_start
    
    if not check_start:
        check_start = True
        start_button.config(state="disabled")
        update_position()


def update_position():

    global check_start

    coords = canvas.coords(snakehead)

    if movement_mark == "up" and coords[1] > 0:
        canvas.move(snakehead, 0, -10)
        root.after(100, update_position)

    elif movement_mark == "down" and coords[3] < 550:
        canvas.move(snakehead, 0, 10)
        root.after(100, update_position)

    elif movement_mark == "right" and coords[2] < 550:
        canvas.move(snakehead, 10, 0)
        root.after(100, update_position)

    elif movement_mark == "left" and coords[0] > 0:
        canvas.move(snakehead, -10, 0)
        root.after(100, update_position)

    else:
        canvas.move(snakehead, 0, 0)
        check_start = False
        start_button.config(state="active")
        canvas.delete("snake")
        loose()


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
        

def spawn_snake():

    global snakehead

    snakehead = canvas.create_rectangle(260, 260, 280, 280, fill="#006400", outline="black", tags="snake")


def loose():
    showinfo(title="Упс...", message="Вы проиграли....", detail="Нажмите 'Ok' чтобы закрыть окно.", icon=ERROR, default=OK)
    spawn_snake()
        

# инициализация
root = tk.Tk()
root.title("Snake the game")
root.geometry("600x600")
root.iconbitmap(default="favicon.ico")
root.resizable(False, False)

main_menu = tk.Menu()


menu_info = tk.Menu(tearoff=0)
menu_info.add_command(label="About")
menu_info.add_command(label="Mode")

menu_info.add_separator()
menu_info.add_command(label="Exit")

main_menu.add_cascade(label="Menu", menu=menu_info)

root.config(menu=main_menu)

check_start = False

start_button = tk.Button(text="Start", command=start_game)
start_button.pack()

# инициализация canvas
canvas = tk.Canvas(bg="black", width=550, height=550)
canvas.pack(anchor="center", expand=1)

snakehead = canvas.create_rectangle(260, 260, 280, 280, fill="#006400", outline="black", tags="snake")

movement_info = tk.Label(text="Use the arrows for control the snake")
movement_info.pack()

# управление
root.bind("<Up>", movement)
root.bind("<Down>", movement)
root.bind("<Right>", movement)
root.bind("<Left>", movement)
movement_mark = "right"

root.mainloop()
