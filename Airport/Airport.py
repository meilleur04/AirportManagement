import tkinter
from tkinter import messagebox
import webbrowser
import pymysql as sqlcon
import matplotlib.pyplot as plt 
k = tkinter.Tk()
def book():
    top=tkinter.Toplevel()
    def e():
        # to get the user input
        f=fname2.get()
        l=lname2.get()
        p=phone2.get()
        fr=flight2.get()
        i=ID2.get()
        a=age2.get()
        # to insert new data into table passenger
        myconec=sqlcon.connect(host='localhost',user='root',passwd='00000000',database='passengers')
        cursorob=myconec.cursor()
        query1="select * from flight"
        cursorob.execute(query1)
        d=cursorob.fetchall()
        Found=False
        for r in d:
            if str(r[0])==str(fr):
               query2="insert into passenger values('{}','{}','{}','{}','{}','{}')".format(str(f),str(l),str(p),str(fr),str(i),str(a))
               cursorob.execute(query2)
               myconec.commit()
               Found=True 
               break
        myconec.close()
        if Found==True:
            messagebox.showinfo("STARK INTERNATIONAL AIRPORT","flight booked")
        else:
            messagebox.showinfo("STARK INTERNATIONAL AIRPORT","flight not found")
        #clearing input fields
        fname2.delete(0,len(f))
        lname2.delete(0,len(l))
        phone2.delete(0,len(p))
        flight2.delete(0,len(fr))
        ID2.delete(0,len(i))
        age2.delete(0,len(i))
    #creating labels in tkinter
    fname1=tkinter.Label(top,text="first name")
    fname1.grid(row=0,column=0)
    lname1=tkinter.Label(top,text="last name")
    lname1.grid(row=1,column=0)
    phone1=tkinter.Label(top,text="phone number")
    phone1.grid(row=2,column=0)
    flight1=tkinter.Label(top,text="want which flight")
    flight1.grid(row=3,column=0)
    ID1=tkinter.Label(top,text="enter id")
    ID1.grid(row=4,column=0)
    age1=tkinter.Label(top,text="age")
    age1.grid(row=5,column=0)
    # creating input fields in tkinter for user to write
    fname2=tkinter.Entry(top)
    fname2.grid(row=0,column=1)
    lname2=tkinter.Entry(top)
    lname2.grid(row=1,column=1)
    phone2=tkinter.Entry(top)
    phone2.grid(row=2,column=1)
    flight2=tkinter.Entry(top)
    flight2.grid(row=3,column=1)
    ID2=tkinter.Entry(top)
    ID2.grid(row=4,column=1)
    age2=tkinter.Entry(top)
    age2.grid(row=5,column=1)
    #a submit button for user to submit data
    B=tkinter.Button(top,text="submit",command=e,padx=100)
    B.grid(row=6,column=0,columnspan=2)
    # for user to go back to main menu
    A=tkinter.Button(top,text="go back to main",padx=100,command=top.destroy)
    A.grid(row=7,column=0,columnspan=2)
def cancel():
    def CANCEL():
        # to get user input
        i=ID2.get()
        myconec=sqlcon.connect(host='localhost',user='root',passwd='00000000',database='passengers')
        cursorob=myconec.cursor()
        cursorob.execute("select * from passenger")
        data=cursorob.fetchall()
        # to check and delete the data
        for record in data:
            if str(record[4])==str(i):
                found=True
                query1="delete from passenger where identification='{}'".format(str(i))
                cursorob.execute(query1)
                myconec.commit()
                messagebox.showinfo('STARK INTERNATIONAL AIRPORT','flight canceled')
                break
            else:
                found=False
        if found==False:
            messagebox.showinfo('STARK INTERNATIONAL AIRPORT','no record found')#if data not found in table
        myconec.close()
    top=tkinter.Toplevel()
    # for user to enter the id
    ID1=tkinter.Label(top,text="enter id")
    ID1.grid(row=0,column=0)    
    ID2=tkinter.Entry(top)
    ID2.grid(row=0,column=1)
    #for user to cancel flight 
    A=tkinter.Button(top,text="cancel flight",command=CANCEL,padx=100)
    A.grid(row=1,column=0,columnspan=2)
    # for user to go back to main menu
    B=tkinter.Button(top,text="go back to main",padx=100,command=top.destroy)
