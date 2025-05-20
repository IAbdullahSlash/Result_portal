import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('500x500')
root.title("Forest")

style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

treeframe = ttk.Frame(root)
treeframe.pack()

cols = ('subjects', 'Total marks', 'marks obtained', 'Grade')

treeview = ttk.Treeview(treeframe, height=20, columns=cols)
treeview.pack()

root.mainloop()