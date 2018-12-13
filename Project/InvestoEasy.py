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

dropDownMenustocks = tk.OptionMenu(root, varName, stockNames[0], stockNames[1], stockNames[2], stockNames[3], stockNames[4])
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

lablEnd = tk.Label(root, text = "End Date",  background = "#336B87", width = 9, foreground = "white", height = 2)
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
"Compute Average Stock Prices",
"Find Highest & Lowest Rates",
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

at = 0

def runSpeechprep(*args):
  t = threading.Thread(target=runSpeech)
  t.start()

def runSpeech(*args):
  global at
  if at == 0:
    at = 1
    print("running text-to-speech")
    lablSpeech.configure(state = "disabled")
    say("This program, Invest-o-Easy, carries out functions on pre-selected stocks by extracting the daily opening and closing market value for those stocks in a set range of days.")
    say("The creator thoroughly hopes that your gain interest and knowledge in investing by the end of your use of this program.")
    say("Here follows a text-to-speech instruction of all elements in this program")
    say("Select a stock label: Apple Inc, Coca-Cola Company and Facebook Inc")
    say("Select the start date and the end date in the format of YY, slash MM, slash DD")
    say("Select a desired function: compute the average price of stocks, find the highest and lowest rates or calculate fluctuations")
    say("Click on colour contrast for a different colour scheme")
    say("Press Run to execute this program")
  at = 0

lablSpeech = tk.Label(root, text = "Text-to-Speech", width = 12, background = "#363A4C", relief = tk.GROOVE, foreground = "white", borderwidth = 1, height = 1)
lablSpeech.grid(row = 4, column = 5, sticky = "NSE")
lablSpeech.bind("<Button-1>", runSpeechprep)

#*******************************Data Processing & Calculatino***********************************

