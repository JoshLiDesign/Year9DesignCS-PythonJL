import tkinter as tk

root = tk.Tk()

textbox = tk.Text(root, height = 10, width = 50)

textbox.insert(tk.INSERT,"Textbox \n")
#textbox.insert(1.4, " ")
textbox.insert(tk.INSERT, "Demo")
textbox.config(state = "disabled")

textbox.pack()

root.mainloop()