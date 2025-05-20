from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry('3000x1000')
bgimage = ImageTk.PhotoImage(file='Blue.jpg')

con = sqlite3.connect('dataT.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Teachers (
            username TEXT NOT NULL,
            password TEXT NOT NULL)''')
con.commit()
con.close() 

def Teacher():
    if userentry.get()=='' or passwentry.get()=='':
        messagebox.showerror(title='Error', message='All fields are Required!')
    else:
        user = userentry.get()
        passw = passwentry.get()
        conn = sqlite3.connect('dataT.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Teachers WHERE username = ? AND password = ?", (user, passw))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo("Success", "Login Successful!")
            root.destroy()
            import Tresultpage
        else:
            messagebox.showerror("Failure", "Login Failed. Incorrect username or password.")

bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)

loginlabel = Label(root, text='Teacher Login', font=('Arial Black', '30'), bg='#9AD9EA', fg='#153E7D')
loginlabel.place(x=880, y=130)

userentry = Entry(root, width=40, font=('Arial', 10,'bold'), bd=0, fg='#153E7D', bg='#9AD9EA')
userentry.place(x=880,y=270)
userentry.insert(0, 'User ID')
userentry.bind("<FocusIn>", lambda e: userentry.delete(0, 'end'))

f1 = Frame(root, width=280, height=2, bg='#153E7D')
f1.place(x=880, y=288)

passwentry = Entry(root, width=40, font=('Arial', 10,'bold'), bd=0, fg='#153E7D', bg='#9AD9EA')
passwentry.place(x=880,y=310)
passwentry.insert(0, 'Password')
passwentry.bind("<FocusIn>", lambda e: passwentry.delete(0, 'end'))

f1 = Frame(root, width=280, height=2, bg='#153E7D')
f1.place(x=880, y=330)

Loginbutton = Button(root, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='#153e7D', activeforeground='white', activebackground='#153e7D', cursor='hand2', bd=0, width=20, command=Teacher)
Loginbutton.place(x=880, y=380)

root.mainloop()