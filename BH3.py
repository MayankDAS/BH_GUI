from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox





root = tk.Tk()
root.title("BRAND HUT")
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 1, weight=1)
root.minsize(300,200)
root.iconbitmap('icov1.ico')





def connectmdb():
        try:
            mydb = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
            connectionLabel=Label(root, text="Successfully Connected").grid(row=2, column=2)
        except mysql.connector.Error as e:
            connectionLabel=Label(root, text="Failed to Connect").grid(row=2, column=2)
   
#-----------------------------------------------PURCHASING FRAME--------------------------------------------------------------------------------------------------------------
def newpurchase():

    newpur = Toplevel()
    newpur.title("Purchase Entry")
    newpur.minsize(500,300)
    newpur.iconbitmap('icov1.ico')
    
    def savepurchase():
        
        mydb = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
        mycursor = mydb.cursor()
       
        date=E1.get()
        party=E2.get()
        bill=E3.get()
        qtym=E4.get()
        ratem=E5.get()
        qtys=E44.get()
        rates=E55.get()

        if (ratem == ""):
            ratem=0
        if (qtym == ""):
            qtym=0
        if (rates == ""):
            rates=0
        if (qtys == ""):
            qtys=0

        amntm= float(qtym)*float(ratem)
        amnts= float(qtys)*float(rates)
        amntTT = amntm + amnts

        ratess=str(rates)
        qtyss=str(qtys)
        ratems=str(ratem)
        qtyms=str(qtym)
        amntms=str(amntm)
        amntss=str(amnts) 
        amntTTs=str(amntTT)

        if (amntm==0):
            items = " Sooji "
        elif (amnts==0):
            items = " Maida "
        else:
            items =" Maida Sooji "

        try:
            mycursor.execute("INSERT INTO purchasingentry (Date, Bill_Number, Unit, QuantityM, AmountM, Party_Name, RateM, Item, QuantityS, RateS, AmountS) VALUES ('"+ date +"','"+ bill +"','QTL','"+ qtyms +"','"+amntms+"','"+ party +"','"+ ratems +"', '"+items+"','"+ qtyss +"','"+ ratess +"','"+ amntss +"')")
            mycursor.execute("INSERT INTO partpaymentpurchase (AmountT, Party_Name, Bill_Number, BIll_Date, Balance, Balance_d) VALUES('"+amntTTs+"', '"+party+"','"+bill+"', '"+ date +"', '"+amntTTs+"', '"+amntTTs+"')")
            messagebox.showinfo("showinfo", "Successfully Submitted Entry for "+items)
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err) 
        mydb.commit() 
        

        #bal=amntt - amntpd
        
        #Lbal = Label(newpur, text=bal).grid(row=8, column=1) 
        Lamnt = Label(newpur, text=amntTTs).grid(row=9, column=1)  
        

    def querrybill():
        L10 = Label(newpur, text="                                                                                                                              ").grid(row=4, column=1)
        L11 = Label(newpur, text="                                                                                                                              ").grid(row=5, column=1)
        L11 = Label(newpur, text="                                                                                                                              ").grid(row=6, column=1)
        L11 = Label(newpur, text="                                                                                                                              ").grid(row=7, column=1)
        L11 = Label(newpur, text="                                                                                                                              ").grid(row=8, column=1)
        mydb = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
        mycursor = mydb.cursor()
        billqq=E10.get()
        mycursor.execute("SELECT AmountT, Party_Name, Amount_Paid, Balance, BIll_Date, Balance_d FROM partpaymentpurchase WHERE Bill_Number = '"+ billqq +"'")
        myresult = mycursor.fetchall()
        for x in myresult:
            amntqr = str(x[0])
            partyqr= str(x[1])
            pdqr= str(x[2])
            balqr= str(x[3])
            dateqr = str(x[4])
            bald = str(x[5])
        
        L11 = Label(frquery, text="Party: ").grid(row=3, column=0)
        L10 = Label(frquery, text=partyqr).grid(row=3, column=1)
        L11 = Label(frquery, text="Amount: ").grid(row=4, column=0)
        L10 = Label(frquery, text=amntqr).grid(row=4, column=1)
        L11 = Label(frquery, text="Paid: ").grid(row=5, column=0)
        L10 = Label(frquery, text=pdqr).grid(row=5, column=1)
        L11 = Label(frquery, text="Last Balance: ").grid(row=6, column=0)
        L10 = Label(frquery, text=bald).grid(row=6, column=1)
        L11 = Label(frquery, text="Bill Date: ").grid(row=7, column=0)
        L10 = Label(frquery, text=dateqr).grid(row=7, column=1)
    def updatepayment():
        L10 = Label(frquery, text="                                                                                                                     ").grid(row=5, column=1)
        L10 = Label(frquery, text="                                                                                                                     ").grid(row=6, column=1)
        L13 = Label(frquery, text="                                                                                                                     ").grid(row=11, column=1)
        
        mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
        mycursor = mainlog.cursor()
        billqq = E10.get()
        partdt = E12.get()
        partpay = E13.get()
        partdts = str(partdt)
        partpays = str(partpay)
        mycursor.execute("SELECT AmountT, Party_Name, Balance, Amount_Paid, BIll_Date, Bill_Number FROM partpaymentpurchase WHERE Bill_Number = '"+ billqq +"'")
        myresult = mycursor.fetchall()
        
        for x in myresult:
            amntqr = str(x[0])
            partyqr= str(x[1])
            balqr= str(x[2])
            amntpd = str(x[3])
            dateqr = str(x[4])
            bill = str(x[5])
        if (balqr=="None"):
            balqr="0"
        if (amntpd=="None"):
            amntpd="0"    
        #upamntt = float(amntqr) - float(partpay)
        #baln= float(amntqr) - float(partpay)  
        baln=float(balqr)-float(partpays)
       
        upamntpd = float(amntpd) + float(partpay)
        upamntpds= str(upamntpd)
        upamntT=float(amntqr) - float(upamntpds)
        upamntTs=str(upamntT)
        try:
            mycursor.execute("UPDATE partpaymentpurchase SET Balance='"+ upamntTs +"', Amount_Paid= '"+upamntpds+"' WHERE Bill_Number='"+ billqq +"' ")
            mycursor.execute("INSERT INTO partpaymentpurchase (AmountT, Party_Name, Bill_Number, Part_date, Part_payment, Balance, Amount_Paid, BIll_Date, Balance_d) VALUES('"+amntqr+"', '"+partyqr+"','"+bill+"', '"+partdts+"', '"+partpays+"', '"+ upamntTs +"','"+upamntpds+"','"+dateqr+"', '"+str(baln)+"' )") 
            messagebox.showinfo("showinfo", "Update Successfull")
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err)
        L10 = Label(frquery, text=upamntpds).grid(row=5, column=1)
        L13 = Label(frquery, text=upamntTs).grid(row=6, column=1)
        L10 = Label(frquery, text=upamntTs).grid(row=11, column=1)
        mainlog.commit()
    def savepack():
        mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
        mycursor = mainlog.cursor()
        date=E1.get()
        party=E2.get()
        bill=E3.get()
        qtypouch=E17.get()
        ratepouch=E18.get()
        qtybag=E19.get()
        ratebag=E20.get()
        qtycart=E21.get()
        ratecart=E22.get()

        if (qtypouch==""):
            qtypouch="0"
        if (ratepouch==""):
            ratepouch="0" 
        if (qtybag==""):
            qtybag="0" 
        if (ratebag==""):
            ratebag="0" 
        if (qtycart==""):
            qtycart="0" 
        if (ratecart==""):
            ratecart="0" 
   

        amntpouch = float(qtypouch) * float(ratepouch)
        amntbag = float(qtybag) * float(ratebag)
        amntcart = float(qtycart) * float(ratecart)
        amntpouchs=str(amntpouch)
        amntbags=str(amntbag)
        amntcarts=str(amntcart)
        thpack = float(qtypouch) * 0.1497
        thpacks =str(thpack)

        L20=Label(frpack, text=amntpouchs).grid(row=6, column=1)
        L21=Label(frpack, text=amntbags).grid(row=7, column=1)
        L22=Label(frpack, text=amntcarts).grid(row=8, column=1)
        try:
            mycursor.execute("INSERT INTO packingpurchase (Date, Party_Name, Bill_Number, QtyP, RateP, AmountP, QtyB, RateB, AmountB, QtyC, RateC, AmountC, packingth) VALUES('"+ date +"', '"+ party +"', '"+ bill +"', '"+ qtypouch +"', '"+ ratepouch +"', '"+ amntpouchs +"', '"+ qtybag +"', '"+ ratebag +"', '"+ amntbags +"', '"+ qtycart +"', '"+ ratecart +"', '"+ amntcarts +"', '"+ thpacks +"') ")
            messagebox.showinfo("showinfo", "Packing Entry Saved Successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err)
        mainlog.commit()

#____________________________NEW ENTRY____________________________________________________

    frnew = LabelFrame(newpur, text="New Bill Entry", padx=10, pady=10)
    frnew.grid(row=0, column=0, padx=10, pady=10)

    frquery = LabelFrame(newpur, text="Query and Update", padx=10, pady=10)
    frquery.grid(row=0, column=1, padx=10, pady=10)

    frpack = LabelFrame(newpur, text="Packing Materials", padx=10, pady=10)
    frpack.grid(row=0, column=2, padx=10, pady=10)

   
    L1 = Label(frnew, text="Date")
    L1.grid(row = 1, column = 0)
    E1 = Entry(frnew)
    E1.grid(row=1, column=1)
    L2 = Label(frnew, text="Vendor")
    L2.grid(row=2, column=0)
    E2 = Entry(frnew)
    E2.grid(row=2, column=1)
    L3 = Label(frnew, text="Bill No.")
    L3.grid(row=3, column=0)
    E3 = Entry(frnew)
    E3.grid(row=3, column=1)

    L4 = Label(frnew, text="Maida Qty.")
    L4.grid(row=5, column=0)
    E4 = Entry(frnew)
    E4.grid(row=6, column=0)
    L5 = Label(frnew, text="Maida Rate")
    L5.grid(row=7, column=0)
    E5 = Entry(frnew)
    E5.grid(row=8, column=0)
    

    L4 = Label(frnew, text="Sooji Qty.")
    L4.grid(row=5, column=1)
    E44 = Entry(frnew)
    E44.grid(row=6, column=1)
    L5 = Label(frnew, text="Sooji Rate")
    L5.grid(row=7, column=1)
    E55 = Entry(frnew)
    E55.grid(row=8, column=1)
    
    L6 = Label(frnew, text="Amount")
    L6.grid(row=9, column=0)
  
    L8 = Label(frnew, text="Balance")
    L8.grid(row=10, column=0)
    SavePur = Button(frnew, text="Save Entry", command=savepurchase).grid(row=11, column=1)  

#___________________________________PACKING___________________________________________________________________________ ____________________  
    
    LLp=Label(frpack, text="     ").grid(row=0, column=0)
   
    L17 = Label(frpack, text="Packing Pouch (Panni):").grid(row=0, column=0)
    
    L17 = Label(frpack, text="Qty (Kgs)").grid(row=0, column=1)
    L17 = Label(frpack, text="Rate").grid(row=0, column=2)
    E17 =Entry(frpack)
    E17.grid(row=1, column=1)
    E18 =Entry(frpack)
    E18.grid(row=1, column=2)

    L18 = Label(frpack, text="Packing Bags (Bori):").grid(row=2, column=0)

    L17 = Label(frpack, text="Qty (No.)").grid(row=2, column=1)
    L17 = Label(frpack, text="Rate").grid(row=2, column=2)
    E19 =Entry(frpack)
    E19.grid(row=3, column=1)
    E20 =Entry(frpack)
    E20.grid(row=3, column=2)
    
    L19 = Label(frpack, text="Empty Carton (Gatte):").grid(row=4, column=0)
    
    L17 = Label(frpack, text="Qty (No.)").grid(row=4, column=1)
    L17 = Label(frpack, text="Rate").grid(row=4, column=2)

    E21 =Entry(frpack)
    E21.grid(row=5, column=1)
    E22 =Entry(frpack)
    E22.grid(row=5, column=2)
    
    L20=Label(frpack, text="Amount Pouch:").grid(row=6, column=0)
    L21=Label(frpack, text="Amount Bags:").grid(row=7, column=0)
    L22=Label(frpack, text="Amount Carton:").grid(row=8, column=0)

    Bsavepack = Button(frpack, text="Save Packings", command=savepack).grid(row=9, column=1)

   
    # ___________________________ QUERY and UPDATE ___________________________________________________________________
    
    Lab = Label(frquery, text="                            ").grid(row=0, column=2)

    Lsb = Label(frquery, text="Search Bill:").grid(row=1, column=0)
    E10 = Entry(frquery)
    E10.grid(row=1, column=1)
    Bquerry = Button(frquery, text="Search",command=querrybill).grid(row=2, column=1)
    L12 = Label(frquery, text="      ").grid(row=8, column=0)
    L12 = Label(frquery, text="Enter Part Payment Date:").grid(row=9, column=0)
    E12 = Entry(frquery)
    E12.grid(row=9, column=1)
    L13 = Label(frquery, text="Part Payment:").grid(row=10, column=0)
    E13 = Entry(frquery)
    E13.grid(row=10, column=1)
    L13 = Label(frquery, text="Updated Balance:").grid(row=11, column=0)
    Bupdate = Button(frquery, text="Update Payment", command=updatepayment).grid(row=12, column=0)
#-----------------------------------------------PURCHASING FRAME ENDS--------------------------------------------------------------------------------------------------------------
   



#-----------------------------------------------PRODUCTION FRAME STARTS--------------------------------------------------------------------------------------------------------------


def newproduction():
    newprod = Toplevel()
    newprod.title("Production Entry")
    newprod.minsize(700,400)
    newprod.iconbitmap('icov1.ico')
    def savecons():
        mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="productionlog")
        mycursor = mainlog.cursor()
        date=E1.get()
        qtyM=E2.get()
        qtyS=E3.get()
       

        if (qtyM==""):
            qtyM="0"
        if (qtyS==""):
            qtyS="0" 
       
        if (qtyM=="" and qtyS==""):
            messagebox.showerror("showerror", "No entries!!") 

        upfactorM = E11.get()
        upfactorN = E10.get()
        factorN =StringVar(newprod, value='upfactorN')
        factorM =StringVar(newprod, value='upfactorM')
        
        thNoo= float(upfactorN) * float(qtyM)
        thNoos =str(thNoo)
        thMac= float(upfactorM) * float(qtyS)
        thMacs =str(thMac)





        try:
            mycursor.execute("INSERT INTO consumption (Date, QtyM, QtyS, ThNoodleProd, ThMacProd) VALUES('"+ date +"', '"+ qtyM +"', '"+ qtyS +"', '"+ thNoos +"', '"+ thMacs +"') ")
            messagebox.showinfo("showinfo", "Consumption Entry Saved Successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err)
        mainlog.commit()
    
   
    def saveprods():
        mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="productionlog")
        mycursor = mainlog.cursor()

        date=E1.get()
        qtyNoodle=E7.get()
        qtyMac=E8.get()
        qtyPasta=E9.get()

        if (qtyNoodle==""):
            qtyNoodle="0"
        if (qtyMac==""):
            qtyMac="0" 
        if (qtyPasta==""):
            qtyPasta="0" 
        
        qtypk = int(qtyNoodle) * 25
        qtypks=str(qtypk)
        qtycts=qtyNoodle
        qtybgs=qtyMac

        try:
            mycursor.execute("INSERT INTO production (Date, qtyNoodle, qtyMac, qtyPasta, QtyP, QtyB, QtyC) VALUES('"+ date +"', '"+ qtyNoodle +"', '"+ qtyMac +"', '"+ qtyPasta +"', '"+ qtypks +"','"+ qtybgs +"','"+ qtycts +"') ")
            messagebox.showinfo("showinfo", "Production Entry Saved Successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err)
        mainlog.commit()
    
#______________________________________ CONSUPTION ________________________________________________________________________

    L1 = Label(newprod, text="Today's Date").grid(row = 0, column = 0, padx=10, pady=10, sticky='W')
    E1 = Entry(newprod)
    E1.grid(row=0, column=0, padx=10, pady=10)

    frcons = LabelFrame(newprod, text="Consumption", padx=20, pady=20, height=400, width=400)
    frcons.grid(row=1, column=0, padx=20, pady=20)
    frprod = LabelFrame(newprod, text="Production", padx=20, pady=20,height=400, width=400)
    frprod.grid(row=1, column=1, padx=20, pady=20)

    L1 = Label(frcons, text="Maida Qty (Bori) :")
    L1.grid(row = 0, column = 0, padx=5, pady=5)
    E2 = Entry(frcons)
    E2.grid(row=0, column=1, padx=5, pady=5)
    
    L1 = Label(frcons, text="Sooji Qty (Bori) :").grid(row = 1, column = 0, padx=5, pady=5)
    E3 = Entry(frcons)
    E3.grid(row=1, column=1, padx=5, pady=5)

   

    L2= Label(frcons, text="              ").grid(row=0, column=2)
    L2= Label(frcons, text="              ").grid(row=2, column=0)
    factorN =StringVar(newprod, value='2.6')
    factorM =StringVar(newprod, value='2.4')
    L1 = Label(frcons, text="Noodle Factor :")
    L1.grid(row = 3, column = 0, padx=5, pady=5)
    E10 = Entry(frcons, textvariable=factorN)
    E10.grid(row=3, column=1, padx=5, pady=5)

    L1 = Label(frcons, text="Macroni Factor :")
    L1.grid(row = 4, column = 0, padx=5, pady=5)
    E11 = Entry(frcons, textvariable=factorM)
    E11.grid(row=4, column=1, padx=5, pady=5)

    Bsavecons = Button(frcons, text="Save Consumption", command=savecons).grid(row=6, column = 1, padx=5, pady=5)

#__________________________________________ PRODUCTION ________________________________________________________________________


    L1 = Label(frprod, text="Noodle Qty :")
    L1.grid(row = 0, column = 0, padx=5, pady=5)
    E7 = Entry(frprod)
    E7.grid(row=0, column=1, padx=5, pady=5)
    
    L1 = Label(frprod, text="Macroni Qty :")
    L1.grid(row = 1, column = 0, padx=5, pady=5)
    E8 = Entry(frprod)
    E8.grid(row=1, column=1, padx=5, pady=5)

    L1 = Label(frprod, text="Pasta Qty :")
    L1.grid(row = 2, column = 0, padx=5, pady=5)
    E9 = Entry(frprod)
    E9.grid(row=2, column=1, padx=5, pady=5)


    

    Bsaveprod = Button(frprod, text="Save Production", command=saveprods).grid(row=6, column = 1, padx=5, pady=5)

#-----------------------------------------------PRODUCTION FRAME ENDS--------------------------------------------------------------------------------------------------------------




#-----------------------------------------------SALES FRAME STARTS--------------------------------------------------------------------------------------------------------------

def newsales():
    newsale = Toplevel()
    newsale.title("Sales Entry")
    newsale.minsize(300,400)
    newsale.iconbitmap('icov1.ico')
    def savesales():
        mydb = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
        mycursor = mydb.cursor()
       
        date=E1.get()
        party=E2.get()
        bill=E3.get()

        qtyn=E4.get()
        raten=E5.get()
        qtym=E44.get()
        ratem=E55.get()
        qtyp=E6.get()
        ratep=E7.get()

        if (ratem == ""):
            ratem=0
        if (qtym == ""):
            qtym=0
        if (raten == ""):
            raten=0
        if (qtyn == ""):
            qtyn=0
        if (ratep == ""):
            ratep=0
        if (qtyp == ""):
            qtyp=0

        amntm= float(qtym)*float(ratem)
        amntn= float(qtyn)*float(raten)
        amntp= float(qtyp)*float(ratep)
        amntTT = amntm + amntn + amntp

        ratens=str(raten)
        qtyns=str(qtyn)
        ratems=str(ratem)
        qtyms=str(qtym)
        rateps=str(ratep)
        qtyps=str(qtyp)
        amntms=str(amntm)
        amntns=str(amntn) 
        amntps=str(amntp)
        amntTTs=str(amntTT)

        items=""

        NoodleSS = " Noodle "
        MacSS = " Macroni "
        PastaSS= " Pasta "


        if (amntns!="0.0"):
            items = items +" "+ NoodleSS
        if (amntms!="0.0"):
            items = items +" "+ MacSS
        
        if (amntps!="0.0"):
            items = items +" "+ PastaSS
       
        try:
            mycursor.execute("INSERT INTO salesentry (Date, Bill_Number, Party_Name, Item,  RateM, QtyM, AmountM,  QtyN, RateN, AmountN, QtyP, RateP, AmountP) VALUES ('"+ date +"','"+ bill +"','"+ party +"', '"+ items +"', '"+ ratems +"', '"+ qtyms +"','"+amntms+"','"+ qtyns +"','"+ ratens +"','"+ amntns +"','"+ qtyps +"','"+ rateps +"','"+ amntps +"') ")
            mycursor.execute("INSERT INTO paymentsales (AmountT, Party_Name, Bill_Number, Bill_Date, Balance_d, Balance) VALUES('"+amntTTs+"', '"+party+"','"+bill+"', '"+ date +"', '"+ amntTTs +"', '"+ amntTTs +"')")
            messagebox.showinfo("showinfo", "Successfully Submitted Sales Entry")
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err) 
        mydb.commit() 
        L6 = Label(frsale, text=amntTTs)
        L6.grid(row=9, column=1)
    
    def querrysales():
        L10 = Label(frpay, text="                                                                                                                              ").grid(row=4, column=1)
        L11 = Label(frpay, text="                                                                                                                              ").grid(row=5, column=1)
        L11 = Label(frpay, text="                                                                                                                              ").grid(row=6, column=1)
        L11 = Label(frpay, text="                                                                                                                              ").grid(row=7, column=1)
        L11 = Label(frpay, text="                                                                                                                              ").grid(row=8, column=1)
        mydb = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
        mycursor = mydb.cursor()
        billqq=E10.get()
        mycursor.execute("SELECT AmountT, Party_Name, Amount_Paid, Balance, Bill_Date, Balance_d FROM paymentsales WHERE Bill_Number = '"+ billqq +"'")
        myresult = mycursor.fetchall()
        for x in myresult:
            amntqr = str(x[0])
            partyqr= str(x[1])
            pdqr= str(x[2])
            balqr= str(x[3])
            dateqr = str(x[4])
            bald = str(x[5])
        
        L11 = Label(frpay, text="Party: ").grid(row=4, column=0)
        L10 = Label(frpay, text=partyqr).grid(row=4, column=1)
        L11 = Label(frpay, text="Amount: ").grid(row=5, column=0)
        L10 = Label(frpay, text=amntqr).grid(row=5, column=1)
        L11 = Label(frpay, text="Paid: ").grid(row=6, column=0)
        L10 = Label(frpay, text=pdqr).grid(row=6, column=1)
        L11 = Label(frpay, text="Last Balance: ").grid(row=7, column=0)
        L10 = Label(frpay, text=bald).grid(row=7, column=1)
        L11 = Label(frpay, text="Bill Date: ").grid(row=8, column=0)
        L10 = Label(frpay, text=dateqr).grid(row=8, column=1)
    
    def uppaysale():
        L10 = Label(frpay, text="                                                                                                                     ").grid(row=7, column=1)
        L10 = Label(frpay, text="                                                                                                                     ").grid(row=6, column=1)
                
        mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
        mycursor = mainlog.cursor()
        billqq = E10.get()
        partdt = E12.get()
        partpay = E13.get()
        partdts = str(partdt)
        partpays = str(partpay)
        mycursor.execute("SELECT AmountT, Party_Name, Balance, Amount_Paid, Bill_Date, Bill_Number, Balance_d FROM paymentsales WHERE Bill_Number = '"+ billqq +"'")
        myresult = mycursor.fetchall()
        
        for x in myresult:
            amntqr = str(x[0])
            partyqr= str(x[1])
            balqr= str(x[2])
            amntpd = str(x[3])
            dateqr = str(x[4])
            bill = str(x[5])
            bald = str(x[5])
        if (balqr=="None"):
            balqr="0"
        if (amntpd=="None"):
            amntpd="0"    
        #upamntt = float(amntqr) - float(partpay)
        #baln= float(amntqr) - float(partpay)  
        baln=float(balqr)-float(partpays)
        #upbal=float(baln) - float(partpays)
        #upbals=str(upbal)
        upamntpd = float(amntpd) + float(partpay)
        upamntpds= str(upamntpd)
        upamntT=float(amntqr) - float(upamntpds)
        upamntTs=str(upamntT)
        try:
            mycursor.execute("UPDATE paymentsales SET Balance='"+ upamntTs +"', Amount_Paid= '"+upamntpds+"' WHERE Bill_Number='"+ billqq +"' ")
            mycursor.execute("INSERT INTO paymentsales (AmountT, Party_Name, Bill_Number, Part_date, Part_Pay, Balance, Amount_Paid, Bill_Date, Balance_d) VALUES('"+amntqr+"', '"+partyqr+"','"+bill+"', '"+partdts+"', '"+partpays+"', '"+ upamntTs +"','"+upamntpds+"','"+dateqr+"', '"+str(baln)+"' )") 
            messagebox.showinfo("showinfo", "Update Successfull")
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err)
        L10 = Label(frpay, text=upamntpds).grid(row=6, column=1)
        L10 = Label(frpay, text=upamntTs).grid(row=12, column=1)
        L10 = Label(frpay, text=upamntTs).grid(row=7, column=1)
        mainlog.commit()

    frsale = LabelFrame(newsale, text="New Bill Entry", padx=20, pady=20, height=400, width=400)
    frsale.grid(row=1, column=0, padx=20, pady=20)
    frpay = LabelFrame(newsale, text="Part Payment Update", padx=20, pady=20,height=400, width=400)
    frpay.grid(row=1, column=1, padx=20, pady=20)  

