import tkinter as tk
import subprocess
import threading

root = tk.Tk()
root.title("Invest-o-Easy")
root.configure(background = "#90AFC5")

#****************************Stock Labels*******************************

def changeStock(*args):
	print(varName.get())

lablName = tk.Label(root, text = "Stock Name", background = "#336B87", foreground = "white", height = 2)
lablName.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

stockNames = [
"Select",
"Apple Inc.",
"Coca-Cola Company",
"Facebook Inc.",
"Monster Beverage",
]

varName = tk.StringVar(root)
varName.set(stockNames[0])
varName.trace("w", changeStock)

dropDownMenustocks = tk.OptionMenu(root, varName, stockNames[0], stockNames[1], stockNames[2], stockNames[3])
dropDownMenustocks.grid(row = 0, column = 2, columnspan = 2)

#*****************************Date Extraction*******************************

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
"Compute Average Stock Price",
"Find Highest & Lowest Rate",
"Calculate Fluctuations",
]

varFunc = tk.StringVar(root)
varFunc.set(stockFunc[0])
varFunc.trace("w", changeFunc)

dropDownMenufunc = tk.OptionMenu(root, varFunc, stockFunc[0], stockFunc[1], stockFunc[2], stockFunc[3])
dropDownMenufunc.grid(row = 2, column = 2, columnspan = 2)

#****************************Accessibility Options*****************************

colourAt = 0;

def runColour(*args):
  global colourAt
  colourAt += 1;
  print("running colour contrast")
  if colourAt % 2 == 1:
    root.configure(background = "#E2755D")
    lablName.configure(background = "#A43820")
    lablStart.configure(background = "#A43820")
    lablEnd.configure(background = "#A43820")
    lablFunc.configure(background = "#A43820")
    lablColour.configure(background = "#46211A")
    lablSpeech.configure(background = "#46211A")
    lablExec.configure(background = "#46211A")
  else:
    root.configure(background = "#90AFC5")
    lablName.configure(background = "#336B87")
    lablStart.configure(background = "#336B87")
    lablEnd.configure(background = "#336B87")
    lablFunc.configure(background = "#336B87")
    lablColour.configure(background = "#363A4C")
    lablSpeech.configure(background = "#363A4C")
    lablExec.configure(background = "#363A4C")


lablColour = tk.Label(root, text = "Colour Contrast", width = 12, background = "#363A4C", relief = tk.GROOVE, foreground = "white", borderwidth = 1, height = 1)
lablColour.grid(row = 3, column = 5, sticky = "NSE")

lablColour.bind("<Button-1>", runColour)


def say(text):
  subprocess.call(['say', text])

print("The text-to-speech funtion is binded by pressing tab");

def runSpeechprep(*args):
  t = threading.Thread(target=runSpeech)
  t.start()

def runSpeech(*args):
  print("running text-to-speech")
  say("This program, Invest-o-Easy, carries out functions on pre-selected stocks by extracting the daily opening and closing market value for those stocks in a set range of days.")
  say("The creator thoroughly hopes that your gain interest and knowledge in investing by the end of your use of this program.")
  say("Here follows a text-to-speech instruction of all elements in this program")
  say("Select a stock label: Apple Inc, Coca-Cola Company and Facebook Inc")
  say("Select the start date and the end date in the format of YY, slash MM, slash DD")
  say("Select a desired function: compute the average price of stocks, find the highest and lowest rates or calculate fluctuations")
  say("Click on colour contrast for a different colour scheme")
  say("Press Run to execute this program")

root.bind('<Tab>', runSpeechprep)

lablSpeech = tk.Label(root, text = "Text-to-Speech", width = 12, background = "#363A4C", relief = tk.GROOVE, foreground = "white", borderwidth = 1, height = 1)
lablSpeech.grid(row = 4, column = 5, sticky = "NSE")
lablSpeech.bind("<Button-1>", runSpeechprep)

#*****************************Execution Catalyst******************************

def runExe(*args):
	print("running program")

root.bind('<Return>', runExe)

lablExec = tk.Label(root, text = "run", font = 40, background = "#363A4C", width = 8, foreground = "white", borderwidth = 2)
lablExec.grid(row = 5, column = 3, sticky = "NESW", pady = 2)
lablExec.bind("<Button-1>", runExe)

#*******************************Data Processing & Calculatino***********************************

temp = 

file = open("Apple.txt","r")

#********************************Output Box*************************************

textbox = tk.Text(root, height = 10, width = 50, borderwidth = 3, relief = tk.GROOVE)

textbox.insert(tk.INSERT,"Textbox \n")
#textbox.insert(1.4, " ")
textbox.insert(tk.INSERT, "Demo")
textbox.config(state = "disabled")
textbox.grid(row = 6, column = 1, columnspan = 5)

root.mainloop()