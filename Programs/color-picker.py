import tkinter as tk
from tkinter import colorchooser

root=tk.Tk()
color=colorchooser.askcolor()

print(color[1])

label = tk.Label(root,
                text="You picked "+color[1],
                fg="white",
                bg="black",
                width=30,
                height=10,
                font=("Courier", 30))
label.pack()
tk.mainloop()
