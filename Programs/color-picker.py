import tkinter as tk
from tkinter import colorchooser

def _from_rgb(rgb):
    # Translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb  

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
inv_color = _from_rgb((int(255-color[0][0]),int(255-color[0][1]),int(255-color[0][2])))
print(color[0])

label.config(fg=inv_color, bg=color[1])
root.configure(bg=color[1])

label = tk.Label(root,
                text="Hex code of color you picked "+color[1],
                fg=inv_color,
                bg=color[1],
                height=5,
                font=("Courier", 20))
label.pack()
tk.mainloop()