def upddata():
    def ENTER():
        def UPDATE():
            # to get user input
            f=fname2.get()
            l=lname2.get()
            p=phone2.get()
            fr=flight2.get()
            a=age2.get()
            myconec=sqlcon.connect(host='localhost',user='root',passwd='00000000',database='passengers')
            cursorob=myconec.cursor()
            query2="select * from flight"
            cursorob.execute(query2)
            data1=cursorob.fetchall()
            Found=False
            # to check and update the data
            for rec1 in data1:
                if str(rec1[0])==str(fr):
                    query1="delete from passenger where identification='{}'".format(str(i))
                    cursorob.execute(query1)
                    myconec.commit()
                    query3="insert into passenger values('{}','{}','{}','{}','{}','{}')".format(str(f),str(l),str(p),str(fr),str(i),str(a))
                    cursorob.execute(query3)
                    myconec.commit()
                    messagebox.showinfo("STARK INTERNATIONAL AIRPORT","flight updated")
                    Found=True
                    break
            myconec.close()
            if Found==False:
                messagebox.showinfo("STARK INTERNATIONAL AIRPORT","flight not found")
            fname2.delete(0,len(f))
            lname2.delete(0,len(l))
            phone2.delete(0,len(p))
            flight2.delete(0,len(fr))
            ID2.delete(0,len(i))
            age2.delete(0,len(i))   
        # to find the data in existing table
        i=ID2.get()
        myconec=sqlcon.connect(host='localhost',user='root',passwd='00000000',database='passengers')
        cursorob=myconec.cursor()
        cursorob.execute("select * from passenger")
        data=cursorob.fetchall()
        for record in data:
            if str(record[4])==str(i):
                found=True
                break
            else:
                found=False
        if found==True:
            fname1=tkinter.Label(top,text="first name")
            fname1.grid(row=2,column=0)
            lname1=tkinter.Label(top,text="last name")
            lname1.grid(row=3,column=0)
            phone1=tkinter.Label(top,text="phone number")
            phone1.grid(row=4,column=0)
            flight1=tkinter.Label(top,text="flight")
            flight1.grid(row=5,column=0)
            age1=tkinter.Label(top,text="age")
            age1.grid(row=6,column=0)
            #
            fname2=tkinter.Entry(top)
            fname2.grid(row=2,column=1)
            lname2=tkinter.Entry(top)
            lname2.grid(row=3,column=1)
            phone2=tkinter.Entry(top)
            phone2.grid(row=4,column=1)
            flight2=tkinter.Entry(top)
            flight2.grid(row=5,column=1)
            age2=tkinter.Entry(top)
            age2.grid(row=6,column=1)
            C=tkinter.Button(top,text="UPDATE",command=UPDATE,padx=100)
            C.grid(row=7,column=0,columnspan=2)
        if found==False:
            ID2.delete(0,len(i))
            messagebox.showinfo("STARK INTERNATIONAL AIRPORT","no record found")
        myconec.close()
    top=tkinter.Toplevel()
    ID1=tkinter.Label(top,text="enter id")
    ID1.grid(row=0,column=0)
    ID2=tkinter.Entry(top)
    ID2.grid(row=0,column=1)
    #for user to enter id
    A=tkinter.Button(top,text="enter",command=ENTER,padx=100)
    A.grid(row=1,column=0,columnspan=2)
    # for user to enter updated data and enter
    C=tkinter.Button(top,text="UPDATE",state='disabled',padx=100)
    C.grid(row=7,column=0,columnspan=2)
    # for user to go back to main menu
    B=tkinter.Button(top,text="go back to main",command=top.destroy,padx=100)
    B.grid(row=8,column=0,columnspan=2)
