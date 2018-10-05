#tkinter is a module that holds code that you can use (tk is shortened name)
import tkinter as tk

#root is a var that holds the information about the main window, That is the 
#window with the close, min, max buttons in the top left

root = tk.Tk()

ent = tk.Entry(root)
ent.grid(row = 0, column = 0)
btn = tk.Button(root, text = "Press Me")
btn.grid(row = 0, column = 1)
label = tk.Label(root, text = "...")
label.grid(row = 0, column = 2)
#sets up your program in an infinite loop waiting for your user to do smth.
#This is an EVENT DRIVE PROGRAM. This means a fuction is called when an event happens
root.mainloop()
