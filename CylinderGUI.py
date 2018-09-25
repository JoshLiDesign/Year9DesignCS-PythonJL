import tkinter as tk

def submit():
	r = float(entr.get())
	h = float(enth.get())

root = tk.Tk()
root.title("Volume of a cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="submit", command = submit)
btn.pack()

output = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief = tk.GROOVE)
output.pack()
output.config(state = "disabled")

root.mainloop()