#__________________________________________ New Bill Entry ________________________________________________________________________
    
    L1 = Label(frsale, text="Date")
    L1.grid(row = 1, column = 0, padx=5, pady=5)
    E1 = Entry(frsale)
    E1.grid(row=1, column=1, padx=5, pady=5)
    L2 = Label(frsale, text="Party")
    L2.grid(row=2, column=0, padx=5, pady=5)
    E2 = Entry(frsale)
    E2.grid(row=2, column=1, padx=5, pady=5)
    L3 = Label(frsale, text="Bill No.")
    L3.grid(row=3, column=0, padx=5, pady=5)
    E3 = Entry(frsale)
    E3.grid(row=3, column=1, padx=5, pady=5)

    L4 = Label(frsale, text="Noodle Qty.")
    L4.grid(row=5, column=0, padx=5, pady=5)
    E4 = Entry(frsale)
    E4.grid(row=6, column=0, padx=5, pady=5)
    L5 = Label(frsale, text="Noodle Rate")
    L5.grid(row=7, column=0, padx=5, pady=5)
    E5 = Entry(frsale)
    E5.grid(row=8, column=0, padx=5, pady=5)
    

    L4 = Label(frsale, text="Macroni Qty.")
    L4.grid(row=5, column=1, padx=5, pady=5)
    E44 = Entry(frsale)
    E44.grid(row=6, column=1, padx=5, pady=5)
    L5 = Label(frsale, text="Macroni Rate")
    L5.grid(row=7, column=1, padx=5, pady=5)
    E55 = Entry(frsale)
    E55.grid(row=8, column=1, padx=5, pady=5)
    
    L4 = Label(frsale, text="Pasta Qty.")
    L4.grid(row=5, column=2, padx=5, pady=5)
    E6 = Entry(frsale)
    E6.grid(row=6, column=2, padx=5, pady=5)
    L5 = Label(frsale, text="Pasta Rate")
    L5.grid(row=7, column=2, padx=5, pady=5)
    E7 = Entry(frsale)
    E7.grid(row=8, column=2, padx=5, pady=5)
    
    L6 = Label(frsale, text="Amount")
    L6.grid(row=9, column=0)
  
    Bsavesale = Button(frsale, text="Save New Bill", command=savesales).grid(row=11, column = 1, padx=5, pady=5)

