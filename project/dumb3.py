from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from project.dumb_data import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

username = "Abdullah"


# conn = sqlite3.connect('dataP.db')
# cursor = conn.cursor()
# cursor.execute("SELECT enroll, stream, dob FROM students WHERE username = ?", (username,))
# values = cursor.fetchall()

# enrolldata = values[0][0]
# streamdata = values[0][1]
# dobdata = values[0][2]

# conn.close()

# enroll = "2200104508"
# stream = "Science"
# dob = "2004-05-15"

conn = sqlite3.connect('dataP.db')
cursor = conn.cursor()
cursor.execute("SELECT enroll, stream, dob FROM students WHERE username = ?", (username,))
values = cursor.fetchall()

enrolldata = values[0][0]
streamdata = values[0][1]
dobdata = values[0][2]

conn.close()

result_window = Tk()
result_window.geometry('1400x800')
result_window.title('Result')

style = ttk.Style(result_window)
result_window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

use = ttk.Label(result_window, text=f"State of marks of {username}", font=('Arial', '30'))
use.pack(pady=40)

treeframe = ttk.Frame(result_window)
treeframe.place(x=60,y=220)


cols = ['subjects', 'CA marks', 'assigh/projects', 'End-sem marks', 'Total marks']
treeview = ttk.Treeview(treeframe, columns=cols, show='headings', height=5)
for col in cols:
    treeview.heading(col, text=col, anchor='center')
    treeview.column(col, width=120, anchor='center')
treeview.pack()


conn = sqlite3.connect('dataP.db')
cursor = conn.cursor()

cursor.execute("SELECT subjects, CA, assighment, end, Total FROM results WHERE username = ?", (username,))
rows = cursor.fetchall()

for row in rows:
    treeview.insert("", "end", values=row)

conn.close()

conn = sqlite3.connect('dataP.db')
cursor = conn.cursor()
cursor.execute("SELECT subjects, Total FROM results WHERE username = ?", (username,))
rows = cursor.fetchall()

marks_data = []
subjects = []
for row in rows:
    marks_data.append(row[1])
    subjects.append(row[0])

max_index = marks_data.index(max(marks_data))
highest_subject = subjects[max_index]
highest_marks = marks_data[max_index]    

conn.close()

fig1, ax1 = plt.subplots()
ax1.set_facecolor('#313131')
fig1.patch.set_facecolor('#414141')
bars = ax1.bar(subjects, marks_data, color='#515151')
ax1.set_title('Total marks in subjects chart', color='white')
ax1.set_xlabel('Subjects', color='white')
ax1.set_ylabel('marks', color='white')
for bar, value in zip(bars, marks_data):
    height = bar.get_height()
    ax1.annotate(f'{value}', xy=(bar.get_x() + bar.get_width() / 2, height), ha='center', color='white', fontsize=10)

ax1.set_yticks([])  
ax1.set_yticks([10, 30, 50, 70, 90]) 


ax1.grid(color='#555555', linestyle='--', linewidth=0.5) 
ax1.tick_params(axis='x', colors='white') 
ax1.tick_params(axis='y', colors='white')  

figureframe = ttk.Frame(result_window)
figureframe.place(x=850,y=100, width=500, height=400)

canvas1 = FigureCanvasTkAgg(fig1, master=figureframe)
canvas1.draw()
canvas1.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)

proficient = ttk.Label(result_window, text=f"The student is proficient in {highest_subject} with {highest_marks} marks!", font=('Arial', '12'))
proficient.place(x=860, y=520)

obtained = ttk.Label(result_window, text=f"Total obtained marks: {sum(marks_data)}/500", font=('Arial', '12'))
obtained.place(x=60, y=400)

totalpercentage = ttk.Label(result_window, text=f"Total percentage: {sum(marks_data)/5}%", font=('Arial', '12'))
totalpercentage.place(x=540, y=400)

result = ttk.Label(result_window, text=f"Result: {'Pass' if sum(marks_data) >= 250 else 'Fail'}", font=('Arial', '12'))
result.place(x=60, y=430)

stname = ttk.Label(result_window, text=f"Student Name: {username}", font=('Arial', '12'))
stname.place(x=60, y=130)

stenroll = ttk.Label(result_window, text=f"Enrollment No.: {enrolldata}", font=('Arial', '12'))
stenroll.place(x=60, y=170)

ststream = ttk.Label(result_window, text=f"Stream: {streamdata}", font=('Arial', '12'))
ststream.place(x=350, y=130)

dob = ttk.Label(result_window, text=f"Date of birth: {dobdata}", font=('Arial', '12'))
dob.place(x=350, y=170)

session = ttk.Label(result_window, text="Session: 2024-2025", font=('Arial', '12'))
session.place(x=600, y=130)





result_window.mainloop()