def runExe(*args):
  stocktempList = varName.get().split()
  stocktemp = stocktempList[0]+".txt"

  file = open(stocktemp,"r")
  data = file.read()
  dataList = data.split()
  dateList = [];
  openList = [];
  closeList = [];
  print(dataList)
  start = False;
  for i in range(len(dataList)-1, -1, -1):
    if dataList[i][:8] == entStart.get():
      start = True
    if start == True:
      dateList.append(dataList[i][:8])
      openList.append(float(dataList[i][9:15]))
      closeList.append(float(dataList[i][15:]))
    if dataList[i][:8] == entEnd.get():
      start = False

  textbox.config(state = "normal")
  if varFunc.get() == "Compute Average Stock Prices":

    textbox.delete('1.0', tk.END)
    openAvg = 0.0
    for i in range(len(openList)):
      openAvg = openAvg+openList[i]+closeList[i]
    openAvg = openAvg/(len(openList)*2)
    textbox.insert(tk.INSERT, "The average of daily market opening and closing values is "+str(round(openAvg, 2))+"\n")

    textbox.insert(tk.INSERT, "\n")
    textbox.insert(tk.INSERT, "'Mean reversion' is financial theory suggesting that asset prices eventually return back to the long-run mean of the entire dataset. ")
    textbox.insert(tk.INSERT, "Typically, the price average is used in conjunction with the earning average for a P/E ratio that serves as the basis of comparison, ")
    textbox.insert(tk.INSERT, "but for the sake of this explanation, we will only concern ourselves with the former.\n")
    textbox.insert(tk.INSERT, "For instance, if\n\t total average = 10 and \n\t latest value = 8, \nMean reversion predicts an increase in the price of stocks until it reverses back to 10")
    textbox.insert(tk.INSERT, "\n")
    textbox.insert(tk.INSERT, "If the latest closing average is " + str(closeList[len(closeList)-1]) + ", then would mean reversion predict an increase? or decrease?")
    textbox.insert(tk.INSERT, "\n\n*Look on https://www.investopedia.com/terms/m/meanreversion.asp for more detail")

  elif varFunc.get() == "Find Highest & Lowest Rates":
    textbox.delete('1.0', tk.END)
    high = -1
    low = 300
    for i in range(len(openList)):
      if openList[i] > high:
        high = openList[i]
      if openList[i] < low:
        low = openList[i]
      if closeList[i] > high:
        high = closeList[i]
      if closeList[i] < low:
        low = closeList[i]

    textbox.insert(tk.INSERT, "The highest opening/closing stock price is "+str(high)+"\nThe lowest opening/closing stock price is "+str(low)+"\nThe range is "+str(round(high-low, 2)))

    textbox.insert(tk.INSERT, "\n")
    textbox.insert(tk.INSERT, "The range of stock prices, together with its mean, reveals the 'volatility' of a market index. This serves as a valuable indicator for the risk of an investment. ")
    textbox.insert(tk.INSERT, "Essentially, the greater the range, the higher the risk. Since the calculation of volatility is rather complicated, try to start by calculating ")
    textbox.insert(tk.INSERT, "this overall variation for yourself.\n")
    textbox.insert(tk.INSERT, "For instance, if\n\t total average is 16 and \n\t the highest point is 19 and \n\t the lowest point is 14, \nThe differences come out to be +3 and -2. ")
    textbox.insert(tk.INSERT, "When compared with the average, these variations weigh approximately 19% and 12%, respectively. This would be a considerable fluctuation and volatility would deem this stock to be riskier.\n")
    textbox.insert(tk.INSERT, "Knowing the highest & lowest stock prices of "+varName.get()+", can you use this program to similarly find the average and evaluate the risk of investing?")
    textbox.insert(tk.INSERT, "\n\n*Look on https://www.investopedia.com/terms/v/volatility.asp for more detail")

  elif varFunc.get() == "Calculate Fluctuations":
    textbox.delete('1.0', tk.END)
    textbox.insert(tk.INSERT, "the fluctuations from the opening to the closing prices are, in order, \n")
    for i in range(len(openList)):
      if closeList[i]/openList[i]-1 >= 0:
        textbox.insert(tk.INSERT, "+"+str(round(((closeList[i]/openList[i])-1)*100, 2))+"% increase on "+dateList[i]+"\n")
      else:
        textbox.insert(tk.INSERT, str(round(((closeList[i]/openList[i])-1)*100, 2))+"% decrease on "+dateList[i]+"\n")

    textbox.insert(tk.INSERT, "\n")
    textbox.insert(tk.INSERT, "Expressing daily market fluctuations in percentages simplistically and effectively presents the trend of a stock, as well as the rate of it. ")
    textbox.insert(tk.INSERT, "While this does provide an subjective perspective into its price variations in the short-term, an evaluation using the average (as opposed to the closing price) provides a more objective view in the long-run.\n")
    textbox.insert(tk.INSERT, "That said, this information would still pertain deeply to the field of work of day-traders, where frequent exchange of stocks is necessary. In this case, the value of this exchange depends on the closing price of the previous night, not the overall average.")
    textbox.insert(tk.INSERT, "\n")
    textbox.insert(tk.INSERT, "\nLooking at the the last few records, can you identify a trend in its fluctations? Do you have enough information to arrive at that conclusion?")


  textbox.config(state = "disabled")
#*****************************Execution Catalyst******************************

lablExec = tk.Label(root, text = "run", font = 40, background = "#363A4C", width = 8, foreground = "white", borderwidth = 2)
lablExec.grid(row = 5, column = 0, columnspan = 6, sticky = "NS", pady = 2)
root.bind('<Return>', runExe)

lablExec.bind("<Button-1>", runExe)

#********************************Output Box*************************************

textbox = tk.Text(root, height = 14, width = 80, borderwidth = 3, relief = tk.GROOVE)

textbox.config(state = "disabled")
textbox.grid(row = 6, column = 1, columnspan = 5)

root.mainloop()