#__________________________________________ Payment Update ________________________________________________________________________

   
    Lsb = Label(frpay, text="Search Bill:").grid(row=1, column=0)
    E10 = Entry(frpay)
    E10.grid(row=1, column=1)
    Bquerry = Button(frpay, text="Search",command=querrysales).grid(row=2, column=1)
    L12 = Label(frpay, text="      ").grid(row=3, column=0)
    

    L12 = Label(frpay, text="Enter Part Payment Date:").grid(row=10, column=0)
    E12 = Entry(frpay)
    E12.grid(row=10, column=1)
    L13 = Label(frpay, text="Part Payment:").grid(row=11, column=0)
    E13 = Entry(frpay)
    E13.grid(row=11, column=1)
    L13 = Label(frpay, text="Updated Balance:").grid(row=12, column=0)
    Bupdate = Button(frpay, text="Update Payment", command=uppaysale).grid(row=13, column=1)

#-----------------------------------------------SALES FRAME ENDS--------------------------------------------------------------------------------------------------------------




#-----------------------------------------------EXPENDITURE FRAME STARTS--------------------------------------------------------------------------------------------------------------

def expend():
    newexp = Toplevel()
    newexp.title("Expenditure Entry")
    newexp.minsize(400,300)
    newexp.iconbitmap('icov1.ico')
    def saveregx():
        mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="expenditure")
        mycursor = mainlog.cursor()

        date=E1.get()
        salary=E2.get()
        diesel=E3.get()
        electricity=E4.get()
        if (salary == ""):
            salary="0"
        if (diesel == ""):
            diesel="0"
        if (electricity == ""):
            electricity="0"
        texp = float(salary) + float(diesel) + float(electricity)
        texps = str(texp)

        try:
            mycursor.execute("INSERT INTO expreg (Date, Salary, Diesel, Electricity, expT ) VALUES('"+date+"', '"+salary+"','"+diesel+"', '"+electricity+"', '"+texps+"') ") 
            messagebox.showinfo("showinfo", "Expenditures Added")
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err)
        mainlog.commit()
        LT=Label(frregx, text="Total expenditure :").grid(row=6, column=0)
        LT=Label(frregx, text=texps).grid(row=6, column=1)
    
    def saveiregx():
        mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="expenditure")
        mycursor = mainlog.cursor()

        date=E5.get()
        name=E6.get()
        amnount=E7.get()

        try:
            mycursor.execute("INSERT INTO expireg (Date, Name, Amount) VALUES('"+date+"', '"+name+"','"+amnount+"') ") 
            messagebox.showinfo("showinfo", "Expenditures Added")
        except mysql.connector.Error as err:
            messagebox.showerror("showerror", err)
        mainlog.commit()

    def clrirx():
        E5 = Entry(friregx)
        E7 = Entry(friregx)
        E6 = Entry(friregx)
        E5.grid(row=0, column=1, padx=5, pady=5)
        E6.grid(row=1, column=1, padx=5, pady=5) 
        E7.grid(row=2, column=1, padx=5, pady=5)

#__________________________________________ REGULAR EXP________________________________________________________________________

    frregx = LabelFrame(newexp, text="Regular Expenditures", padx=10, pady=10, height=400, width=400)
    frregx.grid(row=0, column=0, padx=10, pady=10)

    friregx = LabelFrame(newexp, text="Irregular Expenditures", padx=10, pady=10, height=400, width=400)
    friregx.grid(row=0, column=1, padx=10, pady=10)

    L1 = Label(frregx, text="Date")
    L1.grid(row = 0, column = 0, padx=5, pady=5)
    E1 = Entry(frregx)
    E1.grid(row=0, column=1, padx=5, pady=5)

    L1 = Label(frregx, text="Rs.")
    L1.grid(row = 1, column = 1, padx=5, pady=5, sticky="W")
    

    L1 = Label(frregx, text="Salary :")
    L1.grid(row = 2, column = 0, padx=5, pady=5)
    E2 = Entry(frregx)
    E2.grid(row=2, column=1, padx=5, pady=5)

    L1 = Label(frregx, text="Diesel :")
    L1.grid(row = 3, column = 0, padx=5, pady=5)
    E3 = Entry(frregx)
    E3.grid(row=3, column=1, padx=5, pady=5)

    L1 = Label(frregx, text="Electricity :")
    L1.grid(row = 4, column = 0, padx=5, pady=5)
    E4 = Entry(frregx)
    E4.grid(row=4, column=1, padx=5, pady=5)

    B1 = Button(frregx, text="Save", command=saveregx).grid(row=7, column=1)

#__________________________________________ IRREGULAR EXP________________________________________________________________________

    L1 = Label(friregx, text="Date")
    L1.grid(row = 0, column = 0, padx=5, pady=5)
    E5 = Entry(friregx)
    E5.grid(row=0, column=1, padx=5, pady=5)

    L1 = Label(friregx, text="Name of Expenditure :")
    L1.grid(row = 1, column = 0, padx=5, pady=5)
    E6 = Entry(friregx)
    E6.grid(row=1, column=1, padx=5, pady=5)

    L1 = Label(friregx, text="Amount")
    L1.grid(row = 2, column = 0, padx=5, pady=5)
    E7 = Entry(friregx)
    E7.grid(row=2, column=1, padx=5, pady=5)

    B2 = Button(friregx, text="Save", command=saveiregx).grid(row=3, column=1)
    B3 = Button(friregx, text="Clear", command=clrirx).grid(row=3, column=0)

#-----------------------------------------------EXPENDITURE FRAME ENDS--------------------------------------------------------------------------------------------------------------





#-----------------------------------------------RESULTS FRAME STARTS--------------------------------------------------------------------------------------------------------------

def results():
    result = Toplevel()
    result.title("Results And Queries")
    result.minsize(400,300)
    result.iconbitmap('icov1.ico')
