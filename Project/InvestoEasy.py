import tkinter as tk

root = tk.Tk()
root.title("Invest-o-Easy")
root.configure(background="#F6F6F6")

#****************************input stock labels*******************************

def changeStock(*args):
	print(varName.get())

lablName = tk.Label(root, text = "Stock Name", font = 16, background = "#CAD5E2", foreground = "white")
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

#****************************Enter Dates*******************************

lablStart = tk.Label(root, text = "Start Date", font = 16, background = "#CAD5E2", foreground = "white", borderwidth = 2)
lablStart.grid(row = 1, column = 0, columnspan = 2, sticky = "NESW")


def on_entry_click_start(event):
    if entStart.get() == 'YY/MM/DD':
       entStart.delete(0, "end")
       entStart.insert(0, '')
       entStart.config(fg = 'black')
def on_focusout_start(event):
    if entStart.get() == '':
        entStart.insert(0, 'YY/MM/DD')
        entStart.config(fg = 'grey')

entStart = tk.Entry(root, bd = 3, background = "#FFFFFF")
entStart.insert(0, 'YY/MM/DD')
entStart.bind('<FocusIn>', on_entry_click_start)
entStart.bind('<FocusOut>', on_focusout_start)
entStart.config(fg = 'grey')
entStart.grid(row = 1, column = 2, sticky = "NESW")

lablEnd = tk.Label(root, text = "End Date", font = 16, background = "#CAD5E2", foreground = "white", borderwidth = 2)
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

entEnd = tk.Entry(root, bd = 3, background = "#FFFFFF")
entEnd.insert(0, 'YY/MM/DD')
entEnd.bind('<FocusIn>', on_entry_click_end)
entEnd.bind('<FocusOut>', on_focusout_end)
entEnd.config(fg = 'grey')
entEnd.grid(row = 1, column = 5, sticky = "NESW")

#****************************Input Functions******************************

def changeFunc(*args):
	print(varFunc.get())

lablFunc = tk.Label(root, text = "Functions", font = 16, background = "#CAD5E2", foreground = "white")
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

#****************************Accessibility Options******************************

def runColour(*args):
	print("running colour contrast")

btnColour = tk.Button(root, text="Colour Contrast", command = runColour, background = "white")
btnColour.grid(row = 3, column = 5, pady = 10)

def runFont(*args):
	print("running enlarged fonts")

btnFont = tk.Button(root, text="Enlarged Fonts", command = runColour)
btnFont.grid(row = 4, column = 5)

#****************************Execute Program******************************

def runExe(*args):
	print("running program")

btnExec = tk.Button(root, text="Run", command = runExe)
btnExec.grid(row = 5, column = 1, columnspan = 5)

#****************************Output Textbox******************************

textbox = tk.Text(root, height = 10, width = 50, borderwidth = 3, relief = tk.GROOVE)

textbox.insert(tk.INSERT,"Textbox \n")
#textbox.insert(1.4, " ")
textbox.insert(tk.INSERT, "Demo")
textbox.config(state = "disabled")
textbox.grid(row = 6, column = 1, columnspan = 5)

root.mainloop()