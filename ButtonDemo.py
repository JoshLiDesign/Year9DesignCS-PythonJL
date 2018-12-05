import tkinter as tk

def run():
	print("button clicked")

root = tk.Tk()
root.title("ButtonDemo")

btn = tk.Button(root, text="run", command = run)
btn.pack()

root.mainloop()