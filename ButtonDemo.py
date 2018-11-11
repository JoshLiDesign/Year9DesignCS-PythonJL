import tkinter as tk

def run():
	print("it works")

root = tk.Tk()
root.title("ButtonDemo")

btn = tk.Button(root, text="run", command = run)
btn.pack()

root.mainloop()