def chkdata():
    def ENTER():
        i=ID2.get()
        # to check the data of booked flight
        myconec=sqlcon.connect(host='localhost',user='root',passwd='00000000',database='passengers')
        cursorob=myconec.cursor()
        query1="select * from passenger"
        cursorob.execute(query1)
        data=cursorob.fetchall()
        found=False
        for record in data:
            if record[4]==str(i):
                found=True
                query11="select * from flight where flight='{}'".format(record[3])
                cursorob.execute(query11)
                data=cursorob.fetchone()
                #
                fname1=tkinter.Label(top,text="name")
                fname1.grid(row=2,column=0)
                phone1=tkinter.Label(top,text="phone number")
                phone1.grid(row=3,column=0)
                flight1=tkinter.Label(top,text="flight")
                flight1.grid(row=4,column=0)
                age1=tkinter.Label(top,text="age")
                age1.grid(row=5,column=0)
                start1=tkinter.Label(top,text="flightfrom")
                start1.grid(row=6,column=0)
                destination1=tkinter.Label(top,text="flight to")
                destination1.grid(row=7,column=0)
                price1=tkinter.Label(top,text="price of flight(in Rs)")
                price1.grid(row=8,column=0)
                at1=tkinter.Label(top,text="flight at")
                at1.grid(row=9,column=0)
                duration1=tkinter.Label(top,text="duration")
                duration1.grid(row=10,column=0)
                date1=tkinter.Label(top,text="date of flight")
                date1.grid(row=11,column=0)
                fname2=tkinter.Label(top,text=str(record[0])+' '+str(record[1]))
                fname2.grid(row=2,column=1)
                phone2=tkinter.Label(top,text=str(record[2]))
                phone2.grid(row=3,column=1)
                flight2=tkinter.Label(top,text=str(record[3]))
                flight2.grid(row=4,column=1)
                age2=tkinter.Label(top,text=str(record[5]))
                age2.grid(row=5,column=1)
                start2=tkinter.Label(top,text=str(data[1]))
                start2.grid(row=6,column=1)
                destination2=tkinter.Label(top,text=str(data[2]))
                destination2.grid(row=7,column=1)
                price2=tkinter.Label(top,text=str(data[3]))
                price2.grid(row=8,column=1)
                at2=tkinter.Label(top,text=str(data[4][2:]+":"+data[4][0:2]))
                at2.grid(row=9,column=1)
                duration2=tkinter.Label(top,text=str(data[5][2:]+"hours"+data[5][0:2]+"minute"))
                duration2.grid(row=10,column=1)
                date2=tkinter.Label(top,text=str(data[6]))
                date2.grid(row=11,column=1)
        else:
            if found==False:
                messagebox.showinfo('STARK INTERNATIONAL AIRPORT','no record found')
    top=tkinter.Toplevel()
    ID1=tkinter.Label(top,text="enter id")
    ID1.grid(row=0,column=0)
    ID2=tkinter.Entry(top)
    ID2.grid(row=0,column=1)
    # for user to enter id
    A=tkinter.Button(top,text="enter",command=ENTER,padx=100)
    A.grid(row=1,column=0,columnspan=2)
    # for user to go back to main menu
    B=tkinter.Button(top,text="go back to main",padx=100,command=top.destroy)
    B.grid(row=12,column=0,columnspan=2)
