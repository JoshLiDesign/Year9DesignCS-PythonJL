import tkinter as tk

root = tk.Tk()
root.title("Invest-o-Easy")
root.configure(background="#90AFC5")

#****************************Stock Index*******************************

def changeStock(*args):
	print(varName.get())

lablName = tk.Label(root, text = "Stock Name", background = "#336B87", foreground = "white", height = 2)
lablName.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

stockNames = [
"Select",
"Apple Inc.",
"Coca-Cola Company",
"Facebook, Inc.",
"Monster Beverage",
]

varName = tk.StringVar(root)
varName.set(stockNames[0])
varName.trace("w", changeStock)

dropDownMenustocks = tk.OptionMenu(root, varName, stockNames[0], stockNames[1], stockNames[2], stockNames[3])
dropDownMenustocks.grid(row = 0, column = 2, columnspan = 2)

#*****************************Dates*******************************

lablStart = tk.Label(root, text = "Start Date", background = "#336B87", foreground = "white", height = 2)
lablStart.grid(row = 1, column = 0, columnspan = 2, sticky = "NESW", pady = 1)


def on_entry_click_start(event):
    if entStart.get() == 'YY/MM/DD':
       entStart.delete(0, "end")
       entStart.insert(0, '')
       entStart.config(fg = 'black')
def on_focusout_start(event):
    if entStart.get() == '':
        entStart.insert(0, 'YY/MM/DD')
        entStart.config(fg = 'grey')

entStart = tk.Entry(root, bd = 3)
entStart.insert(0, 'YY/MM/DD')
entStart.bind('<FocusIn>', on_entry_click_start)
entStart.bind('<FocusOut>', on_focusout_start)
entStart.config(fg = 'grey')
entStart.grid(row = 1, column = 2, sticky = "NESW", padx = 2)

lablEnd = tk.Label(root, text = "End Date",  background = "#336B87", foreground = "white", height = 2)
lablEnd.grid(row = 1, column = 3, columnspan = 2, sticky = "NESW")

def on_entry_click_end(event):
    if entEnd.get() == 'YY/MM/DD':
       entEnd.delete(0, "end")
       entEnd.insert(0, '')
       entEnd.config(fg = 'black')
def on_focusout_end(event):
    if entEnd.get() == '':
        entEnd.insert(0, 'YY/MM/DD')
        entEnd.config(fg = 'grey')

entEnd = tk.Entry(root, bd = 3)
entEnd.insert(0, 'YY/MM/DD')
entEnd.bind('<FocusIn>', on_entry_click_end)
entEnd.bind('<FocusOut>', on_focusout_end)
entEnd.config(fg = 'grey')
entEnd.grid(row = 1, column = 5, sticky = "NESW")

#*****************************Functions******************************

def changeFunc(*args):
	print(varFunc.get())

lablFunc = tk.Label(root, text = "Functions", background = "#336B87", foreground = "white", height = 2)
lablFunc.grid(row = 2, column = 0, columnspan = 2, sticky = "NESW")

stockFunc = [
"Select",
"Find highest opening/closing rate",
"Find lowest opening/closing rate",
"Find fluctuation",
]

varFunc = tk.StringVar(root)
varFunc.set(stockFunc[0])
varFunc.trace("w", changeFunc)

dropDownMenufunc = tk.OptionMenu(root, varFunc, stockFunc[0], stockFunc[1], stockFunc[2], stockFunc[3])
dropDownMenufunc.grid(row = 2, column = 2, columnspan = 2)

#****************************Accessibility Options*****************************

def runColour(*args):
	print("running colour contrast")

lablColour = tk.Label(root, text = "Colour Contrast", width = 12, background = "#363A4C", relief = tk.GROOVE, foreground = "white", borderwidth = 1)
lablColour.grid(row = 3, column = 5, sticky = "NSE")
lablColour.bind("<Button-1>", runColour)

def runFont(*args):
	print("running enlarged fonts")

lablColour = tk.Label(root, text = "Enlarged  Fonts", width = 12, background = "#363A4C", relief = tk.GROOVE, foreground = "white", borderwidth = 1)
lablColour.grid(row = 4, column = 5, sticky = "NSE")
lablColour.bind("<Button-1>", runFont)

#*****************************Execution Catalyst******************************

def runExe(*args):
	print("running program")

root.bind('<Return>', runExe)

lablExec = tk.Label(root, text = "run", font = 40, background = "#363A4C", width = 8, foreground = "white", borderwidth = 2)
lablExec.grid(row = 5, column = 3, sticky = "NESW", pady = 2)
lablExec.bind("<Button-1>", runExe)

#********************************Output Box*************************************

textbox = tk.Text(root, height = 10, width = 50, borderwidth = 3, relief = tk.GROOVE)

textbox.insert(tk.INSERT,"Textbox \n")
#textbox.insert(1.4, " ")
textbox.insert(tk.INSERT, "Demo")
textbox.config(state = "disabled")
textbox.grid(row = 6, column = 1, columnspan = 5)

root.mainloop()