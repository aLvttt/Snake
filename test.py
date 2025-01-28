from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
def click(): 
    result = askyesno(title="Подтвержение операции", message="Подтвердить операцию?")
    if result: showinfo("Результат", "Операция подтверждена")
    else: showinfo("Результат", "Операция отменена")
 
ttk.Button(text="Click", command=click).pack(anchor="center", expand=1)
 
root.mainloop()