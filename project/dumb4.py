from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3


username = "abdullah"

result_window = Tk()
result_window.geometry('800x800')
result_window.title('Result')

style = ttk.Style(result_window)
result_window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

use = Label(result_window, text=f"State of marks of", font=('Arial', '30'))
use.pack(pady=40)
cols = ['subjects', 'CA marks', 'assigh/projects', 'End-sem marks', 'Total marks', 'Precentage']

# Create a frame for the Treeview and scrollbars
treeframe = ttk.Frame(result_window)
treeframe.place(relx=0.5, rely=0.5, anchor="center")  # Center the Treeview

# Add a vertical scrollbar
v_scrollbar = ttk.Scrollbar(treeframe, orient="vertical")
v_scrollbar.pack(side="right", fill="y")

# Add a horizontal scrollbar
h_scrollbar = ttk.Scrollbar(treeframe, orient="horizontal")
h_scrollbar.pack(side="bottom", fill="x")

# Create the Treeview
treeview = ttk.Treeview(
    treeframe,
    columns=cols,
    show='headings',
    height=10,
    yscrollcommand=v_scrollbar.set,
    xscrollcommand=h_scrollbar.set
)

# Configure scrollbars
v_scrollbar.config(command=treeview.yview)
h_scrollbar.config(command=treeview.xview)

# Set column headings and dynamically adjust widths
for col in cols:
    treeview.heading(col, text=col, anchor='center')
    treeview.column(col, width=120, anchor='center', stretch=False)  # Fixed width, no stretching

treeview.pack()

# Fetch data from the database
conn = sqlite3.connect('dataP.db')
cursor = conn.cursor()
cursor.execute("SELECT subjects, CA, assighment, end, Total, precentage FROM results WHERE username = ?", (username,))
rows = cursor.fetchall()

# Insert data into the Treeview
for row in rows:
    treeview.insert("", "end", values=row)

# Adjust column widths based on data
for col in cols:
    treeview.column(col, width=max(len(col) * 10, 120))  # Adjust width dynamically

conn.close()

conn = sqlite3.connect('dataP.db')
cursor = conn.cursor()

cursor.execute("SELECT subjects, CA, assighment, end, Total, precentage FROM results WHERE username = ?", (username,))
rows = cursor.fetchall()

for row in rows:
    treeview.insert("", "end", values=row)

conn.close()

result_window.mainloop()