def flight():
    def f1():
        data1 = {'AG184K':50000,'JE638B':100000,'CN294P':70000,'ZX900Q':90000,'RJ638M':60000}
        flightno = list(data1.keys())
        prices = list(data1.values())
        fig = plt.figure(figsize = (10, 5))
        plt.bar(flightno, prices, color ='maroon',width = 0.4)
        plt.xlabel("Flight number")
        plt.ylabel("Prices of different flights")
        plt.title("Flights from STARK INTERNATIONAL AIRPORT airport to New York airport in the next 2 days")
        plt.show()
    def f2():
        data2 = {'NV832P':70000,'PL192P':100000,'XF323K':120000,'QY878O':90000}
        flightno2 = list(data2.keys())
        prices2 = list(data2.values())
        fig = plt.figure(figsize = (10, 5))
        plt.bar(flightno2, prices2, color ='purple',width = 0.4)
        plt.xlabel("Flight number")
        plt.ylabel("Prices of different flights")
        plt.title("Flights from STARK INTERNATIONAL AIRPORT airport to Toronto airport in the next two days")
        plt.show()
    def f3():
        data2 = {'BD792P':40000,'LP475Z':80000,'LD009C':150000,'BC915R':55000}
        flightno2 = list(data2.keys())
        prices2 = list(data2.values())
        fig = plt.figure(figsize = (10, 5))
        plt.bar(flightno2, prices2, color ='green',width = 0.4)
        plt.xlabel("Flight number")
        plt.ylabel("Prices of different flights")
        plt.title("Flights from STARK INTERNATIONAL AIRPORT airport to London airport in the next two days")
        plt.show()
    def f4():
        data2 = {'VN238W':25000,'FN999O':100000,'KF123Z':30000,'YQ546O':40000,'MM222M':60000}
        flightno2 = list(data2.keys())
        prices2 = list(data2.values())
        fig = plt.figure(figsize = (10, 5))
        plt.bar(flightno2, prices2, color ='blue',width = 0.4)
        plt.xlabel("Flight number")
        plt.ylabel("Prices of different flights")
        plt.title("Flights from STARK INTERNATIONAL AIRPORT airport to Singapore airport")
        plt.show()
    def f5():
        data2 = {'HG911H':70000,'YR011S':40000,'ZU923M':64000}
        flightno2 = list(data2.keys())
        prices2 = list(data2.values())
        fig = plt.figure(figsize = (10, 5))
        plt.bar(flightno2, prices2, color ='yellow',width = 0.4)
        plt.xlabel("Flight number")
        plt.ylabel("Prices of different flights")
        plt.title("Flights from STARK INTERNATIONAL AIRPORT airport to Kuwait airport in the next two days")
        plt.show()
    def f6():
        data2 = {'PL980Q':10000,'ZZ118X':80000,'YY010D':12000,'HF643M':30000,'DH444Q':20000}
        flightno2 = list(data2.keys())
        prices2 = list(data2.values())
        fig = plt.figure(figsize = (10, 5))
        plt.bar(flightno2, prices2, color ='red',width = 0.4)
        plt.xlabel("Flight number")
        plt.ylabel("Prices of different flights")
        plt.title("Flights from STARK INTERNATIONAL AIRPORT airport to Mumbai airport in the next two days")
        plt.show()
    # for user to compare prices of different flight
    top=tkinter.Toplevel()
    b1=tkinter.Button(top,text="new york",command=f1,padx=75,pady=50)
    b1.grid(row=1,column=0)
    b2=tkinter.Button(top,text="Toronto",command=f2,padx=75,pady=50)
    b2.grid(row=1,column=1)
    b3=tkinter.Button(top,text="London",command=f3,padx=75,pady=50)
    b3.grid(row=2,column=0)
    b4=tkinter.Button(top,text="Singapore",command=f4,padx=75,pady=50)
    b4.grid(row=2,column=1)
    b5=tkinter.Button(top,text="Kuwait",command=f5,padx=75,pady=50)
    b5.grid(row=3,column=0)
    b6=tkinter.Button(top,text="Mumbai",command=f6,padx=75,pady=50)
    b6.grid(row=3,column=1)
    # for user to go back to main menu
    B=tkinter.Button(top,text="go back to main",command=top.destroy,padx=75,pady=50)
    B.grid(row=4,column=0,columnspan=2)  
#
def o():
    webbrowser.open(r"file:///Users/gurmannjaggi/Desktop/Airport/about.html")
kn=tkinter.Button(k,text="know about our airport",command = o, activeforeground="blue" ,padx=280,pady=50)
kn.grid(row=1,column=0,columnspan=2)
# create a label
air=tkinter.Label(k,text="Airport Management System",padx=125,bg="powder blue",pady=50,fg='white',bd=5,relief='ridge',font=("times new roman",35,"bold"))
air.grid(row=0,column=0,columnspan=2)
# creating buttons
fly=tkinter.Button(k,text="flight comparison",bg="powder blue" ,padx=120,pady=50,command= flight)
fly.grid(row=2,column=0)
#
book_flight=tkinter.Button(k,text="Book a ticket",command=book,bg="powder blue",padx=120,pady=50)
book_flight.grid(row=2,column=1)
#
update=tkinter.Button(k,text="Update your flight info",command=upddata,bg="powder blue",padx=106,pady=50)
update.grid(row=3,column=0)
#
delete=tkinter.Button(k,text="Cancel your ticket",command=cancel,bg="powder blue",padx=106,pady=50)
delete.grid(row=3,column=1)
#
check=tkinter.Button(k,text="Check/Verify your details ",command=chkdata,bg="powder blue",padx=95,pady=50)
check.grid(row=4,column=0)
#
e=tkinter.Button(k,text="exit!",padx=150,pady=50,bg="powder blue",command=quit)
e.grid(row=4,column=1)
#
k.mainloop()