import tkinter as tk
from tkinter import colorchooser

root=tk.Tk()
root.title("Color Picker")
root.configure(bg='black')
label = tk.Label(root,
                text="Pick the color",
                fg="white",
                bg="black",
                width=30,
                height=5,
                font=("Courier", 30))
label.pack()

color=colorchooser.askcolor()

print(color[1])

label = tk.Label(root,
                text="Hex code of color you picked "+color[1],
                fg="white",
                bg="black",
                height=5,
                font=("Courier", 20))
label.pack()
tk.mainloop()
