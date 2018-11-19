import tkinter as tk

def change(*args):
	print(varName.get())

root = tk.Tk()
root.title("Invest-o-Easy")

labelName = tk.Label(root, text = "Stock Name", font = 16)
labelName.grid(row = 0, column = 0, columnspan = 2)

stockNames = [
"Apple Inc.",
"Coca-Cola Company",
"Facebook, Inc.",
"Monster Beverage",
]

varName = tk.StringVar(root)
varName.set(stockNames[0])
varName.trace("w", change)

dropDownMenustocks = tk.OptionMenu(root, varName, stockNames[0], stockNames[1], stockNames[2], stockNames[3])
dropDownMenustocks.grid(row = 0, column = 2, columnspan = 2)

root.mainloop()