import tkinter as tk

def change(*args):
	print(var.get())

root = tk.Tk()

OPTIONS = [

"Samsung",
"Tencent",
"BMW",

]
var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w", change)

dropDownMenu = tk.OptionMenu(root, var, OPTIONS[0], OPTIONS[1], OPTIONS[2])
dropDownMenu.pack()

root.mainloop()