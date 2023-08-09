import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifanac')
cur=con.cursor
root = tk.Tk()
root.title("Number Sum")
root.geometry("800x600")
root.resizable(False,False)
root.configure(background="skyblue")
# Create and place the widgets



label1 = tk.Label(root, text="Student Details")
label1.pack()

l2 = tk.Label(root, text="Name")
l2.pack()
l2.place(x=10,y=30)

e2 = tk.Entry(root,width=30)
e2.pack()
e2.place(x=80,y=30)

l3 = tk.Label(root, text="Address")
l3.pack()
l3.place(x=10,y=90)

e3 = tk.Entry(root,width=40)
e3.pack()
e3.place(x=80,y=90)

l4 = tk.Label(root, text="DOB")
l4.pack()
l4.place(x=10,y=150)

e4 = tk.Entry(root)
e4.pack()
e4.place(x=80,y=150)
def day(event):
    day1 = combo.get()
    day2=e4.get()
    e4.delete(0,tk.END)
    e4.insert(0,str(day2)+day1+"/")
combo=ttk.Combobox(root,width = 20, textvariable=day)
combo.bind('<<ComboboxSelected>>',day)
combo.pack()
combo.place(x=250,y=150)

for x in range(32):
   combo['values']= tuple(list(combo['values']) + [str(x)])

def month(event):
   month1=combo2.get()
   month2=e4.get()
   e4.delete(0,tk.END)
   e4.insert(0,month2+str(month1)+"/")


n = tk.StringVar()

combo2=ttk.Combobox(root,width = 20,textvariable=month)
combo2.bind('<<ComboboxSelected>>',month)
combo2.pack()
combo2.place(x=420,y=150)

combo2['values'] = (' January',
						' February',
						' March',
						' April',
						' May',
						' June',
						' July',
						' August',
						' September',
						' October',
						' November',
						' December')

def year(event):
    year1=combo3.get()
    year2=e4.get()
    
    e4.insert(0,str(year1)+"/")

m = tk.StringVar()

combo3=ttk.Combobox(root,width = 20,textvariable=year)
combo3.bind('<<ComboboxSelected>>',year)
combo3.pack()
combo3.place(x=590,y=150)

for x in range(1990,2009):
   combo3['values']= tuple(list(combo3['values']) + [str(x)])

l5 = tk.Label(root, text="Sex")
l5.pack()
l5.place(x=10,y=210)

e5 = tk.Entry(root)
e5.pack()
e5.place(x=80,y=210)



def gender(gen):
    e5.delete(0,tk.END)
    e5.insert(0,""+gen)

R1 = ttk.Radiobutton(root, text="Male", variable=vars, value=1, command=lambda:gender("Male"))
R1.pack()
R1.place(x=250,y=210)

R2 = ttk.Radiobutton(root, text="Female", variable=vars, value=2, command=lambda:gender("Female"))
R2.pack()
R2.place(x=350,y=210)

l6 = tk.Label(root, text="Course")
l6.pack()
l6.place(x=10,y=270)

def course(num):
    first_course=e6.get()
    e6.delete(0,tk.END)
    e6.insert(0,str(first_course)+str(num)+",")   

check1=tk.Checkbutton(root,text="ICSE",variable=vars ,command=lambda:course("ICSE"))
check1.pack()
check1.place(x=80,y=270)

check2=tk.Checkbutton(root,text="MACT",variable=vars , command=lambda:course("MACT"))
check2.pack()
check2.place(x=160,y=270)

check2=tk.Checkbutton(root,text="PGDCA",variable=vars ,command=lambda:course("PGDCA"))
check2.pack()
check2.place(x=240,y=270)

e6 = tk.Entry(root)
e6.pack()
e6.place(x=380,y=270,width=270)

def clear():
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    e6.delete(0, tk.END)
    combo.delete(0, tk.END)
    combo2.delete(0, tk.END)
    combo3.delete(0, tk.END)


button1=tk.Button(root,text="Clear",width=10, command=clear)
button1.pack()
button1.place(x=260,y=330)

def end():
    root.quit()

button2=tk.Button(root,text="End",width=10, command=end)
button2.pack()
button2.place(x=360,y=330)

def save():
    name=e2.get()
    address=e3.get()
    dob=e4.get()
    sex=e5.get()
    course=e6.get()
    cur=con.cursor()
    if con:
        cur.execute("INSERT INTO STUDENT VALUE('%s','%s','%s','%s','%s')" %(name,address,dob,sex,course,))
        con.commit()
    messagebox.showinfo("Added Successfully")
    
   

button3=tk.Button(root,text="Save",width=10, command=save)
button3.pack()
button3.place(x=460,y=330)


root.mainloop()
