from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

root = tk.Tk()
root.title("BRAND HUT")
#root.minsize(500,400)


def newpurchase():
   
    newpur = tk.Tk()
    newpur.title("Purchase Entry")
    #newpur.minsize(600,400)
    def connectmdb():
        try:
            mydb = mysql.connector.connect(host="localhost",  user="root",  password="haluha12")
            connectionLabel=Label(newpur, text="Successfully Connected").grid(row=0, column=1)
        except mysql.connector.Error as e:
            connectionLabel=Label(newpur, text="Failed to Connect").grid(row=0, column=1)
    
    ConB = Button(newpur, text="Connect", command=connectmdb)
    ConB.grid(row=0, column=0)        
    L1 = Label(newpur, text="Date")
    L1.grid(row = 1, column = 0)
    E1 = Entry(newpur)
    E1.grid(row=1, column=1)
    L2 = Label(newpur, text="Vendor")
    L2.grid(row=2, column=0)
    E2 = Entry(newpur)
    E2.grid(row=2, column=1)
    L3 = Label(newpur, text="Bill No.")
    L3.grid(row=3, column=0)
    E3 = Entry(newpur)
    E3.grid(row=3, column=1)
    L4 = Label(newpur, text="Qty.")
    L4.grid(row=4, column=0)
    E4 = Entry(newpur)
    E4.grid(row=4, column=1)
    L5 = Label(newpur, text="Rate")
    L5.grid(row=5, column=0)
    E5 = Entry(newpur)
    E5.grid(row=5, column=1)
    L6 = Label(newpur, text="Amount")
    L6.grid(row=6, column=0)
    E6 = Entry(newpur)
    E6.grid(row=6, column=1)
    L7 = Label(newpur, text="Paid Amount")
    L7.grid(row=7, column=0)
    E7 = Entry(newpur)
    E7.grid(row=7, column=1)
    L8 = Label(newpur, text="Balance")
    L8.grid(row=8, column=0)
    E8 = Entry(newpur)
    E8.grid(row=8, column=1)
    #connectionLabel = ttk.Label(newpur, text="Text").grid(row=9, column=1)
    SavePur = Button(newpur, text="Save Entry", ).grid(row=9, column=0)        
   

     

frame1 = LabelFrame(root, text="Purchasing", padx=20, pady=20, bg="light pink", relief=RIDGE)
frame1.grid(row=0, column=0)

bpur = Button(frame1, text="New Entry", command=newpurchase)
bpur.grid(row=0, column=0)

frame2 = LabelFrame(root, text="Production", padx=20, pady=20, bg="light blue", relief=RIDGE)
frame2.grid(row=0, column=1)

bprod = Button(frame2, text="New Entry")
bprod.grid(row=0, column=0)


frame3 = LabelFrame(root, text="Sales", padx=20, pady=20, bg="light green", relief=RIDGE)
frame3.grid(row=0, column=2)

bsale = Button(frame3, text="New Entry")
bsale.grid(row=0, column=0)


frame4 = LabelFrame(root, text="Expenditure", padx=20, pady=20, bg="light green", relief=RIDGE)
frame4.grid(row=1, column=0)

bexpn = Button(frame4, text="New Entry")
bexpn.grid(row=0, column=0)

frame5 = LabelFrame(root, text="Results", padx=20, pady=20, bg="light blue", relief=RIDGE)
frame5.grid(row=1, column=1)

brslt = Button(frame5, text="Open")
brslt.grid(row=0, column=0)

frame6 = LabelFrame(root, text="Analysis", padx=20, pady=20, bg="light pink", relief=RIDGE)
frame6.grid(row=1, column=2)

banls = Button(frame6, text="Open")
banls.grid(row=0, column=0)


root.mainloop()