#__________________________________________________________VEIW LOGS______________________________________________________________________________________________
    def viewlistbox():
        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))
        

        Lb1 = Toplevel()
        Lb1.title("LOGS")
        #Lb1.minsize(300,300)
        Grid.rowconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 1, weight=1)
        
        dfrom=E1.get()
        dto=E2.get()

        d1 = drop1.get()
        d2 = drop2.get()
       
        canvas = Canvas(Lb1)
        
        canvas.grid(row=0, column=0, sticky=N+E+W+S)
        
        frlogs = Frame(canvas)

       

        #frlogs.configure(scrollregion=frlogs.bbox("all"))

        if (d1=="Purchase"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
            mycursor = mainlog.cursor()
            
            if (d2=="Maida"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QuantityM, RateM, AmountM FROM purchasingentry WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Item LIKE '%Maida%' ORDER BY Date DESC")
                myresult = mycursor.fetchall()
               
                rc=len(myresult)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Qty").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Rate").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)

                #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
                date = [lis[0] for lis in myresult]
                bill = [lis[1] for lis in myresult]
                party = [lis[2] for lis in myresult]
                qtym = [lis[3] for lis in myresult]
                ratem = [lis[4] for lis in myresult]
                amntm = [lis[5] for lis in myresult]
                #print(res[2])
                sumamnt=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtym[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(ratem[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=5)
                    Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                    if (str(amntm[y])=="None"):
                        amntm[y] = 0
                    sumamnt = sumamnt + float(str(amntm[y]))
                Lbb=Label(frlog, text="Total Purchasing :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlogs, text="Total Purchasing :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)

            if (d2=="Sooji"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QuantityS, RateS, AmountS FROM purchasingentry WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  AND Item LIKE '%Sooji%'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
               
                rc=len(myresult)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Qty").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Rate").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)
                #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
                date = [lis[0] for lis in myresult]
                bill = [lis[1] for lis in myresult]
                party = [lis[2] for lis in myresult]
                qtym = [lis[3] for lis in myresult]
                ratem = [lis[4] for lis in myresult]
                amntm = [lis[5] for lis in myresult]
                #print(res[2])
                sumamnt=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtym[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(ratem[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=5)
                    Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                    if (str(amntm[y])=="None"):
                        amntm[y] = 0
                    sumamnt = sumamnt + float(str(amntm[y]))
                Lbb=Label(frlog, text="Total Purchasing :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlogs, text="Total Purchasing :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)

            if (d2=="Maida and Sooji"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QuantityS, RateS, AmountS, QuantityM, RateM, AmountM FROM purchasingentry WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
               
                rc=len(myresult)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="QtyM").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="RateM").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="AmountS").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="QtyS").grid(row=0, column=6, sticky=N+W+E)
                Label(frlogs, text="RateS").grid(row=0, column=7, sticky=N+W+E)
                Label(frlogs, text="AmountS").grid(row=0, column=8, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=9, sticky=N+W+E)

                #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
                date = [lis[0] for lis in myresult]
                bill = [lis[1] for lis in myresult]
                party = [lis[2] for lis in myresult]
                qtys = [lis[3] for lis in myresult]
                rates = [lis[4] for lis in myresult]
                amnts = [lis[5] for lis in myresult]
                qtym = [lis[6] for lis in myresult]
                ratem = [lis[7] for lis in myresult]
                amntm = [lis[8] for lis in myresult]
                #print(res[2])
                sumamntm=0
                sumamnts=0
                
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtym[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(ratem[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(qtys[y])).grid(row=y+1, column=6)
                    Lb=Label(frlogs, text=str(rates[y])).grid(row=y+1, column=7)
                    Lb=Label(frlogs, text=str(amnts[y])).grid(row=y+1, column=8)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=9)
                    if (str(amntm[y])=="None"):
                        amntm[y] = 0
                    if (str(amnts[y])=="None"):
                        amnts[y] = 0
                    sumamntm = sumamntm + float(str(amntm[y]))
                    sumamnts = sumamnts + float(str(amnts[y]))
                sumamntt =sumamnts + sumamntm
                Lbb=Label(frlog, text="Total Purchasing :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamntt)).grid(row=3, column=1)
                Lbb=Label(frlogs, text="Total Purchasing :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamntt)).grid(row=rc+1, column=1)
            if (d2=="Pouches"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QtyP, RateP, AmountP FROM packingpurchase WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
               
                rc=len(myresult)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Qty").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Rate").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)

                #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
                date = [lis[0] for lis in myresult]
                bill = [lis[1] for lis in myresult]
                party = [lis[2] for lis in myresult]
                qtyp = [lis[3] for lis in myresult]
                ratep = [lis[4] for lis in myresult]
                amntp = [lis[5] for lis in myresult]
                #print(res[2])
                sumamnt=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(ratep[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntp[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                    if (str(amntp[y])=="None"):
                        amntp[y] = 0
                    sumamnt = sumamnt + float(str(amntp[y]))
                Lbb=Label(frlog, text="Total Purchasing :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlogs, text="Total Purchasing :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
            
            if (d2=="Bags"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QtyB, RateB, AmountB FROM packingpurchase WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
               
                rc=len(myresult)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Qty").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Rate").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)

                #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
                date = [lis[0] for lis in myresult]
                bill = [lis[1] for lis in myresult]
                party = [lis[2] for lis in myresult]
                qtyp = [lis[3] for lis in myresult]
                ratep = [lis[4] for lis in myresult]
                amntp = [lis[5] for lis in myresult]
                #print(res[2])
                sumamnt=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(ratep[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntp[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                    if (str(amntp[y])=="None"):
                        amntp[y] = 0
                    sumamnt = sumamnt + float(str(amntp[y]))
                Lbb=Label(frlog, text="Total Purchasing :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlogs, text="Total Purchasing :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
            
            if (d2=="Cartons"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QtyC, RateC, AmountC FROM packingpurchase WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
               
                rc=len(myresult)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Qty").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Rate").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)
                #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
                date = [lis[0] for lis in myresult]
                bill = [lis[1] for lis in myresult]
                party = [lis[2] for lis in myresult]
                qtyp = [lis[3] for lis in myresult]
                ratep = [lis[4] for lis in myresult]
                amntp = [lis[5] for lis in myresult]
                #print(res[2])
                sumamnt=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(ratep[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntp[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                    if (str(amntp[y])=="None"):
                        amntp[y] = 0
                    sumamnt = sumamnt + float(str(amntp[y]))
                Lbb=Label(frlog, text="Total Purchasing :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlogs, text="Total Purchasing :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
            if (d2=="All Packings"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QtyP, RateP, AmountP, QtyB, RateB, AmountB, QtyC, RateC, AmountC FROM packingpurchase WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
               
                rc=len(myresult)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="QtyP").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="RateP").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="AmountP").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="QtyB").grid(row=0, column=6, sticky=N+W+E)
                Label(frlogs, text="RateB").grid(row=0, column=7, sticky=N+W+E)
                Label(frlogs, text="AmountB").grid(row=0, column=8, sticky=N+W+E)
                Label(frlogs, text="QtyC").grid(row=0, column=9, sticky=N+W+E)
                Label(frlogs, text="RateC").grid(row=0, column=10, sticky=N+W+E)
                Label(frlogs, text="AmountC").grid(row=0, column=11, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=12, sticky=N+W+E)
                #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
                date = [lis[0] for lis in myresult]
                bill = [lis[1] for lis in myresult]
                party = [lis[2] for lis in myresult]
                qtyp = [lis[3] for lis in myresult]
                ratep = [lis[4] for lis in myresult]
                amntp = [lis[5] for lis in myresult]
                qtyb = [lis[6] for lis in myresult]
                rateb = [lis[7] for lis in myresult]
                amntb = [lis[8] for lis in myresult]
                qtyc = [lis[9] for lis in myresult]
                ratec = [lis[10] for lis in myresult]
                amntc = [lis[11] for lis in myresult]
                #print(res[2])
                sumamntp=0
                sumamntb=0
                sumamntc=0
                sumamnt=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(ratep[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntp[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(qtyb[y])).grid(row=y+1, column=6)
                    Lb=Label(frlogs, text=str(rateb[y])).grid(row=y+1, column=7)
                    Lb=Label(frlogs, text=str(amntb[y])).grid(row=y+1, column=8)
                    Lb=Label(frlogs, text=str(qtyc[y])).grid(row=y+1, column=9)
                    Lb=Label(frlogs, text=str(ratec[y])).grid(row=y+1, column=10)
                    Lb=Label(frlogs, text=str(amntc[y])).grid(row=y+1, column=11)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=12)
                    if (str(amntp[y])=="None"):
                        amntp[y] = 0
                    if (str(amntb[y])=="None"):
                        amntb[y] = 0
                    if (str(amntc[y])=="None"):
                        amntc[y] = 0
                    
                    sumamntp =  sumamntp +float(str(amntp[y]))
                    sumamntb =  sumamntb +float(str(amntb[y]))
                    sumamntc =  sumamntc +float(str(amntc[y]))
                    
                sumamnt = sumamntp + sumamntc + sumamntb
                Lbb=Label(frlog, text="Total Purchasing :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlogs, text="Total Purchasing :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
        if (d1=="Consumption"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="productionlog")
            mycursor = mainlog.cursor()
            
            if (d2=="Maida"):
                mycursor.execute("SELECT Date, QtyM, ThNoodleProd FROM consumption WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Quantity Consumed").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Theoretical Production Noodle").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
                date = [lis[0] for lis in myresult]
                qtym = [lis[1] for lis in myresult]
                thqtym = [lis[2] for lis in myresult]
              
                sumcon=0
                sumconth=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtym[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thqtym[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)
                    if (str(qtym[y])=="None"):
                        qtym[y] = 0
                    if (str(thqtym[y])=="None"):
                        thqtym[y] = 0
                    sumcon = sumcon + float(str(qtym[y]))
                    sumconth = sumconth + float(str(thqtym[y]))
                Lbb=Label(frlog, text="Total Consumption :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumcon)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Theoretical Noodles Produced :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumconth)).grid(row=4, column=1)

                Lbb=Label(frlogs, text="Total Consumption :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumcon)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Theoretical Noodles Produced :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumconth)).grid(row=rc+2, column=1)
               # Lbb=Label(frlog, text="Wastage :").grid(row=5, column=0)
               # Lbb=Label(frlog, text=str(sumconth-sumcon)).grid(row=5, column=1)
            
            if (d2=="Sooji"):
                mycursor.execute("SELECT Date, QtyS, ThMacProd FROM consumption WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                rc=len(myresult)
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Quantity Consumed").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Theoretical Production Macroni").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
                date = [lis[0] for lis in myresult]
                qtym = [lis[1] for lis in myresult]
                thqtym = [lis[2] for lis in myresult]
              
                sumcon=0
                sumconth=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtym[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thqtym[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)
                    if (str(qtym[y])=="None"):
                        qtym[y] = 0
                    if (str(thqtym[y])=="None"):
                        thqtym[y] = 0
                    sumcon = sumcon + float(str(qtym[y]))
                    sumconth = sumconth + float(str(thqtym[y]))
                Lbb=Label(frlog, text="Total Consumption :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumcon)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Theoretical Production Macroni :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumconth)).grid(row=4, column=1)

                Lbb=Label(frlogs, text="Total Consumption :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumcon)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Theoretical Production Macroni :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumconth)).grid(row=rc+2, column=1)
                #Lbb=Label(frlog, text="Wastage :").grid(row=5, column=0)
                #Lbb=Label(frlog, text=str(sumconth-sumcon)).grid(row=5, column=1)

            if (d2=="Maida and Sooji"):
                mycursor.execute("SELECT Date, QtyM, ThNoodleProd, QtyS, ThMacProd FROM consumption WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
               
                rc=len(myresult)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="QtyMaida").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Theoretical Production Noodle").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="QtySooji").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Theoretical Production Mac").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=5, sticky=N+W+E)
              
                date = [lis[0] for lis in myresult]
                qtym = [lis[1] for lis in myresult]
                thn = [lis[2] for lis in myresult]
                qtys = [lis[3] for lis in myresult]
                thm = [lis[4] for lis in myresult]
             
                sumamntm=0
                sumamnts=0
                sumconthm=0
                sumconthn=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtym[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thn[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtys[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(thm[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=5)
                    if (str(qtym[y])=="None"):
                        qtym[y] = 0
                    if (str(qtys[y])=="None"):
                        qtys[y] = 0
                    if (str(thn[y])=="None"):
                        thn[y] = 0
                    if (str(thm[y])=="None"):
                        thm[y] = 0
                    sumamntm = sumamntm + float(str(qtym[y]))
                    sumamnts = sumamnts + float(str(qtys[y]))
                    sumconthm = sumconthm + float(str(thm[y]))
                    sumconthn = sumconthn + float(str(thn[y]))
                sumamntt =sumamnts + sumamntm
                sumamntth = sumconthm + sumconthn
                Lbb=Label(frlog, text="Total Consumption :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamntt)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Total Theoretical Production :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumamntth)).grid(row=4, column=1)

                Lbb=Label(frlogs, text="Total Consumption :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamntt)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Total Theoretical Production :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumamntth)).grid(row=rc+2, column=1)
               # Lbb=Label(frlog, text="Total Wastage :").grid(row=5, column=0)
              #  Lbb=Label(frlog, text=str(sumamntth-sumamntt)).grid(row=5, column=1)
            
            if (d2=="Pouches"):
                mycursor.execute("SELECT Date, QtyP FROM production WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1) 
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis1[0] for lis1 in myresult]
                qtyp = [lis1[1] for lis1 in myresult]
                
                mainlog2 = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
                mycursor2 = mainlog2.cursor()
                mycursor2.execute("SELECT  packingth FROM packingpurchase WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  ORDER BY Date DESC ")
                myresult2 = mycursor2.fetchall()
                thpp = [lis[0] for lis in myresult2]


                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Qty Produced").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Qty Purchased (Th)").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
               
                sumamnt=0
                sumconthp=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thpp[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)
                    if (str(qtyp[y])=="None"):
                        qtyp[y] = 0
                    sumamnt = sumamnt + float(str(qtyp[y]))
                    if (str(thpp[y])=="None"):
                        thpp[y] = 0
                    sumconthp = sumconthp + float(str(thpp[y]))
                Lbb=Label(frlog, text="Total Produced Packings :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Total Purchased Packings :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumconthp)).grid(row=4, column=1)
                Lbb=Label(frlog, text="Packing in Stock :").grid(row=5, column=0)
                Lbb=Label(frlog, text=str(sumconthp-sumamnt)).grid(row=5, column=1)

                Lbb=Label(frlogs, text="Total Produced Packings :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Total Purchased Packings :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumconthp)).grid(row=rc+2, column=1)
                Lbb=Label(frlogs, text="Packing in Stock :").grid(row=rc+3, column=0)
                Lbb=Label(frlogs, text=str(sumconthp-sumamnt)).grid(row=rc+3, column=1)
            
            if (d2=="Bags"):
                mycursor.execute("SELECT Date, QtyB FROM production WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                qtyp= [lis[1] for lis in myresult]
                
                mainlog2 = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
                mycursor2 = mainlog2.cursor()
                mycursor2.execute("SELECT  QtyB FROM packingpurchase WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult2 = mycursor2.fetchall()
                thpp = [lis[0] for lis in myresult2]
                   
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Qty Produced").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Qty Purchased").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
                sumamnt=0
                sumconthp=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thpp[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)
                    if (str(qtyp[y])=="None"):
                        qtyp[y] = 0
                    sumamnt = sumamnt + float(str(qtyp[y]))
                    if (str(thpp[y])=="None"):
                        thpp[y] = 0
                    sumconthp = sumconthp + float(str(thpp[y]))
                Lbb=Label(frlog, text="Total Produced Bags :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Total Purchased Bags :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumconthp)).grid(row=4, column=1)
                Lbb=Label(frlog, text="Bags in Stock :").grid(row=5, column=0)
                Lbb=Label(frlog, text=str(sumconthp-sumamnt)).grid(row=5, column=1)

                Lbb=Label(frlogs, text="Total Produced Bags :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Total Purchased Bags :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumconthp)).grid(row=rc+2, column=1)
                Lbb=Label(frlogs, text="Bags in Stock :").grid(row=rc+3, column=0)
                Lbb=Label(frlogs, text=str(sumconthp-sumamnt)).grid(row=rc+3, column=1)

            if (d2=="Cartons"):
                mycursor.execute("SELECT Date, QtyC FROM production WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                qtyp= [lis[1] for lis in myresult]
                
                mainlog2 = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
                mycursor2 = mainlog2.cursor()
                mycursor2.execute("SELECT  QtyB FROM packingpurchase WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult2 = mycursor2.fetchall()
                thpp = [lis[0] for lis in myresult2]
                   
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Cartons Produced").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Cartons Purchased").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
                sumamnt=0
                sumconthp=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thpp[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)
                    if (str(qtyp[y])=="None"):
                        qtyp[y] = 0
                    sumamnt = sumamnt + float(str(qtyp[y]))
                    if (str(thpp[y])=="None"):
                        thpp[y] = 0
                    sumconthp = sumconthp + float(str(thpp[y]))
                Lbb=Label(frlog, text="Total Produced Cartons:").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Total Purchased Cartons:").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumconthp)).grid(row=4, column=1)
                Lbb=Label(frlog, text="CArtons in Stock:").grid(row=5, column=0)
                Lbb=Label(frlog, text=str(sumconthp-sumamnt)).grid(row=5, column=1)

                Lbb=Label(frlogs, text="Total Produced Cartons:").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Total Purchased Cartons:").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumconthp)).grid(row=rc+2, column=1)
                Lbb=Label(frlogs, text="CArtons in Stock:").grid(row=rc+3, column=0)
                Lbb=Label(frlogs, text=str(sumconthp-sumamnt)).grid(row=rc+3, column=1)
            if (d2=="All Packings"):
                messagebox.showerror("showerror", "Invalid Request")


        if (d1=="Production"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="productionlog")
            mycursor = mainlog.cursor()


            if (d2=="Noodle"):
                mycursor.execute("SELECT Date, qtyNoodle FROM production WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                qtyp= [lis[1] for lis in myresult]
                

                mycursor.execute("SELECT  ThNoodleProd FROM consumption WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult2 = mycursor.fetchall()
                thpp = [lis[0] for lis in myresult2]
                   
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Qty Produced").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="TH Production").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
                sumamnt=0
                sumconthp=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thpp[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)                   
                    if (str(qtyp[y])=="None"):
                        qtyp[y] = 0
                    sumamnt = sumamnt + float(str(qtyp[y]))
                    if (str(thpp[y])=="None"):
                        thpp[y] = 0
                    sumconthp = sumconthp + float(str(thpp[y]))
                Lbb=Label(frlog, text="Total Production of Noodle :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Total Theoretical Production :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumconthp)).grid(row=4, column=1)
                Lbb=Label(frlog, text="Wastage of Maida :").grid(row=5, column=0)
                Lbb=Label(frlog, text=str(sumconthp-sumamnt)).grid(row=5, column=1)

                Lbb=Label(frlogs, text="Total Production of Noodle :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Total Theoretical Production :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumconthp)).grid(row=rc+2, column=1)
                Lbb=Label(frlogs, text="Wastage of Maida :").grid(row=rc+3, column=0)
                Lbb=Label(frlogs, text=str(sumconthp-sumamnt)).grid(row=rc+3, column=1)
               
            if (d2=="Macroni"):
                mycursor.execute("SELECT Date, qtyMac FROM production WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                qtyp= [lis[1] for lis in myresult]
                
                mycursor.execute("SELECT  ThMacProd FROM consumption WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult2 = mycursor.fetchall()
                thpp = [lis[0] for lis in myresult2]
                   
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Qty Produced").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="TH Production").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
                sumamnt=0
                sumconthp=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thpp[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)                   
                    if (str(qtyp[y])=="None"):
                        qtyp[y] = 0
                    sumamnt = sumamnt + float(str(qtyp[y]))
                    if (str(thpp[y])=="None"):
                        thpp[y] = 0
                    sumconthp = sumconthp + float(str(thpp[y]))
                Lbb=Label(frlog, text="Total Production of Macroni :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Total Theoretical Production :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumconthp)).grid(row=4, column=1)
                Lbb=Label(frlog, text="Wastage of Sooji :").grid(row=5, column=0)
                Lbb=Label(frlog, text=str(sumconthp-sumamnt)).grid(row=5, column=1)

                Lbb=Label(frlogs, text="Total Production of Macroni :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Total Theoretical Production :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumconthp)).grid(row=rc+2, column=1)
                Lbb=Label(frlogs, text="Wastage of Sooji :").grid(row=rc+3, column=0)
                Lbb=Label(frlogs, text=str(sumconthp-sumamnt)).grid(row=rc+3, column=1)

            if (d2=="Pasta"):
                mycursor.execute("SELECT Date, qtyPasta FROM production WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                qtyp= [lis[1] for lis in myresult]
                
                mycursor.execute("SELECT  ThMacProd FROM consumption WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult2 = mycursor.fetchall()
                thpp = [lis[0] for lis in myresult2]
                   
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Qty Produced").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="TH MAc Production").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
                sumamnt=0
                sumconthp=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(thpp[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)                   
                    if (str(qtyp[y])=="None"):
                        qtyp[y] = 0
                    sumamnt = sumamnt + float(str(qtyp[y]))
                    if (str(thpp[y])=="None"):
                        thpp[y] = 0
                    sumconthp = sumconthp + float(str(thpp[y]))
                Lbb=Label(frlog, text="Total Production of Macroni :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)
                Lbb=Label(frlog, text="Total Theoretical Production Mac :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumconthp)).grid(row=4, column=1)
                Lbb=Label(frlog, text="Wastage of Sooji acc Mac :").grid(row=5, column=0)
                Lbb=Label(frlog, text=str(sumconthp-sumamnt)).grid(row=5, column=1)

                Lbb=Label(frlogs, text="Total Production of Macroni :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)
                Lbb=Label(frlogs, text="Total Theoretical Production Mac :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumconthp)).grid(row=rc+2, column=1)
                Lbb=Label(frlogs, text="Wastage of Sooji acc Mac :").grid(row=rc+3, column=0)
                Lbb=Label(frlogs, text=str(sumconthp-sumamnt)).grid(row=rc+3, column=1)

            if (d2=="All"):
                messagebox.showerror("showerror", "Invalid Request")

        if (d1=="Sale"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
            mycursor = mainlog.cursor()
            
            if (d2=="Noodle"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QtyN, RateN, AmountN FROM salesentry WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  AND Item LIKE '%Noodle%' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                bill= [lis[1] for lis in myresult]
                party= [lis[2] for lis in myresult]
                qtyn= [lis[3] for lis in myresult]
                raten= [lis[4] for lis in myresult]
                amntn= [lis[5] for lis in myresult]
                                  
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill No").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Qty").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Rate").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)
                sumamnt=0
                sumqty=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyn[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(raten[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntn[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                    if (str(qtyn[y])=="None"):
                        qtyn[y] = 0
                    if (str(amntn[y])=="None"):
                        amntn[y] = 0
                    sumamnt = sumamnt + float(str(amntn[y]))
                    sumqty=sumqty + float(str(qtyn[y]))
                
                Lbb=Label(frlog, text="Total Sale of Noodle :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumqty)).grid(row=3, column=1)    
                Lbb=Label(frlog, text="Total Amount :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=4, column=1)

                Lbb=Label(frlogs, text="Total Sale of Noodle :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumqty)).grid(row=rc+1, column=1)    
                Lbb=Label(frlogs, text="Total Amount :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+2, column=1)    
            
            if (d2=="Macroni"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QtyM, RateM, AmountM FROM salesentry WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  AND Item LIKE '%Macroni%' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                bill= [lis[1] for lis in myresult]
                party= [lis[2] for lis in myresult]
                qtyn= [lis[3] for lis in myresult]
                raten= [lis[4] for lis in myresult]
                amntn= [lis[5] for lis in myresult]
                                  
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill No").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Qty").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Rate").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)
                sumamnt=0
                sumqty=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyn[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(raten[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntn[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                    if (str(qtyn[y])=="None"):
                        qtyn[y] = 0
                    if (str(amntn[y])=="None"):
                        amntn[y] = 0
                    sumamnt = sumamnt + float(str(amntn[y]))
                    sumqty=sumqty + float(str(qtyn[y]))
                
                Lbb=Label(frlog, text="Total Sale of Macroni :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumqty)).grid(row=3, column=1)    
                Lbb=Label(frlog, text="Total Amount :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=4, column=1) 

                Lbb=Label(frlogs, text="Total Sale of Macroni :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumqty)).grid(row=rc+1, column=1)    
                Lbb=Label(frlogs, text="Total Amount :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+2, column=1)     

            if (d2=="Pasta"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QtyP, RateP, AmountP FROM salesentry WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"'  AND Item LIKE '%Pasta%' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                bill= [lis[1] for lis in myresult]
                party= [lis[2] for lis in myresult]
                qtyn= [lis[3] for lis in myresult]
                raten= [lis[4] for lis in myresult]
                amntn= [lis[5] for lis in myresult]
                                  
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill No").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Qty").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Rate").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)
                sumamnt=0
                sumqty=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyn[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(raten[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntn[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                    if (str(qtyn[y])=="None"):
                        qtyn[y] = 0
                    if (str(amntn[y])=="None"):
                        amntn[y] = 0
                    sumamnt = sumamnt + float(str(amntn[y]))
                    sumqty=sumqty + float(str(qtyn[y]))
                
                Lbb=Label(frlog, text="Total Sale of Pasta :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumqty)).grid(row=3, column=1)    
                Lbb=Label(frlog, text="Total Amount :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=4, column=1)

                Lbb=Label(frlogs, text="Total Sale of Pasta :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumqty)).grid(row=rc+1, column=1)    
                Lbb=Label(frlogs, text="Total Amount :").grid(row=rc+2, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+2, column=1)

            if (d2=="All"):
                mycursor.execute("SELECT Date, Bill_Number, Party_Name, QtyN, RateN, AmountN, QtyM, RateM, AmountM, QtyP, RateP, AmountP FROM salesentry WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                bill= [lis[1] for lis in myresult]
                party= [lis[2] for lis in myresult]
                qtyn= [lis[3] for lis in myresult]
                raten= [lis[4] for lis in myresult]
                amntn= [lis[5] for lis in myresult]
                qtym= [lis[6] for lis in myresult]
                ratem= [lis[7] for lis in myresult]
                amntm= [lis[8] for lis in myresult]
                qtyp= [lis[9] for lis in myresult]
                ratep= [lis[10] for lis in myresult]
                amntp= [lis[11] for lis in myresult]                                  
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Bill No").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="QtyN").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="RateN").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="AmountN").grid(row=0, column=5, sticky=N+W+E)
                Label(frlogs, text="QtyM").grid(row=0, column=6, sticky=N+W+E)
                Label(frlogs, text="RateM").grid(row=0, column=7, sticky=N+W+E)
                Label(frlogs, text="AmountM").grid(row=0, column=8, sticky=N+W+E)
                Label(frlogs, text="QtyP").grid(row=0, column=9, sticky=N+W+E)
                Label(frlogs, text="RateP").grid(row=0, column=10, sticky=N+W+E)
                Label(frlogs, text="AmountP").grid(row=0, column=11, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=12, sticky=N+W+E)
                sumamntm=0
                sumamntn=0
                sumamntp=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyn[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(raten[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(amntn[y])).grid(row=y+1, column=5)
                    Lb=Label(frlogs, text=str(qtym[y])).grid(row=y+1, column=6)
                    Lb=Label(frlogs, text=str(ratem[y])).grid(row=y+1, column=7)
                    Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=8)
                    Lb=Label(frlogs, text=str(qtyp[y])).grid(row=y+1, column=9)
                    Lb=Label(frlogs, text=str(ratep[y])).grid(row=y+1, column=10)
                    Lb=Label(frlogs, text=str(amntp[y])).grid(row=y+1, column=11)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=12)
                    if (str(amntm[y])=="None"):
                        amntm[y] = 0
                    if (str(amntn[y])=="None"):
                        amntn[y] = 0
                    if (str(amntp[y])=="None"):
                        amntp[y] = 0
                    sumamntn = sumamntn + float(str(amntn[y]))
                    sumamntm = sumamntm + float(str(amntm[y]))
                    sumamntp = sumamntp + float(str(amntp[y]))
                sumtt=sumamntp+sumamntm+sumamntn
                Lbb=Label(frlog, text="Total Sale Amount :").grid(row=4, column=0)
                Lbb=Label(frlog, text=str(sumtt)).grid(row=4, column=1)

                Lbb=Label(frlogs, text="Total Sale Amount :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumtt)).grid(row=rc+1, column=1)

        if (d1=="Expenditure"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="expenditure")
            mycursor = mainlog.cursor()

            if (d2=="Regular"):
                mycursor.execute("SELECT Date, Salary, Diesel, Electricity, expT FROM expreg WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                bill= [lis[1] for lis in myresult]
                party= [lis[2] for lis in myresult]
                qtyn= [lis[3] for lis in myresult]
                amntn= [lis[4] for lis in myresult]
                                  
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Salary").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Diesel").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Electricity").grid(row=0, column=3, sticky=N+W+E)
                Label(frlogs, text="Total").grid(row=0, column=4, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=5, sticky=N+W+E)
                sumamnt=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(qtyn[y])).grid(row=y+1, column=3)
                    Lb=Label(frlogs, text=str(amntn[y])).grid(row=y+1, column=4)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=5)
                    if (str(amntn[y])=="None"):
                        amntn[y] = 0
                    sumamnt = sumamnt + float(str(amntn[y]))
               
                Lbb=Label(frlog, text="Total Expenditure :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1)

                Lbb=Label(frlogs, text="Total Expenditure :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)

            if (d2=="Irregular"):
                mycursor.execute("SELECT Date, Name, Amount FROM expireg WHERE Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' ORDER BY Date DESC ")
                myresult = mycursor.fetchall()
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=1)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=3, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=4, column=0)
                Lbb=Label(frlog, text="                                                                                             ").grid(row=5, column=0)
                rc=len(myresult)
                date = [lis[0] for lis in myresult]
                name= [lis[1] for lis in myresult]
                amnt= [lis[2] for lis in myresult]
        
                Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
                Label(frlogs, text="Name").grid(row=0, column=1, sticky=N+W+E)
                Label(frlogs, text="Amount").grid(row=0, column=2, sticky=N+W+E)
                Label(frlogs, text="Sr. No.").grid(row=0, column=3, sticky=N+W+E)
                sumamnt=0
                for y in range(rc):
                    Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                    Lb=Label(frlogs, text=str(name[y])).grid(row=y+1, column=1)
                    Lb=Label(frlogs, text=str(amnt[y])).grid(row=y+1, column=2)
                    Lb=Label(frlogs, text=str(y+1)).grid(row=y+1, column=3)
                    if (str(amnt[y])=="None"):
                        amnt[y] = 0
                    sumamnt = sumamnt + float(str(amnt[y]))
               
                Lbb=Label(frlog, text="Total Expenditure :").grid(row=3, column=0)
                Lbb=Label(frlog, text=str(sumamnt)).grid(row=3, column=1) 

                Lbb=Label(frlogs, text="Total Expenditure :").grid(row=rc+1, column=0)
                Lbb=Label(frlogs, text=str(sumamnt)).grid(row=rc+1, column=1)   
                
        scrollbar = Scrollbar(Lb1, orient="vertical", command = canvas.yview )
        scrollbar.grid( row=0, column = 1, sticky=N+S)
        canvas.configure(yscrollcommand=scrollbar.set)  
        #canvas.create_window((4,4), window=frlogs, anchor="nw")  
        canvas.create_window((100,50), window=frlogs, anchor=tk.NW)
        frlogs.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)
        #frlogs.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
        canvas.configure(scrollregion=bbox, width=700, height=300)


    
    def binddrop1(event):

        list1item=drop1.get()
        if (list1item=="Purchase" or list1item=="Consumption"):
            drop2['values'] = ('Maida', 'Sooji', 'Maida and Sooji', 'Pouches', 'Bags', 'Cartons', 'All Packings') 
            drop2.current()
        if (list1item=="Production" or list1item=="Sale"):
            drop2['values'] = ('Noodle', 'Macroni', 'Pasta', 'All') 
            drop2.current()
        if (list1item=="Expenditure"):
            drop2['values'] = ('Regular', 'Irregular') 
            drop2.current()
#__________________________________________________________VEIW LOGS ENDS__________________________________________________________________________________________


#__________________________________________________________VEIW BILLS_________________________________________________________________________________________   

    def clearedbill():
        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))
        

        Lb1 = Toplevel()
        Lb1.title("LOGS")
        #Lb1.minsize(300,300)
        Grid.rowconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 1, weight=1)
        
        canvas = Canvas(Lb1)
        
        canvas.grid(row=0, column=0, sticky=N+E+W+S)
        
        frlogs = Frame(canvas)
        dfrom=E11.get()
        dto=E22.get()
        qtype=drop3.get()


        if (qtype=="Purchasing"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
            mycursor = mainlog.cursor()


            mycursor.execute("SELECT DISTINCT BIll_Date, Bill_Number, Party_Name, AmountT FROM partpaymentpurchase WHERE BIll_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Balance = '0.00' ORDER BY BIll_Date DESC ")
            myresult = mycursor.fetchall()
    
            rc=len(myresult)
            
            Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
            Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
            Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
            Label(frlogs, text="Amount").grid(row=0, column=3, sticky=N+W+E)
            
            Label(frlogs, text="Sr. No.").grid(row=0, column=4, sticky=N+W+E)

            #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
            date = [lis[0] for lis in myresult]
            bill = [lis[1] for lis in myresult]
            party = [lis[2] for lis in myresult]
            amntm = [lis[3] for lis in myresult]
            #print(res[2])
            sumamnt=0
            for y in range(rc):
                Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                
                Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=3)
                LL=Label(frlogs, text=str(y+1)).grid(row=y+1, column=4)
                if (str(amntm[y])=="None"):
                    amntm[y] = 0
                sumamnt = sumamnt + float(str(amntm[y]))
            LL=Label(frlogs, text="----------------------------------------------------------------------------------------------------------------------------------------------------------").grid(row=rc+1, column =0, columnspan=7)    
            LL=Label(frlogs, text="Total Cleared Amount :").grid(row=rc+2, column =0, columnspan=2)
            LL=Label(frlogs, text=str(sumamnt)).grid(row=rc+2, column =3)

        if (qtype=="Sales"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
            mycursor = mainlog.cursor()


            mycursor.execute("SELECT DISTINCT Bill_Date, Bill_Number, Party_Name, AmountT FROM paymentsales WHERE Bill_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Balance = '0.00' ORDER BY Bill_Date DESC ")
            myresult = mycursor.fetchall()
    
            rc=len(myresult)
           
            Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
            Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
            Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
            Label(frlogs, text="Amount").grid(row=0, column=3, sticky=N+W+E)
            
            Label(frlogs, text="Sr. No.").grid(row=0, column=4, sticky=N+W+E)

            #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
            date = [lis[0] for lis in myresult]
            bill = [lis[1] for lis in myresult]
            party = [lis[2] for lis in myresult]
            amntm = [lis[3] for lis in myresult]
            #print(res[2])
            sumamnt=0

            for y in range(rc):
                Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                
                Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=3)
                LL=Label(frlogs, text=str(y+1)).grid(row=y+1, column=4)
                if (str(amntm[y])=="None"):
                    amntm[y] = 0
                sumamnt = sumamnt + float(str(amntm[y]))
            LL=Label(frlogs, text="----------------------------------------------------------------------------------------------------------------------------------------------------------").grid(row=rc+1, column =0, columnspan=7)    
            LL=Label(frlogs, text="Total Cleared Amount :").grid(row=rc+2, column =0, columnspan=2)
            LL=Label(frlogs, text=str(sumamnt)).grid(row=rc+2, column =3)
            
            
        scrollbar = Scrollbar(Lb1, orient="vertical", command = canvas.yview )
        scrollbar.grid( row=0, column = 1, sticky=N+S)
        canvas.configure(yscrollcommand=scrollbar.set)  
        #canvas.create_window((4,4), window=frlogs, anchor="nw")  
        canvas.create_window((100,50), window=frlogs, anchor=tk.NW)
        frlogs.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)
        #frlogs.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
        canvas.configure(scrollregion=bbox, width=700, height=300)

    def pendingbill():
        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))
        

        Lb1 = Toplevel()
        Lb1.title("LOGS")
        #Lb1.minsize(300,300)
        Grid.rowconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 1, weight=1)
        
        canvas = Canvas(Lb1)
        
        canvas.grid(row=0, column=0, sticky=N+E+W+S)
        
        frlogs = Frame(canvas)
        dfrom=E11.get()
        dto=E22.get()
        qtype=drop3.get()

        if (qtype=="Purchasing"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
            mycursor = mainlog.cursor()


            mycursor.execute("SELECT DISTINCT BIll_Date, Bill_Number, Party_Name, AmountT, Balance, Amount_Paid FROM partpaymentpurchase WHERE BIll_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Balance != '0.00' ORDER BY BIll_Date DESC ")
            myresult = mycursor.fetchall()
    
            rc=len(myresult)
            
            Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
            Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
            Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
            Label(frlogs, text="Amount").grid(row=0, column=3, sticky=N+W+E)
            Label(frlogs, text="Amount_Paid").grid(row=0, column=4, sticky=N+W+E)

            Label(frlogs, text="Last Balance").grid(row=0, column=5, sticky=N+W+E)
            Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)

            #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
            date = [lis[0] for lis in myresult]
            bill = [lis[1] for lis in myresult]
            party = [lis[2] for lis in myresult]
            amntm = [lis[3] for lis in myresult]
            bal=[lis[4] for lis in myresult]    
            amntpdd= [lis[5] for lis in myresult]
            #print(res[2])
           

            sumamnt=0
            for y in range(rc):
                Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                Lb=Label(frlogs, text=str(bal[y])).grid(row=y+1, column=5)
                Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=3)
                Lb=Label(frlogs, text=str(amntpdd[y])).grid(row=y+1, column=4)
                LL=Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                if (str(amntpdd[y])=="None"):
                    amntpdd[y] = 0
                if (str(amntm[y])=="None"):
                    amntm[y] = 0
                sumamnt=sumamnt+float(str(amntm[y]))
                sumpd=sumpd+float(str(amntpdd[y]))
            LL=Label(frlogs, text="----------------------------------------------------------------------------------------------------------------------------------------------------------").grid(row=rc+1, column =0, columnspan=7)    
            LL=Label(frlogs, text="Total:").grid(row=rc+2, column =0)
            LL=Label(frlogs, text=str(sumamnt)).grid(row=rc+2, column =3)
            #LL=Label(frlogs, text="Total Paid Amount :").grid(row=rc+1, column =2)
            LL=Label(frlogs, text=str(sumpd)).grid(row=rc+2, column =4)
            #LL=Label(frlogs, text="Total pending Amount :").grid(row=rc+1, column =4)
            LL=Label(frlogs, text=str(sumamnt-sumpd)).grid(row=rc+2, column =5)

        if (qtype=="Sales"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
            mycursor = mainlog.cursor()


            mycursor.execute("SELECT DISTINCT Bill_Date, Bill_Number, Party_Name, AmountT, Balance, Amount_Paid FROM paymentsales WHERE Bill_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Balance != '0.00' ORDER BY Bill_Date DESC ")
            myresult = mycursor.fetchall()
    
            rc=len(myresult)
           
            Label(frlogs, text="Date").grid(row=0, column=0, sticky=N+W+E)
            Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
            Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
            Label(frlogs, text="Amount").grid(row=0, column=3, sticky=N+W+E)
            Label(frlogs, text="Amount_Paid").grid(row=0, column=4, sticky=N+W+E)

            Label(frlogs, text="Last Balance").grid(row=0, column=5, sticky=N+W+E)
            Label(frlogs, text="Sr. No.").grid(row=0, column=6, sticky=N+W+E)

            #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
            date = [lis[0] for lis in myresult]
            bill = [lis[1] for lis in myresult]
            party = [lis[2] for lis in myresult]
            amntm = [lis[3] for lis in myresult]
            bal= [lis[4] for lis in myresult]
            amntpdd= [lis[5] for lis in myresult]

            sumpd=0
            sumamnt=0
            for y in range(rc):
                Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                Lb=Label(frlogs, text=str(bal[y])).grid(row=y+1, column=5)
                Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=3)
                Lb=Label(frlogs, text=str(amntpdd[y])).grid(row=y+1, column=4)
                LL=Label(frlogs, text=str(y+1)).grid(row=y+1, column=6)
                if (str(amntpdd[y])=="None"):
                    amntpdd[y] = 0
                if (str(amntm[y])=="None"):
                    amntm[y] = 0
                sumamnt=sumamnt+float(str(amntm[y]))
                sumpd=sumpd+float(str(amntpdd[y]))
            LL=Label(frlogs, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").grid(row=rc+1, column =0, columnspan=10)
            LL=Label(frlogs, text="Total:").grid(row=rc+2, column =0)
            LL=Label(frlogs, text=str(sumamnt)).grid(row=rc+2, column =3)
            #LL=Label(frlogs, text="Total Paid Amount :").grid(row=rc+1, column =2)
            LL=Label(frlogs, text=str(sumpd)).grid(row=rc+2, column =4)
            #LL=Label(frlogs, text="Total pending Amount :").grid(row=rc+1, column =4)
            LL=Label(frlogs, text=str(sumamnt-sumpd)).grid(row=rc+2, column =5)
       

        scrollbar = Scrollbar(Lb1, orient="vertical", command = canvas.yview )
        scrollbar.grid( row=0, column = 1, sticky=N+S)
        canvas.configure(yscrollcommand=scrollbar.set)  
        #canvas.create_window((4,4), window=frlogs, anchor="nw")  
        canvas.create_window((100,50), window=frlogs, anchor=tk.NW)
        frlogs.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)
        #frlogs.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
        canvas.configure(scrollregion=bbox, width=700, height=300)
   
    def partybills():
        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))
        

        Lb1 = Toplevel()
        Lb1.title("LOGS")
        #Lb1.minsize(300,300)
        Grid.rowconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 1, weight=1)
        
        canvas = Canvas(Lb1)
        
        canvas.grid(row=0, column=0, sticky=N+E+W+S)
        
        frlogs = Frame(canvas)
        dfrom=E11.get()
        dto=E22.get()
        qtype=drop3.get()
        partyname=E3.get()
        billquery=E4.get()

       
        if (qtype=="Purchasing"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
            mycursor = mainlog.cursor()


            mycursor.execute("SELECT BIll_Date, Bill_Number, Party_Name, AmountT, Balance_d, Part_date, Part_payment, Amount_Paid, Balance FROM partpaymentpurchase WHERE BIll_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Party_Name = '"+partyname+"' ORDER BY BIll_Date DESC ")
            myresult = mycursor.fetchall()
            


            rc=len(myresult)
          
            Lb=Label(frlogs, text="Bill_Date").grid(row=0, column=0, sticky=N+W+E)
            Lb=Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
            Lb=Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
          
            Lb=Label(frlogs, text="Amount").grid(row=0, column=3, sticky=N+W+E)
            #Lb=Label(frlogs, text="Last Balance").grid(row=0, column=7, sticky=N+W+E)
            Lb=Label(frlogs, text="Balance").grid(row=0, column=6, sticky=N+W+E)
            Lb=Label(frlogs, text="Part_Date").grid(row=0, column=4, sticky=N+W+E)
            Lb=Label(frlogs, text="Part_Payment").grid(row=0, column=5, sticky=N+W+E)
            #Lb=Label(frlogs, text="Amount_Paid").grid(row=0, column=4, sticky=N+W+E)
            Lb=Label(frlogs, text="Sr. No.").grid(row=0, column=7, sticky=N+W+E)

            #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
            date = [lis[0] for lis in myresult]
            bill = [lis[1] for lis in myresult]
            party = [lis[2] for lis in myresult]
            amntm = [lis[3] for lis in myresult]
            bal = [lis[4] for lis in myresult]
            ptdat = [lis[5] for lis in myresult]
            ptpay = [lis[6] for lis in myresult]
            amntpd = [lis[7] for lis in myresult]
            bald=[lis[8] for lis in myresult]
            #print(res[2])
            
            cursor2 = mainlog.cursor()
            cursor2.execute("SELECT Balance FROM partpaymentpurchase WHERE BIll_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Party_Name = '"+partyname+"' GROUP BY Bill_Number ORDER BY BIll_Date DESC ")
            result2 = cursor2.fetchall()
            rc2=len(result2)
            bal2=[lis2[0] for lis2 in result2]
            sumbal2 = 0
            for i in range(rc2):
                sumbal2 = sumbal2 + float(bal2[i])
            LL=Label(frlogs, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").grid(row=rc+1, column =0, columnspan=10)
            LL=Label(frlogs, text="Total Pending Balance: ").grid(row=rc+2, column=0, columnspan=2)
            LL=Label(frlogs, text=str(sumbal2)).grid(row=rc+2, column=6)


            sumamnt=0
            for y in range(rc):
                Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=3)
                #Lb=Label(frlogs, text=str(bal[y])).grid(row=y+1, column=7)
                Lb=Label(frlogs, text=str(bald[y])).grid(row=y+1, column=6)
                Lb=Label(frlogs, text=str(ptdat[y])).grid(row=y+1, column=4)
                Lb=Label(frlogs, text=str(ptpay[y])).grid(row=y+1, column=5)
                #Lb=Label(frlogs, text=str(amntpd[y])).grid(row=y+1, column=4)
                LL=Label(frlogs, text=str(y+1)).grid(row=y+1, column=7)
            
        if (qtype=="Sales"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
            mycursor = mainlog.cursor()


            mycursor.execute("SELECT Bill_Date, Bill_Number, Party_Name, AmountT, Balance, Part_Date, Part_Pay, Amount_Paid, Balance_d FROM paymentsales WHERE Bill_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Party_Name = '"+partyname+"' ORDER BY BIll_Date DESC ")
            myresult = mycursor.fetchall()
    
            rc=len(myresult)
         
            Lb=Label(frlogs, text="Bill_Date").grid(row=0, column=0, sticky=N+W+E)
            Lb=Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
            Lb=Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
          
            Lb=Label(frlogs, text="Amount").grid(row=0, column=3, sticky=N+W+E)
            #Lb=Label(frlogs, text="Last Balance").grid(row=0, column=7, sticky=N+W+E)
            Lb=Label(frlogs, text="Balance").grid(row=0, column=6, sticky=N+W+E)
            Lb=Label(frlogs, text="Part_Date").grid(row=0, column=4, sticky=N+W+E)
            Lb=Label(frlogs, text="Part_Payment").grid(row=0, column=5, sticky=N+W+E)
            #Lb=Label(frlogs, text="Amount_Paid").grid(row=0, column=4, sticky=N+W+E)
            Lb=Label(frlogs, text="Sr. No.").grid(row=0, column=7, sticky=N+W+E)

            #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
            date = [lis[0] for lis in myresult]
            bill = [lis[1] for lis in myresult]
            party = [lis[2] for lis in myresult]
            amntm = [lis[3] for lis in myresult]
            bal = [lis[4] for lis in myresult]
            ptdat = [lis[5] for lis in myresult]
            ptpay = [lis[6] for lis in myresult]
            amntpd = [lis[7] for lis in myresult]
            bald=[lis[8] for lis in myresult]
            
            cursor2 = mainlog.cursor()
            cursor2.execute("SELECT Balance FROM paymentsales WHERE BIll_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Party_Name = '"+partyname+"' GROUP BY Bill_Number ORDER BY Bill_Date DESC ")
            result2 = cursor2.fetchall()
            rc2=len(result2)
            bal2=[lis2[0] for lis2 in result2]
            sumbal2 = 0
            for i in range(rc2):
                sumbal2 = sumbal2 + float(bal2[i])
            LL=Label(frlogs, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").grid(row=rc+1, column =0, columnspan=10)    
            LL=Label(frlogs, text="Total Pending Balance: ").grid(row=rc+2, column=0, columnspan=2)
            LL=Label(frlogs, text=str(sumbal2)).grid(row=rc+2, column=6)


            sumamnt=0
            for y in range(rc):
                Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=3)
                #Lb=Label(frlogs, text=str(bal[y])).grid(row=y+1, column=7)
                Lb=Label(frlogs, text=str(bald[y])).grid(row=y+1, column=6)
                Lb=Label(frlogs, text=str(ptdat[y])).grid(row=y+1, column=4)
                Lb=Label(frlogs, text=str(ptpay[y])).grid(row=y+1, column=5)
                #Lb=Label(frlogs, text=str(amntpd[y])).grid(row=y+1, column=4)
                LL=Label(frlogs, text=str(y+1)).grid(row=y+1, column=7)        


        scrollbar = Scrollbar(Lb1, orient="vertical", command = canvas.yview )
        scrollbar.grid( row=0, column = 1, sticky=N+S)
        canvas.configure(yscrollcommand=scrollbar.set)  
        #canvas.create_window((4,4), window=frlogs, anchor="nw")  
        canvas.create_window((100,50), window=frlogs, anchor=tk.NW)
        frlogs.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)
        #frlogs.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
        canvas.configure(scrollregion=bbox, width=700, height=300)

    def billpart():
        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))
        

        Lb1 = Toplevel()
        Lb1.title("LOGS")
        #Lb1.minsize(300,300)
        Grid.rowconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 0, weight=1)
        Grid.columnconfigure(Lb1, 1, weight=1)
        
        canvas = Canvas(Lb1)
        
        canvas.grid(row=0, column=0, sticky=N+E+W+S)
        
        frlogs = Frame(canvas)
        dfrom=E11.get()
        dto=E22.get()
        qtype=drop3.get()
        partyname=E3.get()
        billquery=E4.get()

     

        if (qtype=="Purchasing"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
            mycursor = mainlog.cursor()


            mycursor.execute("SELECT BIll_Date, Bill_Number, Party_Name, AmountT, Balance, Part_date, Part_payment, Amount_Paid, Balance_d FROM partpaymentpurchase WHERE BIll_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Bill_Number = '"+billquery+"' ORDER BY BIll_Date DESC ")
            myresult = mycursor.fetchall()
    
            rc=len(myresult)
        
            L5=Label(frlogs, text="Bill_Date").grid(row=0, column=0, sticky=N+W+E)
            LL=Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
            LL=Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
          
            LL=Label(frlogs, text="Amount").grid(row=0, column=3, sticky=N+W+E)
            #Lb=Label(frlogs, text="Last Balance").grid(row=0, column=7, sticky=N+W+E)
            Lb=Label(frlogs, text="Balance").grid(row=0, column=6, sticky=N+W+E)
            LL=Label(frlogs, text="Part_Date").grid(row=0, column=4, sticky=N+W+E)
            LL=Label(frlogs, text="Part_Payment").grid(row=0, column=5, sticky=N+W+E)
            #LL=Label(frlogs, text="Amount_Paid").grid(row=0, column=4, sticky=N+W+E)
            LL=Label(frlogs, text="Sr. No.").grid(row=0, column=7, sticky=N+W+E)

            #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
            date = [lis[0] for lis in myresult]
            bill = [lis[1] for lis in myresult]
            party = [lis[2] for lis in myresult]
            amntm = [lis[3] for lis in myresult]
            bal = [lis[4] for lis in myresult]
            ptdat = [lis[5] for lis in myresult]
            ptpay = [lis[6] for lis in myresult]
            amntpd = [lis[7] for lis in myresult]
            bald=[lis[8] for lis in myresult]
            sumamnt=0
            for y in range(rc):
                Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=3)
                #Lb=Label(frlogs, text=str(bal[y])).grid(row=y+1, column=7)
                Lb=Label(frlogs, text=str(bald[y])).grid(row=y+1, column=6)
                Lb=Label(frlogs, text=str(ptdat[y])).grid(row=y+1, column=4)
                Lb=Label(frlogs, text=str(ptpay[y])).grid(row=y+1, column=5)
                #Lb=Label(frlogs, text=str(amntpd[y])).grid(row=y+1, column=4)
                LL=Label(frlogs, text=str(y+1)).grid(row=y+1, column=7)
        
        if (qtype=="Sales"):
            mainlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
            mycursor = mainlog.cursor()


            mycursor.execute("SELECT Bill_Date, Bill_Number, Party_Name, AmountT, Balance, Part_Date, Part_Pay, Amount_Paid, Balance_d FROM paymentsales WHERE Bill_Date BETWEEN '"+ dfrom +"' AND '"+ dto +"' AND Bill_Number = '"+billquery+"' ORDER BY BIll_Date DESC ")
            myresult = mycursor.fetchall()
    
            rc=len(myresult)
            
            LL=Label(frlogs, text="Bill_Date").grid(row=0, column=0, sticky=N+W+E)
            LL=Label(frlogs, text="Bill").grid(row=0, column=1, sticky=N+W+E)
            LL=Label(frlogs, text="Party").grid(row=0, column=2, sticky=N+W+E)
          
            LL=Label(frlogs, text="Amount").grid(row=0, column=3, sticky=N+W+E)
            #Lb=Label(frlogs, text="Last Balance").grid(row=0, column=7, sticky=N+W+E)
            Lb=Label(frlogs, text="Balance").grid(row=0, column=6, sticky=N+W+E)
            LL=Label(frlogs, text="Part_Date").grid(row=0, column=4, sticky=N+W+E)
            LL=Label(frlogs, text="Part_Payment").grid(row=0, column=5, sticky=N+W+E)
            #LL=Label(frlogs, text="Amount_Paid").grid(row=0, column=4, sticky=N+W+E)
            LL=Label(frlogs, text="Sr. No.").grid(row=0, column=7, sticky=N+W+E)

            #Lb1.insert(1, "Date                Bill_Number                Party                     Qty      Rate         Amount")
            date = [lis[0] for lis in myresult]
            bill = [lis[1] for lis in myresult]
            party = [lis[2] for lis in myresult]
            amntm = [lis[3] for lis in myresult]
            bal = [lis[4] for lis in myresult]
            ptdat = [lis[5] for lis in myresult]
            ptpay = [lis[6] for lis in myresult]
            amntpd = [lis[7] for lis in myresult]
            bald=[lis[8] for lis in myresult]
            sumamnt=0
            for y in range(rc):
                Lb=Label(frlogs, text=str(date[y])).grid(row=y+1, column=0)
                Lb=Label(frlogs, text=str(bill[y])).grid(row=y+1, column=1)
                Lb=Label(frlogs, text=str(party[y])).grid(row=y+1, column=2)
                Lb=Label(frlogs, text=str(amntm[y])).grid(row=y+1, column=3)
                #Lb=Label(frlogs, text=str(bal[y])).grid(row=y+1, column=7)
                Lb=Label(frlogs, text=str(bald[y])).grid(row=y+1, column=6)
                Lb=Label(frlogs, text=str(ptdat[y])).grid(row=y+1, column=4)
                Lb=Label(frlogs, text=str(ptpay[y])).grid(row=y+1, column=5)
                #Lb=Label(frlogs, text=str(amntpd[y])).grid(row=y+1, column=4)
                LL=Label(frlogs, text=str(y+1)).grid(row=y+1, column=7)
        scrollbar = Scrollbar(Lb1, orient="vertical", command = canvas.yview )
        scrollbar.grid( row=0, column = 1, sticky=N+S)
        canvas.configure(yscrollcommand=scrollbar.set)  
        #canvas.create_window((4,4), window=frlogs, anchor="nw")  
        canvas.create_window((100,50), window=frlogs, anchor=tk.NW)
        frlogs.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)
        #frlogs.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
        canvas.configure(scrollregion=bbox, width=700, height=300)        
#__________________________________________________________VEIW LOGS FRAME__________________________________________________________________________________________   



    frlog = LabelFrame(result, text="View Logs", padx=10, pady=10, height=400, width=400, font=12)
    frlog.grid(row=0, column=0, padx=10, pady=10)
    
    frbill = LabelFrame(result, text="View Bills", padx=10, pady=10, height=400, width=400, font=12)
    frbill.grid(row=0, column=1, padx=10, pady=10)

    L1=Label(frlog, text="From ").grid(row=0, column=0, padx=3, pady=3)
    E1 = Entry(frlog)
    E1.grid(row=0, column=1, padx=3, pady=  3)
    L1=Label(frlog, text=" To ").grid(row=0, column=2, padx=3, pady=3)
    E2 = Entry(frlog)
    E2.grid(row=0, column=3, padx=3, pady=3)

    n = StringVar() 
    m = StringVar() 
    drop1 = ttk.Combobox(frlog, width = 30, textvariable = n) 
    drop2 = ttk.Combobox(frlog, width = 30, textvariable = m) 
    # Adding combobox drop down list 
    drop1['values'] = ('Purchase', 'Consumption', 'Production', 'Sale', 'Expenditure') 
    drop1.grid(row=1, column=0,  padx=5, pady=5, columnspan=2) 
    drop1.current()
    drop1.bind("<<ComboboxSelected>>", binddrop1)
    drop2.grid(row=1, column=2,  padx=5, pady=5, columnspan=2) 

    Bvlog = Button(frlog, text="View Logs", command=viewlistbox).grid(row=2, column=0, padx=3, pady=3)


#__________________________________________________________VEIW BILLS FRAME__________________________________________________________________________________________   

   
    L1=Label(frbill, text="From ").grid(row=0, column=0, padx=3, pady=3)
    E11 = Entry(frbill)
    E11.grid(row=0, column=1, padx=3, pady=  3)
    L1=Label(frbill, text=" To ").grid(row=0, column=2, padx=3, pady=3)
    E22 = Entry(frbill)
    E22.grid(row=0, column=3, padx=3, pady=3)

    L1=Label(frbill, text="Search For :").grid(row=1, column=0, padx=3, pady=3)    
   
    p =StringVar()
    drop3 = ttk.Combobox(frbill, width = 30, textvariable = p)
    drop3['values'] = ('Purchasing', 'Sales') 
    drop3.grid(row=1, column=1,  padx=5, pady=5, columnspan=2)
    drop3.current()
    
    Bcleared=Button(frbill, text="View Cleared Bills", command=clearedbill).grid(row=2, column=0, padx=3, pady=3)
    Bcleared=Button(frbill, text="View Pending Bills", command=pendingbill).grid(row=2, column=1, padx=3, pady=3)
    
    L1=Label(frbill, text="Search by Party:").grid(row=3, column=0, padx=3, pady=3)
    E3 = Entry(frbill)
    E3.grid(row=3, column=1, padx=3, pady=  3)
    L1=Label(frbill, text="Search by Bill").grid(row=4, column=0, padx=3, pady=3)
    E4 = Entry(frbill)
    E4.grid(row=4, column=1, padx=3, pady=3)

    BBB = Button(frbill, text="View Party Bills", command=partybills).grid(row=3, column=2, padx=3, pady=3)
    BB3B = Button(frbill, text="View Part Payments by Bill", command=billpart).grid(row=4, column=2, padx=3, pady=3)
    
    #Lb1 = Listbox(frlog, width=100)
    
#-----------------------------------------------RESULTS FRAME ENDS--------------------------------------------------------------------------------------------------------------





#-----------------------------------------------ANALYSIS FRAME STARTS--------------------------------------------------------------------------------------------------------------   

def analysis():

    newan = Toplevel()
    newan.title("Expenditure Entry")
    newan.minsize(400,300) 
    newan.iconbitmap('icov1.ico')
    def graphs():

        dfrom=E1.get()
        dto=E2.get()
        totalsalep = 0
        totalsalea = 0
        totalpurma = 0
        totalpurmp = 0
        totalexp = 0
        totalpurB = 0
        totalpurC = 0
        totalpurP = 0
        

        salelog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="newsales")
        cursorsale = salelog.cursor()

        cursorsale.execute("SELECT DISTINCT AmountT, Amount_Paid FROM paymentsales WHERE Bill_Date BETWEEN '"+dfrom+"' AND '"+dto+"'  ")
        resultsale = cursorsale.fetchall()
        amnts = [lis[0] for lis in resultsale]
        amntpd = [lis[1] for lis in resultsale]
        rcsale=len(resultsale)
        for i in range(rcsale):
            if(str(amnts[i]) =="None"):
                amnts[i]=0
            if(str(amntpd[i]) =="None"):
                amntpd[i]=0
            totalsalep = totalsalep + float(str(amnts[i]))
            totalsalea = totalsalea + float(str(amntpd[i]))

        purlog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="purchasinglog")
        cursorpur = purlog.cursor()

        cursorpur.execute("SELECT DISTINCT AmountT, Amount_Paid FROM partpaymentpurchase WHERE BIll_Date BETWEEN '"+dfrom+"' AND '"+dto+"'  ")
        resultpur = cursorpur.fetchall()
        amntpur = [lis[0] for lis in resultpur]
        amntpdpur = [lis[1] for lis in resultpur]
        rcpur=len(resultpur)
        for i in range(rcpur):
            if(str(amntpur[i]) =="None"):
                amntpur[i]=0
            if(str(amntpdpur[i]) =="None"):
                amntpdpur[i]=0
            totalpurmp = totalpurmp  + float(str(amntpur[i]))
            totalpurma = totalpurma + float(str(amntpdpur[i]))

        cursorpur.execute("SELECT DISTINCT AmountP, AmountB, AmountC FROM packingpurchase WHERE Date BETWEEN '"+dfrom+"' AND '"+dto+"'  ")
        resultpurp = cursorpur.fetchall()
        amntP = [lis[0] for lis in resultpurp]
        amntB = [lis[1] for lis in resultpurp]
        amntC = [lis[2] for lis in resultpurp]
        rcpurp=len(resultpurp)
        for i in range(rcpurp):
            if(str(amntB[i]) =="None"):
                amntB[i]=0
            if(str(amntC[i]) =="None"):
                amntC[i]=0
            if(str(amntP[i]) =="None"):
                amntP[i]=0
            totalpurB = totalpurB  + float(str(amntB[i]))
            totalpurC = totalpurC + float(str(amntC[i]))
            totalpurP = totalpurP + float(str(amntP[i]))
        totalPPpur = totalpurP + totalpurC + totalpurB

        explog = mysql.connector.connect(host="localhost",  user="root",  password="root123", database="expenditure")
        cursorx = explog.cursor()

        cursorx.execute("SELECT DISTINCT expT FROM expreg WHERE Date BETWEEN '"+dfrom+"' AND '"+dto+"'  ")
        resultx = cursorx.fetchall()
        amntx = [lis[0] for lis in resultx]
        
        rcx=len(resultx)
        for i in range(rcx):
            if(str(amntx[i]) =="None"):
                amntx[i]=0
            totalexp = totalexp  + float(str(amntx[i]))

        profitp = totalsalep - totalpurmp - totalPPpur - totalexp
        profitpp = profitp/(totalpurmp + totalPPpur + totalexp)
        profita = totalsalea - totalpurma - totalPPpur - totalexp
        profitap = profita/(totalpurma + totalPPpur + totalexp)

        LL = Label(newan, text="Projected Profit: ").grid(row=2, column=0, padx=3, pady=3)
        LL = Label(newan, text=profitp).grid(row=2, column=1, padx=3, pady=3)


        LL = Label(newan, text="Projected Profit %: ").grid(row=2, column=2, padx=3, pady=3)
        LL = Label(newan, text=profitpp).grid(row=2, column=3, padx=3, pady=3)

        LL = Label(newan, text="Actual Profit: ").grid(row=3, column=0, padx=3, pady=3)
        LL = Label(newan, text=profitp).grid(row=3, column=1, padx=3, pady=3)


        LL = Label(newan, text="Actual Profit %: ").grid(row=3, column=2, padx=3, pady=3)
        LL = Label(newan, text=profitpp).grid(row=3, column=3, padx=3, pady=3)
#__________________________________________________________VEIW Analysis FRAME__________________________________________________________________________________________

    L1=Label(newan, text="From ").grid(row=0, column=0, padx=3, pady=3)
    E1 = Entry(newan)
    E1.grid(row=0, column=1, padx=3, pady=  3)
    L1=Label(newan, text=" To ").grid(row=0, column=2, padx=3, pady=3)
    E2 = Entry(newan)
    E2.grid(row=0, column=3, padx=3, pady=3)

    BBB = Button(newan, text="View Graphs", command=graphs).grid(row=1, column=0, padx=3, pady=3)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx R O O T xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

frame1 = LabelFrame(root, text="Material Purchasing", padx=20, pady=20, bg="light pink", relief=RIDGE, height=60, width=60, font=10)
frame1.grid(row=0, column=0, padx=10, pady=10, sticky=N+E+S+W)

bpur = Button(frame1, text="Open Purchasing Entry", command=newpurchase)
bpur.grid(row=0, column=0)

frame2 = LabelFrame(root, text="Consumption and Production", padx=20, pady=20, bg="light blue", relief=RIDGE, height=60, width=60, font=10)
frame2.grid(row=0, column=1, padx=10, pady=10, sticky=N+E+S+W)

bprod = Button(frame2, text="Open Production Entry", command=newproduction)
bprod.grid(row=0, column=0)


frame3 = LabelFrame(root, text="Sales", padx=20, pady=20, bg="light green", relief=RIDGE, height=60, width=60, font=10)
frame3.grid(row=0, column=2, padx=10, pady=10, sticky=N+E+S+W)

bsale = Button(frame3, text="New Entry and Payment", command=newsales)
bsale.grid(row=0, column=0)


frame4 = LabelFrame(root, text="Expenditure Entry", padx=20, pady=20, bg="light green", relief=RIDGE, height=60, width=60, font=10)
frame4.grid(row=1, column=0, padx=10, pady=10, sticky=N+E+S+W)

bexpn = Button(frame4, text="     New Expenditures    ", command=expend)
bexpn.grid(row=0, column=0)

frame5 = LabelFrame(root, text="Results", padx=20, pady=20, bg="light blue", relief=RIDGE, height=60, width=60, font=10)
frame5.grid(row=1, column=1, padx=10, pady=10, sticky=N+E+S+W)

brslt = Button(frame5, text=" View Results and Logs ", command=results)
brslt.grid(row=0, column=0)

frame6 = LabelFrame(root, text="Analysis", padx=20, pady=20, bg="light pink", relief=RIDGE, height=60, width=60, font=10)
frame6.grid(row=1, column=2, padx=10, pady=10, sticky=N+E+S+W)

ConB = Button(root, text="Connect", command=connectmdb)
ConB.grid(row=2, column=0)    
Lab333 = Label(root, text="Test Connection").grid(row=2, column =1, sticky=N+E+S+W)

banls = Button(frame6, text="View Graphs and Analysis", command=analysis)
banls.grid(row=0, column=0, sticky=N+E+S+W)


root.mainloop()