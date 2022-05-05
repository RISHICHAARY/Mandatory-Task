#==================================================================IMPORT_AREA==============================================================================#
from tkinter import*
from tkinter import ttk
import random
import time
from datetime import datetime
from tkinter import messagebox
from datetime import datetime
from datetime import date
from datetime import timedelta
import mysql.connector as MC
import sqlite3
#=================================================================FILES_OPEANING============================================================================#
f2=[]
f3=[]
clsc=""
AA11=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
#=================================================================DATABASE_AREA=============================================================================#
def center_window(w=300, h=200):
    # get screen width and height
    ws = Home.winfo_screenwidth()
    hs = Home.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    Home.geometry('%dx%d+%d+%d' % (w, h, x, y))
con=sqlite3.connect('library_data.db')
curs=con.cursor()
curs1=con.cursor()
curs2=con.cursor()
k=curs.execute('PRAGMA database_list;')
a=k.fetchall()
for i in a:
    for k in i:
        if k==0:
            a=0
        else:
            if k[-15:]=='library_data.db' or k[-15:0]=='main':
                a=0
            else:
                Home=Tk()
                Home.title("MVM-Library Recorder")
                Home.configure(background="dodger blue")
                Home.geometry("500x150")
                center_window(500,150)
                Home.resizable(width=0,height=0)
                Home.overrideredirect(1)
                jik=Label(Home,font=("futura",12,"bold"),text="Getting Things Ready...(0%)",bg="dodger blue",fg="black")
                jik.pack(padx=20,pady=25)
                My_progress=ttk.Progressbar(Home,orient=HORIZONTAL,length=250,mode="determinate")
                My_progress.pack(padx=20,pady=10)
                messagebox.showinfo("Please Wait","   This May Take Few Moments \n(Please Don't minimize (or) Switch Tab)")
                My_progress['value']+=10
                jik.config(text="Getting Things Ready...(10.0%)")
                Home.update_idletasks()
                curs1.execute("create table if not exists Staff(staff_Name char(35),staff_ID varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed varchar(12),Due_Date varchar(12))")
                curs1.execute("create table if not exists Books(Book_Name varchar(35),Book_Code varchar(10),Book_Gener varchar(100),Book_Author char(25))")
                curs1.execute("create table if not exists Accounts(user_name varchar(25),password varchar(25))")
                curs2.execute("create table if not exists Theme(Mode char(1))")
                curs2.execute("create table if not exists Resolution(Size char(1))")
                curs2.execute("create table if not exists Remem(User char(25),Pass varchar(25),Rd char(1))")
                con.commit()
                My_progress['value']+=20
                jik.config(text="Getting Things Ready...(30.0%)")
                Home.update_idletasks()
                a=30
                for isec in AA11:
                            a=a+3.5
                            curs2.execute("create table if not exists {}5(Name char(35),Roll_No varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed date,Due_Date date)".format(isec))
                            curs1.execute("create table if not exists {}6(Name char(35),Roll_No varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed date,Due_Date date)".format(isec))
                            curs2.execute("create table if not exists {}7(Name char(35),Roll_No varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed date,Due_Date date)".format(isec))
                            curs1.execute("create table if not exists {}8(Name char(35),Roll_No varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed date,Due_Date date)".format(isec))
                            curs2.execute("create table if not exists {}9(Name char(35),Roll_No varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed date,Due_Date date)".format(isec))
                            curs.execute("create table if not exists {}10(Name char(35),Roll_No varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed date,Due_Date date)".format(isec))
                            curs1.execute("create table if not exists {}11(Name char(35),Roll_No varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed date,Due_Date date)".format(isec))
                            curs2.execute("create table if not exists {}12(Name char(35),Roll_No varchar(15),Book_Name char(35),Book_Code varchar(10),Book_Gener char(100),Book_Author char(25),Date_Borrowed date,Due_Date date)".format(isec))
                            con.commit()
                            My_progress['value']+=3.5
                            jik.config(text="Getting Things Ready...("+str(a)+"%)")
                            Home.update_idletasks()
                time.sleep(1)
                Home.destroy()
                Home.mainloop()
#===============================================================SETTINGS_FRONTEND===========================================================================#
def Settings(A,X,Y):
        curs.execute("select * from Theme")
        theme=curs.fetchall()
        curs1.execute("select * from Remem")
        Remacc=curs1.fetchall()
        curs.execute("select * from Resolution")
        Resol=curs.fetchall()
        #Main_Window
        Home=Tk()
        Home.title("MVM-Library Recorder")
        Home.configure(background="black")
        Home.resizable(width=0,height=0)
        #Frames
        Main=Frame(Home, width=1265,bd=10,relief=RIDGE,bg=X)
        Main.pack(side=TOP)
        Title=Frame(Main, width=1265,padx='5',pady='5',bd=0,relief=RIDGE,bg=X)
        Title.pack(side=TOP)
        Full=Frame(Main, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Full.pack(side=TOP)
        #Pros_&B_uttons
        JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y).pack()
        Head=Label(Title,font=("futura",25,"bold"),text="MAHARISHI VIDYA MANDIR",bg=X,fg=Y).pack()
        HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y).pack()
        JGD1=Label(Full,font=("futura",12,"bold"),text="Add A Sign_In Account : ",bg=X,fg=Y).grid(row=0,column=0,sticky=W)
        JGD3=Label(Full,font=("futura",12,"bold"),text="Dark Mode : ",bg=X,fg=Y).grid(row=2,column=0,sticky=W)
        JGD4=Label(Full,font=("futura",12,"bold"),text="View Books : ",bg=X,fg=Y).grid(row=1,column=0,sticky=W)
        JGD5=Label(Full,font=("futura",12,"bold"),text="Remember Me : ",bg=X,fg=Y).grid(row=0,column=3,sticky=W)
        JGD6=Label(Full,font=("futura",12,"bold"),text="Set Resolution to : ",bg=X,fg=Y).grid(row=3,column=0,sticky=W)
        b=[]
        if(Resol==[]):
            Resolch=Button(Full,text="1268x780",font=("futura",12,"bold"),command=lambda:[Resoled(X,Y)])
            Resolch.grid(row=3,column=1,padx='5',pady='5',sticky="nesw")
        else:
            Resolch=Button(Full,text="1920x1020",font=("futura",12,"bold"),command=lambda:[Resoled1(X,Y)])
            Resolch.grid(row=3,column=1,padx='5',pady='5',sticky="nesw")
        if(Remacc!=b):
            JGD6=Label(Full,font=("futura",12,"bold"),text="Forget Me : ",bg=X,fg=Y).grid(row=1,column=3,sticky=W)
        Add_Acc=Button(Full,text="ADD",font=("futura",12,"bold"),command=lambda:[Sign_up(X,Y)])
        Add_Acc.grid(row=0,column=1,padx='5',pady='5',sticky="nesw")
        Facres=Button(Full,text="Reset",font=("futura",12,"bold"),command=lambda:[Facres(A,Home,X,Y)])
        if(Remacc==b):
                    Rem=Button(Full,text="ADD",font=("futura",12,"bold"),command=lambda:[Home.destroy(),Rem(X,Y)])
                    Rem.grid(row=0,column=4,padx='5',pady='5',sticky="nesw")
                    JGD6=Label(Full,font=("futura",12,"bold"),text="Factory Reset : ",bg=X,fg=Y).grid(row=1,column=3,sticky=W)
                    Facres.grid(row=1,column=4,padx='5',pady='5',sticky="nesw")
        else:
            Rem=Button(Full,text="Change",font=("futura",12,"bold"),command=lambda:[Rem(X,Y)])
            Rem.grid(row=0,column=4,padx='5',pady='5',sticky="nesw")
            Remcancel=Button(Full,text="Forget",font=("futura",12,"bold"),command=lambda:[Home.destroy7(),Remcan(X,Y)])
            Remcancel.grid(row=1,column=4,padx='5',pady='5',sticky="nesw")
            JGD6=Label(Full,font=("futura",12,"bold"),text="Factory Reset : ",bg=X,fg=Y).grid(row=2,column=3,sticky=W)
            Facres.grid(row=2,column=4,padx='5',pady='5',sticky="nesw")
        if(theme==[]):
            Dark=Button(Full,text="Turn ON",font=("futura",12,"bold"),command=lambda:[dark(A)])
        else:
            Dark=Button(Full,text="Turn OFF",font=("futura",12,"bold"),command=lambda:[dark1(A)])
        Dark.grid(row=2,column=1,padx='5',pady='5',sticky="nesw")
        Dark1=Button(Full,text="View",font=("futura",12,"bold"),command=lambda:[View(X,Y)])
        Dark1.grid(row=1,column=1,padx='5',pady='5',sticky="nesw")
#================================================================SETTINGS_BACKEND===========================================================================#
        def dark(A):
                curs.execute("insert into Theme values('D')")
                con.commit()
                messagebox.showinfo("NOTE","THEME WILL BE APPLIED ONCE WHEN YOU RESTART")
                ins=messagebox.askyesno("HELP","DO YOU WANT TO RESTART NOW")
                if(ins>0):
                    A.destroy()
                    Home.quit()
                    Execution()
        def dark1(A):
                curs.execute("delete from Theme where Mode='D'")
                con.commit()
                messagebox.showinfo("NOTE","CHANGES WILL BE APPLIED ONCE WHEN YOU RESTART")
                ins=messagebox.askyesno("HELP","DO YOU WANT TO RESTART NOW")
                if(ins>0):
                    A.destroy()
                    Home.destroy()
                    Execution()
        def View(X,Y):
                #Main_Window
                Home=Tk()
                Home.title("MVM-Library Recorder")
                Home.configure(background="black")
                Home.eval('tk::PlaceWindow . center')
                #Frames
                Main=Frame(Home, width=1265,bd=10,bg=X,relief=RIDGE)
                Main.pack(side=TOP)
                due=Frame(Main,width=1265,height=100,padx=65,pady=5,bd=10,bg=X,relief=RIDGE)
                due.pack()
                JGD4=Label(due,font=("futura",10,"bold"),text="Book Name:",bg=X,fg=Y).grid(row=0,column=0)
                JGD5=Label(due,font=("futura",10,"bold"),text="Book Code:",bg=X,fg=Y).grid(row=0,column=1)
                JGD6=Label(due,font=("futura",10,"bold"),text="Book Gener:",bg=X,fg=Y).grid(row=0,column=3)
                JGD7=Label(due,font=("futura",10,"bold"),text="Book Author:",bg=X,fg=Y).grid(row=0,column=2)
                DisplayR111=Text(due,font=('futura',12,'bold'),width=25)
                DisplayR111.grid(row=1,column=0)
                DisplayR11=Text(due,font=('futura',12,'bold'),width=10)
                DisplayR11.grid(row=1,column=1)
                DisplayR21=Text(due,font=('futura',12,'bold'),width=23)
                DisplayR21.grid(row=1,column=2)
                DisplayR31=Text(due,font=('futura',12,'bold'),width=35)
                DisplayR31.grid(row=1,column=3)
                curs.execute("select * from Books")
                ak=[]
                iret=curs.fetchall()
                for ic in range(len(iret)):
                        lk=str(iret[ic][0])
                        lk1=str(iret[ic][1])
                        lk2=str(iret[ic][2])
                        lk3=str(iret[ic][3])
                        pk=[lk,lk1,lk2,lk3]
                        ak=ak+pk
                for jkl in range(0,len(ak),4):
                        DisplayR111.insert(END,ak[jkl]+"\n")
                        DisplayR11.insert(END,ak[jkl+1]+"\n")
                        DisplayR21.insert(END,ak[jkl+2]+"\n") 
                        DisplayR31.insert(END,ak[jkl+3]+"\n")
                Home.mainloop()
        def Rem(X,Y):
            ins=messagebox.askyesno("WARNING","This Could Make You Less Secure")
            if(ins>0):
                wind11=Tk()
                wind11.title("MVM-Library Recorder")
                wind11.resizable(width=0,height=0)
                Main=Frame(wind11, width=1265,bd=10,bg=X,relief=RIDGE)
                Main.pack(side=TOP)
                Title=Frame(Main, width=1265,padx='5',pady='5',bd=0,relief=RIDGE,bg=X)
                Title.pack(side=TOP)
                Full=Frame(Main, width=1265,padx='5',pady='5',bd=5,relief=RIDGE,bg=X)
                Full.pack(side=TOP)
                msd=Label(Full,font=("futura",15,"bold"),text="Enter Account To Remember",bg=X,fg=Y).pack()
                Entr=Frame(Full, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
                Entr.pack()
                Butt=Frame(Full,width=1265,height=100,padx=5,pady=5,bd=10,relief=RIDGE,bg=X)
                Butt.pack()
                JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y).pack()
                Head=Label(Title,font=("futura",25,"bold"),text="MAHARISHI VIDYA MANDIR",bg=X,fg=Y).pack()
                HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y).pack()
                user=Label(Entr,font=("futura",12,"bold"),text="UserName:",bg=X,fg=Y).grid(row=0,column=0,sticky=W)
                pas=Label(Entr,font=("futura",12,"bold"),text="Password:",bg=X,fg=Y).grid(row=1,column=0,sticky=W)
                user12=Entry(Entr,font=("futura",19,"bold"),width="25",bd=2)
                user12.grid(row=0,column=1)
                pas12=Entry(Entr,font=("futura",19,"bold"),width="25",bd=2,show="*")
                pas12.grid(row=1,column=1)
                lg=Button(Butt,text="ADD",font=("futura",12,"bold"),command=lambda:[Elsup(),wind11.destroy()])
                lg.pack(side=RIGHT)
                def Elsup():
                    A111=user12.get()
                    B111=pas12.get()
                    b=curs1.execute("select * from accounts")
                    d=b.fetchall()
                    for i in range(0,len(d)):
                        if(d[i][0]==A111 and d[i][1]==B111):
                            curs.execute("insert into Remem (user,pass,Rd) values('{}','{}','D')".format(A111,B111))
                            con.commit()
                            messagebox.showinfo("Success","Account Remembered Successfully")
                            break
                        elif(A111==""and B111==""):
                                    messagebox.showinfo("ERROR!!!","Please Enter A Valid Account")
                                    break
                        else:
                            if(i==len(d)-1):
                                messagebox.showinfo("ERROR!!!","Please Enter A Valid Account")
                wind11.mainloop()
        def Remcan(X,Y):
            ins=messagebox.askyesno("WARNING","Do Want To Forget Your Default Login")
            if(ins>0):
                curs1.execute("delete from Remem where Rd='D'")
                con.commit()
                messagebox.showinfo("Success","Account Forgot Successfully")
        def Resoled(X,Y):
            curs.execute("insert into Resolution values('D')")
            con.commit()
            messagebox.showinfo("NOTE","CHANGES WILL BE APPLIED ONCE WHEN YOU RESTART")
            ins=messagebox.askyesno("WARNING","DO YOU WANT TO RESTART NOW")
            if(ins>0):
                A.destroy()
                Home.destroy()
                Execution()
        def Resoled1(X,Y):
            curs.execute("delete from Resolution where Size='D'")
            con.commit()
            messagebox.showinfo("NOTE","CHANGES WILL BE APPLIED ONCE WHEN YOU RESTART")
            ins=messagebox.askyesno("WARNING","DO YOU WANT TO RESTART NOW")
            if(ins>0):
                A.destroy()
                Home.destroy()
                Execution()
        def Facres(A,B,X,Y):
            def center_window(w=300, h=200):
                # get screen width and height
                ws = Home.winfo_screenwidth()
                hs = Home.winfo_screenheight()
                # calculate position x, y
                x = (ws/2) - (w/2)    
                y = (hs/2) - (h/2)
                Home.geometry('%dx%d+%d+%d' % (w, h, x, y))
            ins=messagebox.askyesno("INFO","This Will Erase All Your Data And Reset This Application")
            if(ins>0):
                B.destroy()
                A.destroy()
                Home=Tk()
                Home.title("MVM-Library Recorder")
                Home.configure(background="dodger blue")
                Home.geometry("500x150")
                center_window(500,150)
                Home.resizable(width=0,height=0)
                Home.overrideredirect(1)
                jik=Label(Home,font=("futura",12,"bold"),text="Initilizing Reset...(0.0%)",bg="dodger blue",fg="black")
                jik.pack(padx=20,pady=25)
                My_progress=ttk.Progressbar(Home,orient=HORIZONTAL,length=250,mode="determinate")
                My_progress.pack(padx=20,pady=10)
                messagebox.showinfo("Please Wait","   This May Take Few Moments \n(Please Don't minimize (or) Switch Tab)")
                curs1.execute("drop table Staff")
                curs1.execute("drop table Books")
                curs1.execute("drop table accounts")
                curs1.execute("drop table Theme")
                curs1.execute("drop table Resolution")
                curs1.execute("drop table Remem")
                con.commit()
                My_progress['value']+=10
                jik.config(text="Removing Data...(10.0%)")
                Home.update_idletasks()
                a=10
                for isec in AA11:
                            a=a+3.5
                            curs2.execute("drop table {}5".format(isec))
                            curs1.execute("drop table {}6".format(isec))
                            curs2.execute("drop table {}7".format(isec))
                            curs1.execute("drop table {}8".format(isec))
                            curs2.execute("drop table {}9".format(isec))
                            curs.execute("drop table {}10".format(isec))
                            curs1.execute("drop table {}11".format(isec))
                            curs2.execute("drop table {}12".format(isec))
                            con.commit()
                            My_progress['value']+=3.5
                            jik.config(text="Removing Databases...("+str(a)+"%)")
                            Home.update_idletasks()
                con.commit()
                My_progress['value']+=10
                jik.config(text="Clearing Files...(90%)")
                Home.update_idletasks()
                Remfl=open("Rem.txt","w")
                a99=open("User.txt","w")
                a999=open("Pass.txt","w")
                a33=open("Dark.txt","w")
                My_progress['value']+=10
                jik.config(text="Removing Final Traces...(100.0%)")
                Home.update_idletasks()
                time.sleep(5)
                Home.destroy()
                messagebox.showinfo("INFO","Factory Reset Successful"+"\n""Start This Application Mannualy")
                Home.mainloop()
        Home.mainloop()
#=========================================================ACCESSVERIFICATION_FRONTEND=======================================================================#
def Acess_verification(X,Y):
    def center_window(w=300, h=200):
        # get screen width and height
        ws = wind11.winfo_screenwidth()
        hs = wind11.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        wind11.geometry('%dx%d+%d+%d' % (w, h, x, y))
    b34=curs.execute("select * from Remem")
    b=b34.fetchall()
    b1=curs1.execute("select * from accounts")
    d=b1.fetchall()
    #print(d)
    if(d==[]):
        Sign_up(X,Y)
    else:
        wind11=Tk()
        wind11.title("MVM-Library Recorder")
        wind11.resizable(width=0,height=0)
        wind11.overrideredirect(1)
        center_window(475,425)
        Main=Frame(wind11, width=1265,bd=10,bg=X,relief=RIDGE)
        Main.pack(side=TOP)
        Title=Frame(Main, width=1265,padx='5',pady='5',bd=0,relief=RIDGE,bg=X)
        Title.pack(side=TOP)
        Full=Frame(Main, width=1265,padx='5',pady='5',relief=RIDGE,bg=X)
        Full.pack(side=TOP)
        Entr=Frame(Full, width=1265,padx='90',pady='5',bd=10,relief=RIDGE,bg=X)
        Entr.pack(padx=5,pady=15)
        JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
        JGD.pack()
        Head=Label(Title,font=("futura",25,"bold"),text="MAHARISHI VIDYA MANDIR",bg=X,fg=Y)
        Head.pack()
        HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y)
        HSR.pack()
        user=Label(Entr,font=("futura",12,"bold"),text="USER NAME:",bg=X,fg=Y)
        user.pack(padx='5',pady='5')
        user1=Entry(Entr,font=("futura",19,"bold"),width="15",bd=2)
        user1.pack()
        pas=Label(Entr,font=("futura",12,"bold"),text="PASSWORD:",bg=X,fg=Y)
        pas.pack(padx='5',pady='5')
        pas1=Entry(Entr,font=("futura",19,"bold"),width="15",bd=2,show="*")
        pas1.pack()
        if(b==[]):
            pass
        else:
            user1.insert(END,b[0][0])
            pas1.insert(END,b[0][1])
        user11=user1.get()
        pas11=pas1.get()
        Butt=Frame(Entr,width=1265,height=100,padx=5,pady=5,bd=10,relief=RIDGE,bg=X)
        Butt.pack(padx=5,pady=15)
        gi=Button(Butt,text="Sign In",font=("futura",12,"bold"),command=lambda:[wind11.destroy(),Sign_in(user11,pas11,X,Y)])
        gi.pack(side=LEFT)
        lg=Button(Butt,text="Sign up",font=("futura",12,"bold"),command=lambda:[Sign_up(X,Y)])
        lg.pack(side=RIGHT)
        wind11.mainloop()
#=============================================================STUDENT_&_STAFF_RECORD_FRONTEND===============================================================#
def Students2(x,y,z,X,Y):
    curs.execute("select * from Resolution")
    Resol=curs.fetchall()
    b=[]
    if(Resol==b):
        def center_window(w=300, h=200):
            # get screen width and height
            ws = Home2.winfo_screenwidth()
            hs = Home2.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            Home2.geometry('%dx%d+%d+%d' % (w, h, x, y))
        #Main_Window
        Home2=Tk()
        Home2.title("MVM-Library Recorder")
        Home2.overrideredirect(1)
        center_window(1550,860)
        Home2.geometry()
        #Frames
        Main=Frame(Home2, width=1265,bd=10,padx='36',pady='10',bg=X,relief=RIDGE)
        Main.pack(side=TOP)
        Title=Frame(Main, width=1265,padx='5',pady='5',bd=0,bg=X,relief=RIDGE)
        Title.pack(side=TOP)
        Title1=Frame(Main, width=1265,padx='5',pady='5',bd=10,bg=X,relief=RIDGE)
        Title1.pack(side=TOP)
        Title11=Frame(Title1, width=1265,padx='5',pady='5',bd=10,bg=X,relief=RIDGE)
        Title11.grid(row=0,column=5,padx='2',pady='5')
        Time=Frame(Title1, width=1265,padx='5',pady='5',bd=10,bg=X,relief=RIDGE)
        Time.grid(row=0,column=0,padx='5',pady='5')
        Secinf=Frame(Title1, width=1265,padx='5',pady='5',bd=10,bg=X,relief=RIDGE)
        Secinf.grid(row=0,column=7,padx='5',pady='5')
        Content=Frame(Main,width=1265,padx='10',pady='5',bd=10,bg=X,relief=RIDGE)
        Content.pack(padx='5',pady='5')
        BroInf=LabelFrame(Content,text="FILL THE INFORMATION'S",font=("futura",10),width=300,padx='5',pady='10',bd=5,bg=X,fg=Y,relief=RIDGE)
        BroInf.pack(side=LEFT)
        BookSlc=LabelFrame(Content,text="SELECT BOOK",font=("futura",10),width=300,height=200,padx='5',pady='5',bd=5,bg=X,fg=Y,relief=RIDGE)
        BookSlc.pack(side=LEFT)
        BookInf=LabelFrame(Content,text="SELECT TO EXPAND",font=("futura",10),width=300,height=200,padx='5',pady='5',bd=5,bg=X,fg=Y,relief=RIDGE)
        BookInf.pack(side=LEFT)
        Details=LabelFrame(Content,text="DETAILS",font=("futura",10),width=300,height=175,padx=5,pady=2,bd=5,bg=X,fg=Y,relief=RIDGE)
        Details.pack(side=LEFT)
        srch=LabelFrame(Content,text="FIND YOUR REQUIREMENTS",font=("futura",10),width=1265,padx='5',pady='23',bd=5,bg=X,fg=Y,relief=RIDGE)
        srch.pack(side=RIGHT)
        if(x=="Staff"):
            srcha=LabelFrame(srch,text="SEARCH STAFF IN DATA",font=("futura",10),width=1265,padx='5',pady='5',bd=5,bg=X,fg=Y,relief=RIDGE)
            srcha.pack(side=TOP)
        else:
            srcha=LabelFrame(srch,text="SEARCH STUDENT IN THIS SECTION",font=("futura",10),width=1265,padx='5',pady='5',bd=5,bg=X,fg=Y,relief=RIDGE)
            srcha.pack(side=TOP)
        srchb=LabelFrame(srch,text="SEARCH BOOKS IN LIBRARY",font=("futura",10),width=1265,padx='5',pady='4',bd=5,bg=X,fg=Y,relief=RIDGE)
        srchb.pack(side=BOTTOM)
        due=Frame(Main,width=1265,height=100,padx=35,pady=5,bd=10,bg=X,relief=RIDGE)
        due.pack()
        Butt=Frame(Main,width=1265,height=100,bd=12,bg=X,relief=RIDGE)
        Butt.pack(pady=5)
        #Pros
        de=date.today()
        fg=de.strftime("%Y-%m-%d")
        fg2=de.strftime("%d/%m/%Y")
        gt=fg2.split("/")
        aq=datetime(int(gt[2]),int(gt[1]),int(gt[0]))
        for i in range(0,7):
            aq=aq+timedelta(days=1)
        aq=aq.strftime("%Y-%m-%d")
        kgf=Label(Time,font=("futura",19,"bold"),text="Date:"+fg,fg=Y,bg=X)
        kgf.grid(row=0,column=0,sticky=W)
        li=datetime.now()
        vy=li.strftime("%I:%M %p")
        kgf1=Label(Time,font=("futura",19,"bold"),text="Time:"+vy,bg=X,fg=Y)
        kgf1.grid(row=1,column=0,sticky=W)
        if(x=="Staff"):
            si=Label(Secinf,font=("futura",19,"bold"),text="          "+x+"       ",bg=X,fg=Y)
            si.grid(row=0,column=1,sticky=W)
            si1=Label(Secinf,font=("futura",19,"bold"),text="         "+y+"   ",bg=X,fg=Y)
            si1.grid(row=1,column=1,sticky=W)
        else:
            si=Label(Secinf,font=("futura",15,"bold"),text="Class:"+"\t"+x+"\t",bg=X,fg=Y,pady=3)
            si.grid(row=0,column=11,sticky=W)
            si1=Label(Secinf,font=("futura",15,"bold"),text="Sec:"+"\t"+y+"\t",bg=X,fg=Y,pady=3)
            si1.grid(row=1,column=11,sticky=W)
        si11=Label(Title11,font=("futura",28,"bold"),text="                         Library Data Recorder        \t",bg=X,fg=Y)
        si11.grid(row=1,column=11,sticky=W,padx=10,pady=10)
        JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
        JGD.pack()
        Head=Label(Title,font=("futura",35,"bold"),text="             MAHARISHI VIDYA MANDIR          ",bg=X,fg=Y)
        Head.pack()
        HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y)
        HSR.pack()
        BookName=Label(BroInf,text="Book Name:",font=("futura",14,"bold"),bg=X,fg=Y)
        BookName.grid(row=2,column=0,sticky=W)
        BookName1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
        BookName1.grid(row=2,column=1)
        BookCode=Label(BroInf,text="Book Code:",font=("futura",14,"bold"),bg=X,fg=Y)
        BookCode.grid(row=3,column=0,sticky=W)
        BookCode1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
        BookCode1.grid(row=3,column=1)
        Cata=Label(BroInf,text="Book Genre:",font=("futura",14,"bold"),bg=X,fg=Y)
        Cata.grid(row=4,column=0,sticky=W)
        Cata1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
        Cata1.grid(row=4,column=1)
        Srch=Label(srcha,text="Name:",font=("futura",10,"bold"),fg=Y,bg=X)
        Srch.grid(row=0,column=0,sticky=W)
        Srch1=Entry(srcha,font=("futura",10,"bold"),width="25",bd=2)
        Srch1.grid(row=1,column=0)
        Srch11=Button(srcha,text="Search",font=("futura",8,"bold"),command=lambda:[srchn()])
        Srch11.grid(row=1,column=1)
        Srch12=Label(srchb,text="Book Name:",font=("futura",10,"bold"),bg=X,fg=Y).grid(row=0,column=0,sticky=W)
        Srch112=Entry(srchb,font=("futura",10,"bold"),width="25",bd=2)
        Srch112.grid(row=1,column=0)
        Srch1112=Button(srchb,text="Search",font=("futura",8,"bold"),command=lambda:[srchn1()])
        Srch1112.grid(row=1,column=1)
        if(x=="Staff"):
            RollNo=Label(BroInf,text="Staff ID:",font=("futura",14,"bold"),bg=X,fg=Y)
            RollNo.grid(row=1,column=0,sticky=W)
            RollNo1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
            RollNo1.grid(row=1,column=1)
        else:
            RollNo=Label(BroInf,text="RollNo:",font=("futura",14,"bold"),bg=X,fg=Y)
            RollNo.grid(row=1,column=0,sticky=W)
            RollNo1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
            RollNo1.grid(row=1,column=1)
        if(x=="Staff"):
             Name=Label(BroInf,text="Staff Name:",font=("futura",14,"bold"),bg=X,fg=Y)
             Name.grid(row=0,column=0,sticky=W,)
             Name1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
             Name1.grid(row=0,column=1)
        else:
            Name=Label(BroInf,text="Name:",font=("futura",14,"bold"),bg=X,fg=Y)
            Name.grid(row=0,column=0,sticky=W,)
            Name1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
            Name1.grid(row=0,column=1)
        DateBorrowed=Label(BroInf,text="Date Borrowed:",font=("futura",14,"bold"),bg=X,fg=Y)
        DateBorrowed.grid(row=6,column=0,sticky=W)
        DateBorrowed1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
        DateBorrowed1.grid(row=6,column=1)
        DateBorrowed1.insert(END,fg)
        DatesLoan=Label(BroInf,text="Book Author:",font=("futura",14,"bold"),bg=X,fg=Y)
        DatesLoan.grid(row=5,column=0,sticky=W)
        DatesLoan1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
        DatesLoan1.grid(row=5,column=1)
        DueDate=Label(BroInf,text="Due Date:",font=("futura",14,"bold"),bg=X,fg=Y)
        DueDate.grid(row=7,column=0,sticky=W)
        DueDate1=Entry(BroInf,font=("futura",14,"bold"),width="25",bd=2)
        DueDate1.grid(row=7,column=1)
        DueDate1.insert(END,aq)
        DisplayR=Text(Details,font=('arial',12,'bold'),width=23,height=13)
        DisplayR.grid(row=0,column=1)
        JGD2=Label(due,font=("futura",10,"bold"),text="Name:",bg=X,fg=Y)
        JGD2.grid(row=0,column=1)
        JGD3=Label(due,font=("futura",10,"bold"),text="Roll No:",bg=X,fg=Y)
        JGD3.grid(row=0,column=2)
        JGD4=Label(due,font=("futura",10,"bold"),text="Book Name:",bg=X,fg=Y)
        JGD4.grid(row=0,column=3)
        JGD5=Label(due,font=("futura",10,"bold"),text="Book Code:",bg=X,fg=Y)
        JGD5.grid(row=0,column=4)
        JGD6=Label(due,font=("futura",10,"bold"),text="Book Gener:",bg=X,fg=Y)
        JGD6.grid(row=0,column=5)
        JGD7=Label(due,font=("futura",10,"bold"),text="Book Author:",bg=X,fg=Y)
        JGD7.grid(row=0,column=6)
        JGD8=Label(due,font=("futura",10,"bold"),text="Date Borrowed:",bg=X,fg=Y)
        JGD8.grid(row=0,column=7)
        JGD9=Label(due,font=("futura",10,"bold"),text="Due Date:",bg=X,fg=Y)
        JGD9.grid(row=0,column=8)
        JGD10=Label(due,font=("futura",18,"bold"),text="Today's Due:  ",bg=X,fg=Y)
        JGD10.grid(row=1,column=0)
        DisplayR111=Text(due,font=('futura',12,'bold'),width=23,height=2)
        DisplayR111.grid(row=1,column=1)
        DisplayR11=Text(due,font=('futura',12,'bold'),width=10,height=2)
        DisplayR11.grid(row=1,column=2)
        DisplayR21=Text(due,font=('futura',12,'bold'),width=23,height=2)
        DisplayR21.grid(row=1,column=3)
        DisplayR31=Text(due,font=('futura',12,'bold'),width=10,height=2)
        DisplayR31.grid(row=1,column=4)
        DisplayR41=Text(due,font=('futura',12,'bold'),width=15,height=2)
        DisplayR41.grid(row=1,column=5)
        DisplayR51=Text(due,font=('futura',12,'bold'),width=25,height=2)
        DisplayR51.grid(row=1,column=6)
        DisplayR61=Text(due,font=('futura',12,'bold'),width=11,height=2)
        DisplayR61.grid(row=1,column=7)
        DisplayR71=Text(due,font=('futura',12,'bold'),width=11,height=2)
        DisplayR71.grid(row=1,column=8)
        add=Button(Butt,text="ADD",font=("futura",19,"bold"),padx=5,pady=5,bd=5,command=lambda:[sad(),Home2.destroy(),Students2(x,y,z,X,Y)])
        add.grid(row=0,column=0,padx='5',pady='5')
        go=Button(Butt,text="SETTINGS",font=("futura",19,"bold"),padx=5,pady=5,bd=5,command=lambda:[Settings(Home2,X,Y)])
        go.grid(row=0,column=40,padx='5',pady='5')
        delete=Button(Butt,text="REMOVE",font=("futura",19,"bold"),padx=5,pady=5,bd=5,command=lambda:[clear(),Home2.destroy(),Students2(x,y,z,X,Y)])
        delete.grid(row=0,column=1,padx='5',pady='5')
        fst1=Button(Butt,text="ADD BOOK",font=("futura",19,"bold"),padx=5,pady=5,bd=5,command=lambda:[Books(X,Y)])
        fst1.grid(row=0,column=11,padx='5',pady='5')
        exi=Button(Butt,text="QUIT",font=("futura",19,"bold"),padx=5,pady=5,bd=5,bg="red",command=lambda:[qui()])
        exi.grid(row=0,column=500,padx='5',pady='5')
        fst=Button(Butt,text="GO BACK",font=("futura",19,"bold"),padx=5,pady=5,bd=5,bg="blue",command=lambda:[Home2.destory(),Login_selection2(X,Y)])
        fst.grid(row=0,column=400,padx='5',pady='5')
    #============================================================STUDENT_&_STAFF_RECORD_BACKEND=================================================================#
        def sad():
            a=Name1.get()
            aa=BookName1.get()
            bb=BookCode1.get()
            cc=RollNo1.get()
            dd=DateBorrowed1.get()
            ee=Cata1.get()
            ff=DueDate1.get()
            gg=DatesLoan1.get()
            ad=str(aa)
            bd=str(bb)
            cd=str(cc)
            dd=str(dd)
            ed=str(ee)
            fd=str(ff)
            gd=str(gg)
            w=str(a)
            if(len(w)>25):
                if(x=="Staff"):
                    messagebox.showinfo("Error!!!","Staff Name Entered Is To Long(MAX-25 Characters)")
                else:
                    messagebox.showinfo("Error!!!","Name Entered Is To Long(MAX-25 Characters)")
            elif(len(cd)>10):
                if(x=="Staff"):
                    messagebox.showinfo("Error!!!","Staff ID Entered Is To Long(MAX-10 Characters)")
                else:
                    messagebox.showinfo("Error!!!","Roll No Entered Is To Long(MAX-10 Characters)")
            else:
                if(x=="Staff"):
                    curs1.execute("insert into Staff values('{}','{}','{}','{}','{}','{}','{}','{}')".format(w,cd,ad,bd,ed,gd,dd,fd))
                    con.commit()
                else:
                    curs1.execute("insert into {} values('{}','{}','{}','{}','{}','{}','{}','{}')".format(z,w,cd,ad,bd,ed,gd,dd,fd))
                    con.commit()
        def qui():
            exiit=messagebox.askyesno("EXIT","ARE YOU SURE YOU WANT TO QUIT")
            if(exiit>0):
                Home2.destroy()
        def clear():
            ins=messagebox.askyesno("WARNING","DO YOU WANT TO REMOVE THIS STUDENT DATA")
            if(ins>0):
                if(x=="Staff"):
                    curs1.execute("select staff_Name from Staff")
                else:
                    curs1.execute("select Name from {}".format(z))
                iret=curs1.fetchall()
                kret=[]
                for ic in range(len(iret)):
                        lk=str(iret[ic][0])
                        pk=[lk]
                        kret=kret+pk
            value=str(booklist.get(booklist.curselection()))
            gf=value
            for i in range(0,len(kret)):
                    if(gf==kret[i]):
                        if(x=="Staff"):
                            curs1.execute("delete from Staff where staff_Name='{}'".format(gf))
                            con.commit()
                        else:
                            curs1.execute("delete from {} where Name='{}'".format(z,gf))
                            con.commit()
        def ret(evt):
            DisplayR.delete(1.0,END)
            if(x=="Staff"):
                curs1.execute("select staff_name from Staff")
            else:
                curs1.execute("select name from {}".format(z))
            iret=curs1.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            value=str(booklist.get(booklist.curselection()))
            gf=value
            for i in range(0,len(kret)):
                if(gf==kret[i]):
                    if(x=="Staff"):
                        curs1.execute("select * from Staff where staff_Name like '{}'".format(kret[i]))
                    else:
                        curs1.execute("select * from {} where name like '{}'".format(z,kret[i]))
                    iret1=curs1.fetchall()
                    kret1=[]
                    for ic in range(len(iret1)):
                        lk=str(iret1[ic][0])
                        lk1=str(iret1[ic][1])
                        lk2=str(iret1[ic][2])
                        lk3=str(iret1[ic][3])
                        lk4=str(iret1[ic][4])
                        lk5=str(iret1[ic][5])
                        lk6=str(iret1[ic][6])
                        lk7=str(iret1[ic][7])
                        pk=[lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                        kret1=kret1+pk
                    for jkl in range(len(kret1)):
                        if(jkl==(0)):
                            if(x=="Staff"):
                                DisplayR.insert(END,"Staff Name:"+kret1[0])
                            else:
                                DisplayR.insert(END,"Name:"+kret1[0])
                        elif(jkl==1):
                            if(x=="Staff"):
                                DisplayR.insert(END,"\n\nStaff ID:"+kret1[1])
                            else:
                                DisplayR.insert(END,"\n\nRoll No:"+kret1[1])
                        elif(jkl==2):
                            DisplayR.insert(END,"\n\nBook Name:"+kret1[2])
                        elif(jkl==3):
                            DisplayR.insert(END,"\n\nBook ID:"+kret1[3])
                        elif(jkl==4):
                            DisplayR.insert(END,"\n\nBook Genre:"+kret1[4])
                        elif(jkl==5):
                            DisplayR.insert(END,"\n\nBook Author:"+kret1[5])
                        elif(jkl==6):
                            DisplayR.insert(END,"\n\nDate Borrowed:"+kret1[6])
                        elif(jkl==7):
                            DisplayR.insert(END,"\n\nDue Date:"+kret1[7])
        def ret1(evt):
            BookName1.delete(0, END)
            BookCode1.delete(0, END)
            DatesLoan1.delete(0, END)
            Cata1.delete(0, END)
            curs1.execute("select Book_Name from Books")
            iret=curs1.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            value=str(booklist1.get(booklist1.curselection()))
            gf=value
            for i in range(0,len(kret)):
                if(gf==kret[i]):
                    curs1.execute("select * from Books where Book_Name like '{}'".format(kret[i]))
                    iret1=curs1.fetchall()
                    kret1=[]
                    for ic in range(len(iret1)):
                        lk=str(iret1[ic][0])
                        lk1=str(iret1[ic][1])
                        lk2=str(iret1[ic][2])
                        lk3=str(iret1[ic][3])
                        pk=[lk,lk1,lk2,lk3]
                        kret1=kret1+pk
                    for jkl in range(len(kret1)):
                        if(jkl==(0)):
                                BookName1.insert(END,kret1[0])
                        elif(jkl==1):
                                BookCode1.insert(END,kret1[1])
                        elif(jkl==2):
                                DatesLoan1.insert(END,kret1[2])
                        elif(jkl==3):
                                Cata1.insert(END,kret1[3])                    
        def srchn():
            gt=Srch1.get()
            gf=str(gt)
            if(x=="Staff"):
                curs1.execute("select staff_name from Staff")
            else:
                curs1.execute("select name from {}".format(z))
            iret=curs1.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            for i in range(0,len(kret)):
                if(gf.upper()==kret[i].upper()):
                    messagebox.showinfo("Success","YEAH!! WE FOUND "+gf.upper()+" IN OUR DATA AS "+str(i+1)+" TH MEMBER")
                    if(x=="Staff"):
                        ins=messagebox.askyesno("HELP","DO YOU WANT TO DISPLAY THIS STAFF DATA")
                    else:
                        ins=messagebox.askyesno("HELP","DO YOU WANT TO DISPLAY THIS STUDENT DATA")
                    if(ins>0):
                        DisplayR.delete(1.0,END)
                        if(x=="Staff"):
                            curs1.execute("select * from Staff where staff_Name like '{}'".format(kret[i]))
                        else:
                            curs1.execute("select * from {} where name like '{}'".format(z,kret[i]))
                        iret1=curs1.fetchall()
                        kret1=[]
                        for ic in range(len(iret1)):
                            lk=str(iret1[ic][0])
                            lk1=str(iret1[ic][1])
                            lk2=str(iret1[ic][2])
                            lk3=str(iret1[ic][3])
                            lk4=str(iret1[ic][4])
                            lk5=str(iret1[ic][5])
                            lk6=str(iret1[ic][6])
                            lk7=str(iret1[ic][7])
                            pk=[lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                            kret1=kret1+pk
                        for jkl in range(len(kret1)):
                            if(jkl==(0)):
                                if(x=="Staff"):
                                    DisplayR.insert(END,"Staff Name:"+kret1[0])
                                else:
                                    DisplayR.insert(END,"Name:"+kret1[0])
                            elif(jkl==1):
                                 if(x=="Staff"):
                                     DisplayR.insert(END,"\n\nStaff ID:"+kret1[1])
                                 else:
                                     DisplayR.insert(END,"\n\nRoll No:"+kret1[1])
                            elif(jkl==2):
                                DisplayR.insert(END,"\n\nBook Name:"+kret1[2])
                            elif(jkl==3):
                                DisplayR.insert(END,"\n\nBook ID:"+kret1[3])
                            elif(jkl==4):
                                DisplayR.insert(END,"\n\nBook Gener:"+kret1[4])
                            elif(jkl==5):
                                DisplayR.insert(END,"\n\nBook Author:"+kret1[5])
                            elif(jkl==6):
                                DisplayR.insert(END,"\n\nDate Borrowed:"+kret1[6])
                            elif(jkl==7):
                                DisplayR.insert(END,"\n\nDue Date:"+kret1[7])
                    break
                else:
                        if(i==len(kret)-1):
                                messagebox.showinfo("ERROR","SORRY!! WE COULDNOT FIND "+gf.upper()+" IN OUR DATA")

        def srchn1():
            gt=Srch112.get()
            gt1=str(gt)
            curs1.execute("select Book_Name from Books")
            iret=curs1.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            for i in range(len(kret)):
                    if(gt1.upper()==kret[i].upper()):
                            messagebox.showinfo("Success","YEAH!! WE CAN FIND "+gt1.upper()+" IN OUR DATA")
                            ins=messagebox.askyesno("HELP","DO YOU WANT TO INSERT THIS BOOK")
                            if(ins>0):
                                    BookName1.delete(0, END)
                                    BookCode1.delete(0, END)
                                    DatesLoan1.delete(0, END)
                                    Cata1.delete(0, END)
                                    curs1.execute("select * from Books where Book_Name like '{}'".format(kret[i]))
                                    iret1=curs1.fetchall()
                                    kret1=[]
                                    for ic in range(len(iret1)):
                                        lk=str(iret1[ic][0])
                                        lk1=str(iret1[ic][1])
                                        lk2=str(iret1[ic][2])
                                        lk3=str(iret1[ic][3])
                                        pk=[lk,lk1,lk2,lk3]
                                        kret1=kret1+pk
                                    for jkl in range(len(kret1)):
                                        if(jkl==(0)):
                                                BookName1.insert(END,kret1[0])
                                        elif(jkl==1):
                                                BookCode1.insert(END,kret1[1])
                                        elif(jkl==2):
                                                Cata1.insert(END,kret1[2])
                                        elif(jkl==3):
                                                DatesLoan1.insert(END,kret1[3])
                            break
                    else:
                            if(i==len(kret)-1):
                                    messagebox.showinfo("ERROR","SORRY!! WE COULD NOT FIND "+gt1.upper()+" IN OUR DATA")
        if(x=="Staff"):
            curs1.execute("select Staff_name from Staff")
        else:
            curs1.execute("select name from {}".format(z))
        i=curs1.fetchall()
        k=[]
        for ic in range(len(i)):
            lk=str(i[ic][0])
            pk=[lk]
            k=k+pk
        ListOfBooks=k
        scrollbar=Scrollbar(BookInf)
        scrollbar.grid(row=0,column=1,sticky='ns')
        booklist=Listbox(BookInf,width=17,height=12,font=('arial',12,'bold'))
        booklist.bind('<<ListboxSelect>>',ret)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)
        for items in ListOfBooks:
                      booklist.insert(END,items)
        curs1.execute("select Book_Name from Books")
        iret=curs1.fetchall()
        ak=[]
        for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                ak=ak+pk
        ListOfBooks=ak
        scrollbar1=Scrollbar(BookSlc)
        scrollbar1.grid(row=0,column=1,sticky='ns')
        booklist1=Listbox(BookSlc,width=17,height=12,font=('arial',12,'bold'))
        booklist1.bind('<<ListboxSelect>>',ret1)
        booklist1.grid(row=0,column=0,padx=8)
        scrollbar1.config(command=booklist1.yview)
        for items in ListOfBooks:
                      booklist1.insert(END,items)
        if(x=="Staff"):
            curs1.execute("select * from Staff where Staff.Due_Date<='{}'".format(fg))
        else:
            curs1.execute("select * from {} where {}.Due_Date<='{}'".format(z,z,fg))
        iret=curs1.fetchall()
        ak=[]
        for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                lk1=str(iret[ic][1])
                lk2=str(iret[ic][2])
                lk3=str(iret[ic][3])
                lk4=str(iret[ic][4])
                lk5=str(iret[ic][5])
                lk6=str(iret[ic][6])
                lk7=str(iret[ic][7])
                pk=[lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                ak=ak+pk
        for jkl in range(0,len(ak),8):
                DisplayR111.insert(END,ak[jkl]+"\n")
                DisplayR11.insert(END,ak[jkl+1]+"\n")
                DisplayR21.insert(END,ak[jkl+2]+"\n") 
                DisplayR31.insert(END,ak[jkl+3]+"\n")
                DisplayR41.insert(END,ak[jkl+4]+"\n")
                DisplayR51.insert(END,ak[jkl+5]+"\n")
                DisplayR61.insert(END,ak[jkl+6]+"\n")
                DisplayR71.insert(END,ak[jkl+7]+"\n")
        DisplayR111.configure(state='disabled')
        DisplayR11.configure(state='disabled')
        DisplayR21.configure(state='disabled')
        DisplayR31.configure(state='disabled')
        DisplayR41.configure(state='disabled')
        DisplayR51.configure(state='disabled')
        DisplayR61.configure(state='disabled')
        DisplayR71.configure(state='disabled')
        Home2.mainloop()
    else:
        def center_window(w=300, h=200):
            # get screen width and height
            ws = Home2.winfo_screenwidth()
            hs = Home2.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            Home2.geometry('%dx%d+%d+%d' % (w, h, x, y))
        #Main_Window
        Home2=Tk()
        Home2.title("MVM-Library Recorder")
        Home2.overrideredirect(1)
        Home2.geometry("1280x768")
        center_window(1280,768)
        #Frames
        Main=Frame(Home2, width=1265,bd=10,padx='30',pady=8,bg=X,relief=RIDGE)
        Main.pack(side=TOP)
        Title=Frame(Main, width=1265,padx='5',pady='5',bd=0,bg=X,relief=RIDGE)
        Title.pack(side=TOP)
        Title1=Frame(Main, width=1265,padx='5',pady='5',bd=10,bg=X,relief=RIDGE)
        Title1.pack(side=TOP)
        Title11=Frame(Title1, width=1265,padx='5',pady='5',bd=10,bg=X,relief=RIDGE)
        Title11.grid(row=0,column=5,padx='2',pady='5')
        Time=Frame(Title1, width=1265,padx='5',pady='5',bd=10,bg=X,relief=RIDGE)
        Time.grid(row=0,column=0,padx='5',pady='5')
        Secinf=Frame(Title1, width=1265,padx='5',pady='5',bd=10,bg=X,relief=RIDGE)
        Secinf.grid(row=0,column=7,padx='5',pady='5')
        Content=Frame(Main,width=1265,padx='30',pady='5',bd=10,bg=X,relief=RIDGE)
        Content.pack(padx='0',pady='0')
        BroInf=LabelFrame(Content,text="FILL THE INFORMATION'S",font=("futura",10),width=300,padx='5',pady='10',bd=5,bg=X,fg=Y,relief=RIDGE)
        BroInf.pack(side=LEFT)
        BookSlc=LabelFrame(Content,text="SELECT BOOK",font=("futura",10),width=300,height=200,padx='5',pady='5',bd=5,bg=X,fg=Y,relief=RIDGE)
        BookSlc.pack(side=LEFT)
        BookInf=LabelFrame(Content,text="SELECT TO EXPAND",font=("futura",10),width=300,height=200,padx='5',pady='5',bd=5,bg=X,fg=Y,relief=RIDGE)
        BookInf.pack(side=LEFT)
        Details=LabelFrame(Content,text="DETAILS",font=("futura",10),width=300,height=175,padx=5,pady=2,bd=5,bg=X,fg=Y,relief=RIDGE)
        Details.pack(side=LEFT)
        srch=LabelFrame(Content,text="FIND YOUR REQUIREMENTS",font=("futura",10),width=1265,padx='5',pady='23',bd=5,bg=X,fg=Y,relief=RIDGE)
        srch.pack(side=RIGHT)
        if(x=="Staff"):
            srcha=LabelFrame(srch,text="SEARCH STAFF",font=("futura",10),width=1265,padx='5',pady='5',bd=5,bg=X,fg=Y,relief=RIDGE)
            srcha.pack(side=TOP,pady=12)
        else:
            srcha=LabelFrame(srch,text="SEARCH STUDENT",font=("futura",10),width=1265,padx='5',pady='5',bd=5,bg=X,fg=Y,relief=RIDGE)
            srcha.pack(side=TOP,pady=12)
        srchb=LabelFrame(srch,text="SEARCH BOOKS",font=("futura",10),width=1265,padx='5',pady='4',bd=5,bg=X,fg=Y,relief=RIDGE)
        srchb.pack(side=BOTTOM,pady=12)
        due=Frame(Main,width=1265,height=100,padx=25,pady=5,bd=10,bg=X,relief=RIDGE)
        due.pack()
        Butt=Frame(Main,width=1265,height=100,bd=0,padx=50,pady=0,bg=X,relief=RIDGE)
        Butt.pack()
        #Pros
        de=date.today()
        fg=de.strftime("%Y-%m-%d")
        fg2=de.strftime("%d/%m/%Y")
        gt=fg2.split("/")
        aq=datetime(int(gt[2]),int(gt[1]),int(gt[0]))
        for i in range(0,7):
            aq=aq+timedelta(days=1)
        aq=aq.strftime("%Y-%m-%d")
        kgf=Label(Time,font=("futura",10,"bold"),text="Date:"+fg,fg=Y,bg=X)
        kgf.grid(row=0,column=0,sticky=W)
        li=datetime.now()
        vy=li.strftime("%I:%M %p")
        kgf1=Label(Time,font=("futura",10,"bold"),text="Time:"+vy,bg=X,fg=Y)
        kgf1.grid(row=1,column=0,sticky=W)
        if(x=="Staff"):
            si=Label(Secinf,font=("futura",10,"bold"),text="          "+x+"       ",bg=X,fg=Y)
            si.grid(row=0,column=1,sticky=W)
            si1=Label(Secinf,font=("futura",10,"bold"),text="         "+y+"   ",bg=X,fg=Y)
            si1.grid(row=1,column=1,sticky=W)
        else:
            si=Label(Secinf,font=("futura",10,"bold"),text="Class:"+"\t"+x+"\t",bg=X,fg=Y,pady=3)
            si.grid(row=0,column=11,sticky=W)
            si1=Label(Secinf,font=("futura",10,"bold"),text="Sec:"+"\t"+y+"\t",bg=X,fg=Y,pady=3)
            si1.grid(row=1,column=11,sticky=W)
        si11=Label(Title11,font=("futura",23,"bold"),text="                 Library Data Recorder                 ",bg=X,fg=Y)
        si11.grid(row=1,column=11,sticky=W,padx=10,pady=10)
        JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
        JGD.pack()
        Head=Label(Title,font=("futura",30,"bold"),text="             MAHARISHI VIDYA MANDIR          ",bg=X,fg=Y)
        Head.pack()
        HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y)
        HSR.pack()
        BookName=Label(BroInf,text="Book Name:",font=("futura",14,"bold"),bg=X,fg=Y)
        BookName.grid(row=2,column=0,sticky=W)
        BookName1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
        BookName1.grid(row=2,column=1)
        BookCode=Label(BroInf,text="Book Code:",font=("futura",14,"bold"),bg=X,fg=Y)
        BookCode.grid(row=3,column=0,sticky=W)
        BookCode1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
        BookCode1.grid(row=3,column=1)
        Cata=Label(BroInf,text="Book Genre:",font=("futura",14,"bold"),bg=X,fg=Y)
        Cata.grid(row=4,column=0,sticky=W)
        Cata1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
        Cata1.grid(row=4,column=1)
        Srch=Label(srcha,text="Name:",font=("futura",10,"bold"),fg=Y,bg=X)
        Srch.grid(row=0,column=0,sticky=W)
        Srch1=Entry(srcha,font=("futura",9,"bold"),width="25",bd=2)
        Srch1.grid(row=1,column=0)
        Srch11=Button(srcha,text="Search",font=("futura",8,"bold"),command=lambda:[srchn()])
        Srch11.grid(row=1,column=1)
        Srch12=Label(srchb,text="Book Name:",font=("futura",10,"bold"),bg=X,fg=Y).grid(row=0,column=0,sticky=W)
        Srch112=Entry(srchb,font=("futura",9,"bold"),width="25",bd=2)
        Srch112.grid(row=1,column=0)
        Srch1112=Button(srchb,text="Search",font=("futura",8,"bold"),command=lambda:[srchn1()])
        Srch1112.grid(row=1,column=1)
        if(x=="Staff"):
            RollNo=Label(BroInf,text="Staff ID:",font=("futura",14,"bold"),bg=X,fg=Y)
            RollNo.grid(row=1,column=0,sticky=W)
            RollNo1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
            RollNo1.grid(row=1,column=1)
        else:
            RollNo=Label(BroInf,text="RollNo:",font=("futura",14,"bold"),bg=X,fg=Y)
            RollNo.grid(row=1,column=0,sticky=W)
            RollNo1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
            RollNo1.grid(row=1,column=1)
        if(x=="Staff"):
             Name=Label(BroInf,text="Staff Name:",font=("futura",14,"bold"),bg=X,fg=Y)
             Name.grid(row=0,column=0,sticky=W,)
             Name1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
             Name1.grid(row=0,column=1)
        else:
            Name=Label(BroInf,text="Name:",font=("futura",14,"bold"),bg=X,fg=Y)
            Name.grid(row=0,column=0,sticky=W,)
            Name1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
            Name1.grid(row=0,column=1)
        DateBorrowed=Label(BroInf,text="Date Borrowed:",font=("futura",14,"bold"),bg=X,fg=Y)
        DateBorrowed.grid(row=6,column=0,sticky=W)
        DateBorrowed1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
        DateBorrowed1.grid(row=6,column=1)
        DateBorrowed1.insert(END,fg)
        DatesLoan=Label(BroInf,text="Book Author:",font=("futura",14,"bold"),bg=X,fg=Y)
        DatesLoan.grid(row=5,column=0,sticky=W)
        DatesLoan1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
        DatesLoan1.grid(row=5,column=1)
        DueDate=Label(BroInf,text="Due Date:",font=("futura",14,"bold"),bg=X,fg=Y)
        DueDate.grid(row=7,column=0,sticky=W)
        DueDate1=Entry(BroInf,font=("futura",10,"bold"),width="25",bd=2)
        DueDate1.grid(row=7,column=1)
        DueDate1.insert(END,aq)
        DisplayR=Text(Details,font=('futura',10,'bold'),width=20,height=15)
        DisplayR.grid(row=0,column=1)
        JGD2=Label(due,font=("futura",10,"bold"),text="Name:",bg=X,fg=Y)
        JGD2.grid(row=0,column=1)
        JGD3=Label(due,font=("futura",10,"bold"),text="Roll No:",bg=X,fg=Y)
        JGD3.grid(row=0,column=2)
        JGD4=Label(due,font=("futura",10,"bold"),text="Book Name:",bg=X,fg=Y)
        JGD4.grid(row=0,column=3)
        JGD5=Label(due,font=("futura",10,"bold"),text="Book Code:",bg=X,fg=Y)
        JGD5.grid(row=0,column=4)
        JGD6=Label(due,font=("futura",10,"bold"),text="Book Gener:",bg=X,fg=Y)
        JGD6.grid(row=0,column=5)
        JGD7=Label(due,font=("futura",10,"bold"),text="Book Author:",bg=X,fg=Y)
        JGD7.grid(row=0,column=6)
        JGD8=Label(due,font=("futura",10,"bold"),text="Date Borrowed:",bg=X,fg=Y)
        JGD8.grid(row=0,column=7)
        JGD9=Label(due,font=("futura",10,"bold"),text="Due Date:",bg=X,fg=Y)
        JGD9.grid(row=0,column=8)
        JGD10=Label(due,font=("futura",13,"bold"),text="Today's Due:  ",bg=X,fg=Y)
        JGD10.grid(row=1,column=0)
        DisplayR111=Text(due,font=('futura',10,'bold'),width=23,height=2)
        DisplayR111.grid(row=1,column=1)
        DisplayR11=Text(due,font=('futura',10,'bold'),width=15,height=2)
        DisplayR11.grid(row=1,column=2)
        DisplayR21=Text(due,font=('futura',10,'bold'),width=23,height=2)
        DisplayR21.grid(row=1,column=3)
        DisplayR31=Text(due,font=('futura',10,'bold'),width=15,height=2)
        DisplayR31.grid(row=1,column=4)
        DisplayR41=Text(due,font=('futura',10,'bold'),width=15,height=2)
        DisplayR41.grid(row=1,column=5)
        DisplayR51=Text(due,font=('futura',10,'bold'),width=23,height=2)
        DisplayR51.grid(row=1,column=6)
        DisplayR61=Text(due,font=('futura',10,'bold'),width=14,height=2)
        DisplayR61.grid(row=1,column=7)
        DisplayR71=Text(due,font=('futura',10,'bold'),width=12,height=2)
        DisplayR71.grid(row=1,column=8)
        add=Button(Butt,text="ADD",font=("futura",19,"bold"),padx=5,pady=5,bd=5,command=lambda:[sad(),Students2(x,y,z,X,Y),Home2.destroy()])
        add.grid(row=0,column=0,padx='5',pady='5')
        go=Button(Butt,text="SETTINGS",font=("futura",19,"bold"),padx=5,pady=5,bd=5,command=lambda:[Settings(Home2,X,Y)])
        go.grid(row=0,column=40,padx='5',pady='5')
        delete=Button(Butt,text="REMOVE",font=("futura",19,"bold"),padx=5,pady=5,bd=5,command=lambda:[clear(),Home2.destroy(),Students2(x,y,z,X,Y)])
        delete.grid(row=0,column=1,padx='5',pady='5')
        fst1=Button(Butt,text="ADD BOOK",font=("futura",19,"bold"),padx=5,pady=5,bd=5,command=lambda:[Books(X,Y)])
        fst1.grid(row=0,column=11,padx='5',pady='5')
        exi=Button(Butt,text="QUIT",font=("futura",19,"bold"),padx=5,pady=5,bd=5,bg="red",command=lambda:[qui()])
        exi.grid(row=0,column=500,padx='5',pady='5')
        fst=Button(Butt,text="GO BACK",font=("futura",19,"bold"),padx=5,pady=5,bd=5,bg="blue",command=lambda:[Login_selection2(X,Y),Home2.destroy()])
        fst.grid(row=0,column=400,padx='5',pady='5')
    #============================================================STUDENT_&_STAFF_RECORD_BACKEND=================================================================#
        def sad():
            a=Name1.get()
            aa=BookName1.get()
            bb=BookCode1.get()
            cc=RollNo1.get()
            dd=DateBorrowed1.get()
            ee=Cata1.get()
            ff=DueDate1.get()
            gg=DatesLoan1.get()
            ad=str(aa)
            bd=str(bb)
            cd=str(cc)
            dd=str(dd)
            ed=str(ee)
            fd=str(ff)
            gd=str(gg)
            w=str(a)
            if(len(w)>25):
                if(x=="Staff"):
                    messagebox.showinfo("Error!!!","Staff Name Entered Is To Long(MAX-25 Characters)")
                else:
                    messagebox.showinfo("Error!!!","Name Entered Is To Long(MAX-25 Characters)")
            elif(len(cd)>10):
                if(x=="Staff"):
                    messagebox.showinfo("Error!!!","Staff ID Entered Is To Long(MAX-10 Characters)")
                else:
                    messagebox.showinfo("Error!!!","Roll No Entered Is To Long(MAX-10 Characters)")
            else:
                if(x=="Staff"):
                    curs1.execute("insert into Staff values('{}','{}','{}','{}','{}','{}','{}','{}')".format(w,cd,ad,bd,ed,gd,dd,fd))
                    con.commit()
                else:
                    curs1.execute("insert into {} values('{}','{}','{}','{}','{}','{}','{}','{}')".format(z,w,cd,ad,bd,ed,gd,dd,fd))
                    con.commit()
        def qui():
            exiit=messagebox.askyesno("EXIT","ARE YOU SURE YOU WANT TO QUIT")
            if(exiit>0):
                Home2.destroy()
        def clear():
            ins=messagebox.askyesno("WARNING","DO YOU WANT TO REMOVE THIS STUDENT DATA")
            if(ins>0):
                if(x=="Staff"):
                    curs1.execute("select staff_Name from Staff")
                else:
                    curs1.execute("select Name from {}".format(z))
                iret=curs1.fetchall()
                kret=[]
                for ic in range(len(iret)):
                        lk=str(iret[ic][0])
                        pk=[lk]
                        kret=kret+pk
            value=str(booklist.get(booklist.curselection()))
            gf=value
            for i in range(0,len(kret)):
                    if(gf==kret[i]):
                        if(x=="Staff"):
                            curs1.execute("delete from Staff where staff_Name='{}'".format(gf))
                            con.commit()
                        else:
                            curs1.execute("delete from {} where Name='{}'".format(z,gf))
                            con.commit()
        def ret(evt):
            DisplayR.delete(1.0,END)
            if(x=="Staff"):
                curs1.execute("select staff_name from Staff")
            else:
                curs1.execute("select name from {}".format(z))
            iret=curs1.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            value=str(booklist.get(booklist.curselection()))
            gf=value
            for i in range(0,len(kret)):
                if(gf==kret[i]):
                    if(x=="Staff"):
                        curs1.execute("select * from Staff where staff_Name like '{}'".format(kret[i]))
                    else:
                        curs1.execute("select * from {} where name like '{}'".format(z,kret[i]))
                    iret1=curs1.fetchall()
                    kret1=[]
                    for ic in range(len(iret1)):
                        lk=str(iret1[ic][0])
                        lk1=str(iret1[ic][1])
                        lk2=str(iret1[ic][2])
                        lk3=str(iret1[ic][3])
                        lk4=str(iret1[ic][4])
                        lk5=str(iret1[ic][5])
                        lk6=str(iret1[ic][6])
                        lk7=str(iret1[ic][7])
                        pk=[lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                        kret1=kret1+pk
                    for jkl in range(len(kret1)):
                        if(jkl==(0)):
                            if(x=="Staff"):
                                DisplayR.insert(END,"Staff Name:"+kret1[0])
                            else:
                                DisplayR.insert(END,"Name:"+kret1[0])
                        elif(jkl==1):
                            if(x=="Staff"):
                                DisplayR.insert(END,"\n\nStaff ID:"+kret1[1])
                            else:
                                DisplayR.insert(END,"\n\nRoll No:"+kret1[1])
                        elif(jkl==2):
                            DisplayR.insert(END,"\n\nBook Name:"+kret1[2])
                        elif(jkl==3):
                            DisplayR.insert(END,"\n\nBook ID:"+kret1[3])
                        elif(jkl==4):
                            DisplayR.insert(END,"\n\nBook Genre:"+kret1[4])
                        elif(jkl==5):
                            DisplayR.insert(END,"\n\nBook Author:"+kret1[5])
                        elif(jkl==6):
                            DisplayR.insert(END,"\n\nDate Borrowed:"+kret1[6])
                        elif(jkl==7):
                            DisplayR.insert(END,"\n\nDue Date:"+kret1[7])
        def ret1(evt):
            BookName1.delete(0, END)
            BookCode1.delete(0, END)
            DatesLoan1.delete(0, END)
            Cata1.delete(0, END)
            curs1.execute("select Book_Name from Books")
            iret=curs1.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            value=str(booklist1.get(booklist1.curselection()))
            gf=value
            for i in range(0,len(kret)):
                if(gf==kret[i]):
                    curs1.execute("select * from Books where Book_Name like '{}'".format(kret[i]))
                    iret1=curs1.fetchall()
                    kret1=[]
                    for ic in range(len(iret1)):
                        lk=str(iret1[ic][0])
                        lk1=str(iret1[ic][1])
                        lk2=str(iret1[ic][2])
                        lk3=str(iret1[ic][3])
                        pk=[lk,lk1,lk2,lk3]
                        kret1=kret1+pk
                    for jkl in range(len(kret1)):
                        if(jkl==(0)):
                                BookName1.insert(END,kret1[0])
                        elif(jkl==1):
                                BookCode1.insert(END,kret1[1])
                        elif(jkl==2):
                                DatesLoan1.insert(END,kret1[2])
                        elif(jkl==3):
                                Cata1.insert(END,kret1[3])                    
        def srchn():
            gt=Srch1.get()
            gf=str(gt)
            if(x=="Staff"):
                curs1.execute("select staff_name from Staff")
            else:
                curs1.execute("select name from {}".format(z))
            iret=curs1.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            for i in range(0,len(kret)):
                if(gf.upper()==kret[i].upper()):
                    messagebox.showinfo("Success","YEAH!! WE FOUND "+gf.upper()+" IN OUR DATA AS "+str(i+1)+" TH MEMBER")
                    if(x=="Staff"):
                        ins=messagebox.askyesno("HELP","DO YOU WANT TO DISPLAY THIS STAFF DATA")
                    else:
                        ins=messagebox.askyesno("HELP","DO YOU WANT TO DISPLAY THIS STUDENT DATA")
                    if(ins>0):
                        DisplayR.delete(1.0,END)
                        if(x=="Staff"):
                            curs1.execute("select * from Staff where staff_Name like '{}'".format(kret[i]))
                        else:
                            curs1.execute("select * from {} where name like '{}'".format(z,kret[i]))
                        iret1=curs1.fetchall()
                        kret1=[]
                        for ic in range(len(iret1)):
                            lk=str(iret1[ic][0])
                            lk1=str(iret1[ic][1])
                            lk2=str(iret1[ic][2])
                            lk3=str(iret1[ic][3])
                            lk4=str(iret1[ic][4])
                            lk5=str(iret1[ic][5])
                            lk6=str(iret1[ic][6])
                            lk7=str(iret1[ic][7])
                            pk=[lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                            kret1=kret1+pk
                        for jkl in range(len(kret1)):
                            if(jkl==(0)):
                                if(x=="Staff"):
                                    DisplayR.insert(END,"Staff Name:"+kret1[0])
                                else:
                                    DisplayR.insert(END,"Name:"+kret1[0])
                            elif(jkl==1):
                                 if(x=="Staff"):
                                     DisplayR.insert(END,"\n\nStaff ID:"+kret1[1])
                                 else:
                                     DisplayR.insert(END,"\n\nRoll No:"+kret1[1])
                            elif(jkl==2):
                                DisplayR.insert(END,"\n\nBook Name:"+kret1[2])
                            elif(jkl==3):
                                DisplayR.insert(END,"\n\nBook ID:"+kret1[3])
                            elif(jkl==4):
                                DisplayR.insert(END,"\n\nBook Gener:"+kret1[4])
                            elif(jkl==5):
                                DisplayR.insert(END,"\n\nBook Author:"+kret1[5])
                            elif(jkl==6):
                                DisplayR.insert(END,"\n\nDate Borrowed:"+kret1[6])
                            elif(jkl==7):
                                DisplayR.insert(END,"\n\nDue Date:"+kret1[7])
                    break
                else:
                        if(i==len(kret)-1):
                                messagebox.showinfo("ERROR","SORRY!! WE COULDNOT FIND "+gf.upper()+" IN OUR DATA")

        def srchn1():
            gt=Srch112.get()
            gt1=str(gt)
            curs1.execute("select Book_Name from Books")
            iret=curs1.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            for i in range(len(kret)):
                    if(gt1.upper()==kret[i].upper()):
                            messagebox.showinfo("Success","YEAH!! WE CAN FIND "+gt1.upper()+" IN OUR DATA")
                            ins=messagebox.askyesno("HELP","DO YOU WANT TO INSERT THIS BOOK")
                            if(ins>0):
                                    BookName1.delete(0, END)
                                    BookCode1.delete(0, END)
                                    DatesLoan1.delete(0, END)
                                    Cata1.delete(0, END)
                                    curs1.execute("select * from Books where Book_Name like '{}'".format(kret[i]))
                                    iret1=curs1.fetchall()
                                    kret1=[]
                                    for ic in range(len(iret1)):
                                        lk=str(iret1[ic][0])
                                        lk1=str(iret1[ic][1])
                                        lk2=str(iret1[ic][2])
                                        lk3=str(iret1[ic][3])
                                        pk=[lk,lk1,lk2,lk3]
                                        kret1=kret1+pk
                                    for jkl in range(len(kret1)):
                                        if(jkl==(0)):
                                                BookName1.insert(END,kret1[0])
                                        elif(jkl==1):
                                                BookCode1.insert(END,kret1[1])
                                        elif(jkl==2):
                                                Cata1.insert(END,kret1[2])
                                        elif(jkl==3):
                                                DatesLoan1.insert(END,kret1[3])
                            break
                    else:
                            if(i==len(kret)-1):
                                    messagebox.showinfo("ERROR","SORRY!! WE COULD NOT FIND "+gt1.upper()+" IN OUR DATA")
        if(x=="Staff"):
            curs1.execute("select Staff_name from Staff")
        else:
            curs1.execute("select name from {}".format(z))
        i=curs1.fetchall()
        k=[]
        for ic in range(len(i)):
            lk=str(i[ic][0])
            pk=[lk]
            k=k+pk
        ListOfBooks=k
        scrollbar=Scrollbar(BookInf)
        scrollbar.grid(row=0,column=1,sticky='ns')
        booklist=Listbox(BookInf,width=15,height=14,font=('arial',10,'bold'))
        booklist.bind('<<ListboxSelect>>',ret)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)
        for items in ListOfBooks:
                      booklist.insert(END,items)
        curs1.execute("select Book_Name from Books")
        iret=curs1.fetchall()
        ak=[]
        for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                ak=ak+pk
        ListOfBooks=ak
        scrollbar1=Scrollbar(BookSlc)
        scrollbar1.grid(row=0,column=1,sticky='ns')
        booklist1=Listbox(BookSlc,width=15,height=14,font=('arial',10,'bold'))
        booklist1.bind('<<ListboxSelect>>',ret1)
        booklist1.grid(row=0,column=0,padx=8)
        scrollbar1.config(command=booklist1.yview)
        for items in ListOfBooks:
                      booklist1.insert(END,items)
        if(x=="Staff"):
            curs1.execute("select * from Staff where Staff.Due_Date<='{}'".format(fg))
        else:
            curs1.execute("select * from {} where {}.Due_Date<='{}'".format(z,z,fg))
        iret=curs1.fetchall()
        ak=[]
        for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                lk1=str(iret[ic][1])
                lk2=str(iret[ic][2])
                lk3=str(iret[ic][3])
                lk4=str(iret[ic][4])
                lk5=str(iret[ic][5])
                lk6=str(iret[ic][6])
                lk7=str(iret[ic][7])
                pk=[lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                ak=ak+pk
        for jkl in range(0,len(ak),8):
                DisplayR111.insert(END,ak[jkl]+"\n")
                DisplayR11.insert(END,ak[jkl+1]+"\n")
                DisplayR21.insert(END,ak[jkl+2]+"\n") 
                DisplayR31.insert(END,ak[jkl+3]+"\n")
                DisplayR41.insert(END,ak[jkl+4]+"\n")
                DisplayR51.insert(END,ak[jkl+5]+"\n")
                DisplayR61.insert(END,ak[jkl+6]+"\n")
                DisplayR71.insert(END,ak[jkl+7]+"\n")
        Home2.mainloop()
#======================================================================LOGIN_VERIFICATION===================================================================#
def Maain(X,Y,Z):
        ad=open("Staff","r")
        ad1=ad.readline()
        if(ad1=="Staff"):
            Students2(ad1,"Record","Staff",X,Y)
            ad=open("Staff","w")
            Z.destroy()
        else:
            f=open("Class.txt","r")
            l=open("Sec.txt","r")
            f2=f.readlines()
            f3=l.readlines()
            if(f2==[] or f3==[]):
                Login=messagebox.showinfo("ERROR!!!","Please Select Class And Section")
            else:
                cls=str(f2[0])
                sc=str(f3[0]).lower()
                clsc=sc+cls
                Students2(cls,sc.upper(),clsc,X,Y)
                Z.destroy()
#=======================================================================LOGINPAGE_FRONTEND==================================================================#
def Login_selection2(X,Y):
    curs.execute("select * from Resolution")
    Resol=curs.fetchall()
    if(Resol==[]):
        def center_window(w=300, h=200):
            # get screen width and height
            ws = wind123.winfo_screenwidth()
            hs = wind123.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            wind123.geometry('%dx%d+%d+%d' % (w,h, x, y))
        wind123=Tk()
        de=date.today()
        fg=de.strftime("%Y-%m-%d")
        wind123.title("MVM-Library Recorder")
        wind123.resizable(width=0,height=0)
        wind123.overrideredirect(1)
        center_window(1310,550)
        Main=Frame(wind123,padx='15',pady='5',bd=10,relief=RIDGE,bg=X)
        Main.pack()
        Title=Frame(Main,padx='5',pady='30',bd=0,relief=RIDGE,bg=X)
        Title.pack(side=TOP)
        Title4=Frame(Main,padx='5',pady='15',bd=10,relief=RIDGE,bg=X)
        Title4.pack(side=RIGHT,pady='15')
        frAme1=Frame(Title4,padx='10',pady='10',bd=5,relief=RIDGE,width=70,bg=X)
        frAme1.pack(side=TOP,padx='5',pady='5')
        Title1=Frame(Title4,padx='5',pady='5',bd=0,relief=RIDGE,bg=X)
        Title1.pack()
        Title2=Frame(Main,padx='5',pady='15',bd=0,relief=RIDGE,bg=X)
        Title2.pack(side=LEFT,pady='15')
        JGD1=Label(Title2,font=("futura",19,"bold"),text="Select Record",bg=X,fg=Y)
        JGD1.pack()
        frAme=Frame(Title2,padx='10',pady='10',bg=X)
        frAme.pack(side=TOP,padx='5',pady='5')
        Butt=Frame(Title2,padx='10',pady='5',bd=10,relief=RIDGE,bg=X)
        Butt.pack(side=TOP,padx='5',pady='0')
        JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
        JGD.pack()
        Head=Label(Title,font=("futura",35,"bold"),text="\tMAHARISHI VIDYA MANDIR             ",bg=X,fg=Y)
        Head.pack()
        HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y)
        HSR.pack()
        BookName=Label(frAme,text="Class:",font=("futura",19,"bold"),bg=X,fg=Y)
        BookName.grid(row=0,column=0,sticky=E)
        Book=Label(frAme,text="Section:",font=("futura",19,"bold"),bg=X,fg=Y)
        Book.grid(row=1,column=0,sticky=E,padx='5',pady='5')
        due=Label(frAme1,text="          Today's Due         ",font=("futura",19,"bold"),bg=X,fg=Y)
        due.pack()
        JGD2=Label(Title1,font=("futura",13,"bold"),text="Name:",bg=X,fg=Y)
        JGD2.grid(row=0,column=0)
        JGD3=Label(Title1,font=("futura",13,"bold"),text="Roll No:",bg=X,fg=Y)
        JGD3.grid(row=0,column=1)
        JGD4=Label(Title1,font=("futura",13,"bold"),text="Book Name:",bg=X,fg=Y)
        JGD4.grid(row=0,column=2)
        JGD5=Label(Title1,font=("futura",13,"bold"),text="Book Code:",bg=X,fg=Y)
        JGD5.grid(row=0,column=3)
        JGD6=Label(Title1,font=("futura",13,"bold"),text="From:",bg=X,fg=Y)
        JGD6.grid(row=0,column=4)
        DisplayR=Text(Title1,font=('arial',13,'bold'),width=23,height=10)
        DisplayR.grid(row=1,column=0)
        DisplayR1=Text(Title1,font=('arial',13,'bold'),width=10,height=10)
        DisplayR1.grid(row=1,column=1)
        DisplayR2=Text(Title1,font=('arial',13,'bold'),width=23,height=10)
        DisplayR2.grid(row=1,column=2)
        DisplayR3=Text(Title1,font=('arial',13,'bold'),width=12,height=10)
        DisplayR3.grid(row=1,column=3)
        DisplayR4=Text(Title1,font=('arial',13,'bold'),width=6,height=10)
        DisplayR4.grid(row=1,column=4)
        chose=ttk.Combobox(frAme,font=("arial",19,"bold"),width=25,state="randomly")
        chose["values"]=[5,6,7,8,9,10,11,12]
        chose.current(0)
        chose.grid(column=1,row=0)
        name1=StringVar()
        chose1=ttk.Combobox(frAme,font=("futura",19,"bold"),width=25,state="randomly")
        chose1["values"]=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
        chose1.current(0)
        chose1.grid(column=1,row=1,padx='5',pady='5')
        Tadd=Button(frAme,text="Open Record",font=("futura",13,"bold"),bd=3,command=lambda:[gu(),Maain(X,Y,wind123)])
        Tadd.grid(row=2,column=1,sticky=E)
        Tlog=Button(frAme,text="Staff Record",font=("futura",13,"bold"),bd=3,command=lambda:[gu1(),Maain(X,Y,wind123)])
        Tlog.grid(row=2,column=1,sticky=W)
        Tlog1=Button(Butt,text="Add Book",font=("futura",15,"bold"),bd=3,command=lambda:[Books(X,Y)])
        Tlog1.grid(row=0,column=0,sticky=W,padx='10')
        settings=Button(Butt,text="Settings",font=("futura",15,"bold"),bd=3,command=lambda:[Settings(wind123,X,Y)])
        settings.grid(row=0,column=1,sticky=EW,padx='10')
        exi=Button(Butt,text="QUIT",font=("futura",15,"bold"),bg="red",bd=3,command=lambda:[qui()])
        exi.grid(row=0,column=2,sticky=E,padx='10')
    #======================================================================LOGINPAGE_BACKEND====================================================================#
        def qui():
                    exiit=messagebox.askyesno("EXIT","ARE YOU SURE YOU WANT TO QUIT")
                    if(exiit>0):
                        wind123.destroy()
        curs1.execute("select * from staff where staff.Due_Date <= '{}'".format(fg))
        iret=curs1.fetchall()
        kret1=[]
        ak=[]
        kret11=[]
        def gu():
                Class=chose.get()
                Sec=chose1.get()
                Class=str(Class)
                Sec=str(Sec)
                ad=open("Class.txt","w")
                bd=open("Sec.txt","w")
                aw=ad.write(Class)
                am=bd.write(Sec)
        def gu1():
            ad=open("Staff","w")
            ad.write("Staff")
        for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                lk1=str(iret[ic][1])
                lk2=str(iret[ic][2])
                lk3=str(iret[ic][3])
                lk4=str(iret[ic][4])
                lk5=str(iret[ic][5])
                lk6=str(iret[ic][6])
                lk7=str(iret[ic][7])
                pk=["Staff",lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                ak=ak+pk
        for jkl in range(0,len(ak),9):
                DisplayR.insert(END,ak[jkl+1]+"\n")
                DisplayR1.insert(END,ak[jkl+2]+"\n")
                DisplayR2.insert(END,ak[jkl+3]+"\n") 
                DisplayR3.insert(END,ak[jkl+4]+"\n")
                DisplayR4.insert(END,ak[jkl]+"\n")
        for pc in AA11:
            curs.execute("select * from {}5 where {}5.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["5"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}6 where {}6.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["6"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}7 where {}7.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["7"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}8 where {}8.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["8"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}9 where {}9.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["9"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}10 where {}10.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["10"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}11 where {}11.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["11"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}12 where {}12.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["12"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
        for jkl in range(0,len(kret1),9):
                DisplayR.insert(END,kret1[jkl+1]+"\n")
                DisplayR1.insert(END,kret1[jkl+2]+"\n")
                DisplayR2.insert(END,kret1[jkl+3]+"\n") 
                DisplayR3.insert(END,kret1[jkl+4]+"\n")
                DisplayR4.insert(END,kret1[jkl]+"\n")
        DisplayR.configure(state='disabled')
        DisplayR1.configure(state='disabled')
        DisplayR2.configure(state='disabled')
        DisplayR3.configure(state='disabled')
        DisplayR4.configure(state='disabled')
        wind123.mainloop()
    else:
        def center_window(w=300, h=200):
            # get screen width and height
            ws = wind123.winfo_screenwidth()
            hs = wind123.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            wind123.geometry('%dx%d+%d+%d' % (w,h, x, y))
        wind123=Tk()
        de=date.today()
        fg=de.strftime("%Y-%m-%d")
        wind123.title("MVM-Library Recorder")
        wind123.resizable(width=0,height=0)
        wind123.overrideredirect(1)
        center_window(1150,550)
        Main=Frame(wind123,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Main.pack()
        Title=Frame(Main,padx='5',pady='30',bd=0,relief=RIDGE,bg=X)
        Title.pack(side=TOP)
        Title4=Frame(Main,padx='5',pady='15',bd=10,relief=RIDGE,bg=X)
        Title4.pack(side=RIGHT,pady='15')
        frAme1=Frame(Title4,padx='10',pady='10',bd=5,relief=RIDGE,width=70,bg=X)
        frAme1.pack(side=TOP,padx='5',pady='5')
        Title1=Frame(Title4,padx='5',pady='5',bd=0,relief=RIDGE,bg=X)
        Title1.pack()
        Title2=Frame(Main,padx='5',pady='15',bd=0,relief=RIDGE,bg=X)
        Title2.pack(side=LEFT,pady='15')
        JGD1=Label(Title2,font=("futura",19,"bold"),text="Select Login",bg=X,fg=Y)
        JGD1.pack()
        frAme=Frame(Title2,padx='10',pady='10',bg=X)
        frAme.pack(side=TOP,padx='5',pady='5')
        Butt=Frame(Title2,padx='10',pady='10',bd=10,relief=RIDGE,bg=X)
        Butt.pack(side=TOP,padx='5',pady='5')
        JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
        JGD.pack()
        Head=Label(Title,font=("futura",35,"bold"),text="\tMAHARISHI VIDYA MANDIR             ",bg=X,fg=Y)
        Head.pack()
        HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y)
        HSR.pack()
        BookName=Label(frAme,text="Class:",font=("futura",19,"bold"),bg=X,fg=Y)
        BookName.grid(row=0,column=0,sticky=E)
        Book=Label(frAme,text="Section:",font=("futura",19,"bold"),bg=X,fg=Y)
        Book.grid(row=1,column=0,sticky=E,padx='5',pady='5')
        due=Label(frAme1,text="          Today's Due         ",font=("futura",19,"bold"),bg=X,fg=Y)
        due.pack()
        JGD2=Label(Title1,font=("futura",10,"bold"),text="Name:",bg=X,fg=Y)
        JGD2.grid(row=0,column=0)
        JGD3=Label(Title1,font=("futura",10,"bold"),text="Roll No:",bg=X,fg=Y)
        JGD3.grid(row=0,column=1)
        JGD4=Label(Title1,font=("futura",10,"bold"),text="Book Name:",bg=X,fg=Y)
        JGD4.grid(row=0,column=2)
        JGD5=Label(Title1,font=("futura",10,"bold"),text="Book Code:",bg=X,fg=Y)
        JGD5.grid(row=0,column=3)
        JGD6=Label(Title1,font=("futura",10,"bold"),text="From:",bg=X,fg=Y)
        JGD6.grid(row=0,column=4)
        DisplayR=Text(Title1,font=('arial',10,'bold'),width=23,height=10)
        DisplayR.grid(row=1,column=0)
        DisplayR1=Text(Title1,font=('arial',10,'bold'),width=10,height=10)
        DisplayR1.grid(row=1,column=1)
        DisplayR2=Text(Title1,font=('arial',10,'bold'),width=23,height=10)
        DisplayR2.grid(row=1,column=2)
        DisplayR3=Text(Title1,font=('arial',10,'bold'),width=12,height=10)
        DisplayR3.grid(row=1,column=3)
        DisplayR4=Text(Title1,font=('arial',10,'bold'),width=6,height=10)
        DisplayR4.grid(row=1,column=4)
        chose=ttk.Combobox(frAme,font=("arial",19,"bold"),width=25,state="randomly")
        chose["values"]=[5,6,7,8,9,10,11,12]
        chose.current(0)
        chose.grid(column=1,row=0)
        name1=StringVar()
        chose1=ttk.Combobox(frAme,font=("futura",19,"bold"),width=25,state="randomly")
        chose1["values"]=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
        chose1.current(0)
        chose1.grid(column=1,row=1,padx='5',pady='5')
        def gu():
                Class=chose.get()
                Sec=chose1.get()
                Class=str(Class)
                Sec=str(Sec)
                ad=open("Class.txt","w")
                bd=open("Sec.txt","w")
                aw=ad.write(Class)
                am=bd.write(Sec)
        Tadd=Button(frAme,text="Open Record",font=("futura",13,"bold"),bd=3,command=lambda:[gu(),Maain(X,Y,wind123)])
        Tadd.grid(row=2,column=1,sticky=E)
        Tlog=Button(frAme,text="Staff Record",font=("futura",13,"bold"),bd=3,command=lambda:[gu1(),Maain(X,Y,wind123)])
        Tlog.grid(row=2,column=1,sticky=W)
        Tlog1=Button(Butt,text="Add Book",font=("futura",15,"bold"),bd=3,command=lambda:[Books(X,Y)])
        Tlog1.grid(row=0,column=0,sticky=W,padx='10')
        settings=Button(Butt,text="Settings",font=("futura",15,"bold"),bd=3,command=lambda:[Settings(wind123,X,Y)])
        settings.grid(row=0,column=1,sticky=EW,padx='10')
        exi=Button(Butt,text="QUIT",font=("futura",15,"bold"),bg="red",bd=3,command=lambda:[qui()])
        exi.grid(row=0,column=2,sticky=E,padx='10')
    #======================================================================LOGINPAGE_BACKEND====================================================================#
        def qui():
                    exiit=messagebox.askyesno("EXIT","ARE YOU SURE YOU WANT TO QUIT")
                    if(exiit>0):
                        wind123.destroy()
        curs1.execute("select * from staff where staff.Due_Date <= '{}'".format(fg))
        iret=curs1.fetchall()
        kret1=[]
        ak=[]
        kret11=[]
        def gu():
                Class=chose.get()
                Sec=chose1.get()
                Class=str(Class)
                Sec=str(Sec)
                ad=open("Class.txt","w")
                bd=open("Sec.txt","w")
                aw=ad.write(Class)
                am=bd.write(Sec)
        def gu1():
            ad=open("Staff","w")
            ad.write("Staff")
        for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                lk1=str(iret[ic][1])
                lk2=str(iret[ic][2])
                lk3=str(iret[ic][3])
                lk4=str(iret[ic][4])
                lk5=str(iret[ic][5])
                lk6=str(iret[ic][6])
                lk7=str(iret[ic][7])
                pk=["Staff",lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                ak=ak+pk
        for jkl in range(0,len(ak),9):
                DisplayR.insert(END,ak[jkl+1]+"\n")
                DisplayR1.insert(END,ak[jkl+2]+"\n")
                DisplayR2.insert(END,ak[jkl+3]+"\n") 
                DisplayR3.insert(END,ak[jkl+4]+"\n")
                DisplayR4.insert(END,ak[jkl]+"\n")
        for pc in AA11:
            curs.execute("select * from {}5 where {}5.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["5"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}6 where {}6.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["6"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}7 where {}7.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["7"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}8 where {}8.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["8"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}9 where {}9.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["9"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}10 where {}10.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["10"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}11 where {}11.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["11"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
            curs.execute("select * from {}12 where {}12.Due_Date <= '{}'".format(pc,pc,fg))
            iret1=curs.fetchall()
            for ic in range(len(iret1)):
                lk=str(iret1[ic][0])
                lk1=str(iret1[ic][1])
                lk2=str(iret1[ic][2])
                lk3=str(iret1[ic][3])
                lk4=str(iret1[ic][4])
                lk5=str(iret1[ic][5])
                lk6=str(iret1[ic][6])
                lk7=str(iret1[ic][7])
                pk=["12"+pc,lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7]
                kret1=kret1+pk
        for jkl in range(0,len(kret1),9):
                DisplayR.insert(END,kret1[jkl+1]+"\n")
                DisplayR1.insert(END,kret1[jkl+2]+"\n")
                DisplayR2.insert(END,kret1[jkl+3]+"\n") 
                DisplayR3.insert(END,kret1[jkl+4]+"\n")
                DisplayR4.insert(END,kret1[jkl]+"\n")
        wind123.mainloop()
#======================================================================BOOKSRECORD_FRONTEND=================================================================#
def Books(X,Y):
        def center_window(w=300, h=200):
            # get screen width and height
            ws = Home1.winfo_screenwidth()
            hs = Home1.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            Home1.geometry('%dx%d+%d+%d' % (w, h, x, y))
        #Main_Window
        Home1=Tk()
        Home1.title("MVM-Library Recorder")
        Home1.configure(background="white")
        Home1.overrideredirect(1)
        center_window(1200,600)
        Home1.resizable(width=0,height=0)
        #Frames
        Main=Frame(Home1, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Main.pack(side=TOP)
        Title=Frame(Main, width=1265,padx='5',pady='5',relief=RIDGE,bg=X)
        Title.pack(side=TOP)
        Title1=Frame(Main, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Title1.pack(side=TOP)
        Title11=Frame(Title1, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Title11.grid(row=0,column=5)
        Time=Frame(Title1, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Time.grid(row=0,column=0)
        Secinf=Frame(Title1, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Secinf.grid(row=0,column=7)
        Content=Frame(Main,width=1265,padx='20',pady='5',bd=10,relief=RIDGE,bg=X)
        Content.pack()
        BroInf=Frame(Content,width=300,padx='5',pady=5,relief=RIDGE,bg=X)
        BroInf.pack(side=LEFT)
        BroInf1=LabelFrame(BroInf,text="FILL THE INFORMATION'S",width=300,padx='5',pady=5,bd=5,relief=RIDGE,bg=X,fg=Y)
        BroInf1.pack(side=TOP,padx='5',pady='5')
        BookSlc=LabelFrame(Content,text="BOOK'S",padx='5',pady='5',bd=5,relief=RIDGE,bg=X,fg=Y)
        BookSlc.pack(side=LEFT,padx='5',pady='5')
        Details=LabelFrame(Content,text="DETAILS",font=("futura",10),width=300,height=175,padx=5,pady=2,bd=5,bg=X,fg=Y,relief=RIDGE)
        Details.pack(side=LEFT,padx='5',pady='5')
        DisplayR=Text(Details,font=('arial',12,'bold'),width=25,height=14)
        DisplayR.grid(row=0,column=1)
        Butt=Frame(BroInf,width=1265,height=100,padx=2,pady=2,bd=5,relief=RIDGE,bg=X)
        Butt.pack(side=BOTTOM,anchor=SW,pady=5)
        #Pros
        de=date.today()
        fg=de.strftime("%Y-%m-%d")
        kgf=Label(Time,font=("futura",15,"bold"),text="Date:"+fg,bg=X,fg=Y)
        kgf.grid(row=0,column=0,sticky=W)
        li=datetime.now()
        vy=li.strftime("%I:%M %p")
        kgf1=Label(Time,font=("futura",15,"bold"),text="Time:"+vy,bg=X,fg=Y)
        kgf1.grid(row=1,column=0,sticky=W)
        si=Label(Secinf,font=("futura",15,"bold"),text="         Book          ",bg=X,fg=Y)
        si.grid(row=0,column=11,sticky=W)
        si1=Label(Secinf,font=("futura",15,"bold"),text="       Record        ",bg=X,fg=Y)
        si1.grid(row=1,column=11,sticky=W)
        si11=Label(Title11,font=("futura",28,"bold"),text="                Library Book Record \t",bg=X,fg=Y)
        si11.grid(row=1,column=11,sticky=W,padx=10,pady=10)
        JGD=Label(Title,font=("futura",10,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
        JGD.pack()
        Head=Label(Title,font=("futura",30,"bold"),text="             MAHARISHI VIDYA MANDIR          ",bg=X,fg=Y)
        Head.pack()
        HSR=Label(Title,font=("futura",9,"bold"),text="HOSUR",bg=X,fg=Y)
        HSR.pack()
        BookName=Label(BroInf1,text="Book Name:",font=("futura",19,"bold"),bg=X,fg=Y)
        BookName.grid(row=0,column=0,sticky=W)
        BookName1=Entry(BroInf1,font=("futura",19,"bold"),width="25",bd=2)
        BookName1.grid(row=0,column=1)
        BookCode=Label(BroInf1,text="Book Code:",font=("futura",19,"bold"),bg=X,fg=Y)
        BookCode.grid(row=1,column=0,sticky=W)
        BookCode1=Entry(BroInf1,font=("futura",19,"bold"),width="25",bd=2)
        BookCode1.grid(row=1,column=1)
        Cata=Label(BroInf1,text="Book Gener:",font=("futura",19,"bold"),bg=X,fg=Y)
        Cata.grid(row=3,column=0,sticky=W)
        Cata1=ttk.Combobox(BroInf1,font=("futura",19,"bold"),width="24",state="randomly")
        Cata1['values']=["Action","Alternate history","Adventure","Anthology","Art","Biography","Business","economics","Chick lit","Children","Classic","Comic book","Coming of age","Crime","Crafts/hobbies","Cookbook","Diary","Dictionary","Drama","Fairytale","Fantasy","Guide","Graphic novel","Historical fiction","Horror","Health","fitness","History","Home and garden","Humor","Journal","Mystery","Math","Memoir","Paranormal romance","Picture book","Philosophy","Poetry","Prayer","Political thriller","Religion spirituality and new age","Romance","Review","Satire","Science fiction","Short story","Suspense","Science","Self help","Sports and leisure","Textbook","True crime","Thriller","Travel","Western","Young adult"]
        Cata1.grid(row=3,column=1)
        RollNo=Label(BroInf1,text="Author:",font=("futura",19,"bold"),bg=X,fg=Y)
        RollNo.grid(row=2,column=0,sticky=W)
        RollNo1=Entry(BroInf1,font=("futura",19,"bold"),width="25",bd=2)
        RollNo1.grid(row=2,column=1)
        delete=Button(Butt,text="REMOVE",font=("futura",15,"bold"),padx=5,pady=5,bd=3,command=lambda:[clear(),Home1.destroy(),Books(X,Y)])
        delete.grid(padx=7,pady=5,row=0,column=1)
        fst1=Button(Butt,text="   ADD    ",font=("futura",15,"bold"),padx=5,pady=5,bd=3,command=lambda:[sad(),Home1.destroy(),Books(X,Y)])
        fst1.grid(padx=7,pady=5,row=0,column=0)
        exi=Button(Butt,text="GO BACK",font=("futura",15,"bold"),padx=5,pady=5,bd=3,bg="blue",command=lambda:[qui()])
        exi.grid(padx=7,pady=5,row=0,column=500)
#=====================================================================BOOKRECORD_BACKEND====================================================================#
        def qui():
            Home1.destroy()
        def sad():
            a1=BookName1.get()
            b1=BookCode1.get()
            c1=RollNo1.get()
            d1=Cata1.get()
            if(len(a1)>25):
                 messagebox.showinfo("Error!!!","Book Name Entered Is To Long(MAX-25 Characters)")
            elif(len(b1)>10):
                 messagebox.showinfo("Error!!!","Book Code Entered Is To Long(MAX-10 Characters)")
            elif(len(c1)>15):
                 messagebox.showinfo("Error!!!","Author Name Entered Is To Long(MAX-25 Characters)")
            curs.execute("insert into Books values('{}','{}','{}','{}')".format(a1,b1,c1,d1))
            con.commit()
        def ret1(evt):
                    DisplayR.delete(1.0,END)
                    curs1.execute("select Book_Name from Books")
                    iret=curs1.fetchall()
                    kret=[]
                    for ic in range(len(iret)):
                        lk=str(iret[ic][0])
                        pk=[lk]
                        kret=kret+pk
                    value=str(booklist.get(booklist.curselection()))
                    gf=value
                    for i in range(0,len(kret)):
                        if(gf==kret[i]):
                            curs1.execute("select * from Books where Book_Name like '{}'".format(kret[i]))
                            iret1=curs1.fetchall()
                            kret1=[]
                            for ic in range(len(iret1)):
                                lk=str(iret1[ic][0])
                                lk1=str(iret1[ic][1])
                                lk2=str(iret1[ic][2])
                                lk3=str(iret1[ic][3])
                                pk=[lk,lk1,lk2,lk3]
                                kret1=kret1+pk
                            for jkl in range(len(kret1)):
                                if(jkl==(0)):
                                        DisplayR.insert(END,"Name: "+kret1[0])
                                elif(jkl==1):
                                        DisplayR.insert(END,"\n\nCode: "+kret1[1])
                                elif(jkl==2):
                                        DisplayR.insert(END,"\n\nAuthor: "+kret1[2])
                                elif(jkl==3):
                                        DisplayR.insert(END,"\n\nGenre: "+kret1[3])
        curs.execute("select Book_Name from Books")
        iret=curs.fetchall()
        ak=[]
        for ic in range(len(iret)):
                    lk=str(iret[ic][0])
                    pk=[lk]
                    ak=ak+pk
        ListOfBooks=ak
        scrollbar=Scrollbar(BookSlc)
        scrollbar.grid(row=0,column=1,sticky='ns')
        booklist=Listbox(BookSlc,width=25,height=13,font=('arial',12,'bold'))
        booklist.bind('<<ListboxSelect>>',ret1)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)
        for items in ListOfBooks:
                      booklist.insert(END,items)
        def clear():
            ins=messagebox.askyesno("HELP","DO YOU WANT TO DELETE THIS BOOK")
            if(ins>0):
                curs.execute("select Book_Name from Books")
                iret=curs.fetchall()
                kret=[]
                for ic in range(len(iret)):
                        lk=str(iret[ic][0])
                        pk=[lk]
                        kret=kret+pk
                value=str(booklist.get(booklist.curselection()))
                gf=value
                for i in range(0,len(kret)):
                        if(gf==kret[i]):
                            curs.execute("delete from Books where Book_Name='{}'".format(gf))
                            con.commit()
        def srchn1():
            gt=Srch112.get()
            gt1=str(gt)
            curs.execute("select Book_Name from Books")
            iret=curs.fetchall()
            kret=[]
            for ic in range(len(iret)):
                lk=str(iret[ic][0])
                pk=[lk]
                kret=kret+pk
            for i in range(len(kret)):
                    if(gt1.upper()==kret[i].upper()):
                            messagebox.showinfo("Sucess","YEAH!! WE CAN FIND "+gt1.upper()+" IN OUR DATA")
                            ins=messagebox.askyesno("HELP","DO YOU WANT TO DELETE THIS BOOK")
                            if(ins>0):
                                curs.execute("select Book_Name from Books")
                                iret=curs.fetchall()
                                kret=[]
                                for ic in range(len(iret)):
                                        lk=str(iret[ic][0])
                                        pk=[lk]
                                        kret=kret+pk
                                value=str(Srch112.get())
                                gf=value
                                for i in range(0,len(kret)):
                                        if(gf==kret[i]):
                                            curs.execute("delete from Books where Book_Name='{}'".format(gf))
                                            con.commit()
                            break
                    else:
                            if(i==len(kret)-1):
                                    messagebox.showinfo("ERROR","SORRY!! WE COULD NOT FIND "+gt1.upper()+" IN OUR DATA")
        Home1.mainloop()
#===================================================================SIGNUP_FRONTEND_&_BACKEND===============================================================#
def Sign_up(X,Y):
    def center_window(w=300, h=200):
        # get screen width and height
        ws = wind11.winfo_screenwidth()
        hs = wind11.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        wind11.geometry('%dx%d+%d+%d' % (w, h, x, y))
    b=curs1.execute("select * from accounts")
    d=b.fetchall()
    if(d==[]):
        wind11=Tk()
        wind11.title("MVM-Library Recorder")
        wind11.resizable(width=0,height=0)
        wind11.overrideredirect(1)
        center_window(520,340)
        Main=Frame(wind11, width=1265,bd=10,bg=X,relief=RIDGE)
        Main.pack(side=TOP)
        Title=Frame(Main, width=1265,padx='5',pady='5',bd=0,relief=RIDGE,bg=X)
        Title.pack(side=TOP)
        Full=Frame(Main, width=1265,padx='5',pady='5',bd=5,relief=RIDGE,bg=X)
        Full.pack(side=TOP)
        msd=Label(Full,font=("futura",15,"bold"),text="Enter your New Sign UP",bg=X,fg=Y).pack()
        Entr=Frame(Full, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Entr.pack()
        Butt=Frame(Full,width=1265,height=100,padx=5,pady=5,bd=10,relief=RIDGE,bg=X)
        Butt.pack()
        JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
        JGD.pack()
        Head=Label(Title,font=("futura",25,"bold"),text="MAHARISHI VIDYA MANDIR",bg=X,fg=Y)
        Head.pack()
        HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y)
        HSR.pack()
        user=Label(Entr,font=("futura",12,"bold"),text="UserName:",bg=X,fg=Y)
        user.grid(row=0,column=0,sticky=W)
        pas=Label(Entr,font=("futura",12,"bold"),text="Password:",bg=X,fg=Y)
        pas.grid(row=1,column=0,sticky=W)
        user11=Entry(Entr,font=("futura",19,"bold"),width="25",bd=2)
        user11.grid(row=0,column=1)
        pas11=Entry(Entr,font=("futura",19,"bold"),width="25",bd=2,show="*")
        pas11.grid(row=1,column=1)
        lg=Button(Butt,text="Create Account",font=("futura",12,"bold"),command=lambda:[Create(),Sign_in(user11,pas11,X,Y),wind11.destroy()])
        lg.pack(side=RIGHT)
        def Create():
            A111=user11.get()
            B111=pas11.get()
            curs1.execute("insert into accounts values('{}','{}')".format(A111,B111))
            con.commit()
            messagebox.showinfo("Success","Account Created Successfully")
        wind11.mainloop()
    else:
        wind11=Tk()
        wind11.title("MVM-Library Recorder")
        wind11.resizable(width=0,height=0)
        wind11.overrideredirect(1)
        center_window(520,340)
        Main=Frame(wind11, width=1265,bd=10,bg=X,relief=RIDGE)
        Main.pack(side=TOP)
        Title=Frame(Main, width=1265,padx='5',pady='5',bd=0,relief=RIDGE,bg=X)
        Title.pack(side=TOP)
        Full=Frame(Main, width=1265,padx='5',pady='5',bd=5,relief=RIDGE,bg=X)
        Full.pack(side=TOP)
        msd=Label(Full,font=("futura",15,"bold"),text="Verify An Existing Account To Contineue",bg=X,fg=Y).pack()
        Entr=Frame(Full, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
        Entr.pack()
        Butt=Frame(Full,width=1265,height=100,padx=5,pady=5,bd=10,relief=RIDGE,bg=X)
        Butt.pack()
        JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
        JGD.pack()
        Head=Label(Title,font=("futura",25,"bold"),text="MAHARISHI VIDYA MANDIR",bg=X,fg=Y)
        Head.pack()
        HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y)
        HSR.pack()
        user=Label(Entr,font=("futura",12,"bold"),text="UserName:",bg=X,fg=Y)
        user.grid(row=0,column=0,sticky=W)
        pas=Label(Entr,font=("futura",12,"bold"),text="Password:",bg=X,fg=Y)
        pas.grid(row=1,column=0,sticky=W)
        user12=Entry(Entr,font=("futura",19,"bold"),width="25",bd=2)
        user12.grid(row=0,column=1)
        pas12=Entry(Entr,font=("futura",19,"bold"),width="25",bd=2,show="*")
        pas12.grid(row=1,column=1)
        lg=Button(Butt,text="Verify",font=("futura",12,"bold"),command=lambda:[Elsup(wind11)])
        lg.pack(side=RIGHT)
        def Elsup(Z):
            def center_window(w=300, h=200):
                # get screen width and height
                ws = wind11.winfo_screenwidth()
                hs = wind11.winfo_screenheight()
                # calculate position x, y
                x = (ws/2) - (w/2)    
                y = (hs/2) - (h/2)
                wind11.geometry('%dx%d+%d+%d' % (w, h, x, y))
            A111=user12.get()
            B111=pas12.get()
            b=curs1.execute("select * from accounts")
            d=b.fetchall()
            for i in range(0,len(d)):
                if(d[i][0]==A111 and d[i][1]==B111):
                    Z.destroy()
                    wind11=Tk()
                    wind11.title("MVM-Library Recorder")
                    wind11.resizable(width=0,height=0)
                    wind11.overrideredirect(1)
                    center_window(520,340)
                    Main=Frame(wind11, width=1265,bd=10,bg=X,relief=RIDGE)
                    Main.pack(side=TOP)
                    Title=Frame(Main, width=1265,padx='5',pady='5',bd=0,relief=RIDGE,bg=X)
                    Title.pack(side=TOP)
                    Full=Frame(Main, width=1265,padx='5',pady='5',bd=5,relief=RIDGE,bg=X)
                    Full.pack(side=TOP)
                    msd=Label(Full,font=("futura",15,"bold"),text="Enter your New Account Details",bg=X,fg=Y).pack()
                    Entr=Frame(Full, width=1265,padx='5',pady='5',bd=10,relief=RIDGE,bg=X)
                    Entr.pack()
                    Butt=Frame(Full,width=1265,height=100,padx=5,pady=5,bd=10,relief=RIDGE,bg=X)
                    Butt.pack()
                    JGD=Label(Title,font=("futura",12,"bold"),text="JAI GURU DEV",bg=X,fg=Y)
                    JGD.pack()
                    Head=Label(Title,font=("futura",25,"bold"),text="MAHARISHI VIDYA MANDIR",bg=X,fg=Y)
                    Head.pack()
                    HSR=Label(Title,font=("futura",11,"bold"),text="HOSUR",bg=X,fg=Y)
                    HSR.pack()
                    user=Label(Entr,font=("futura",12,"bold"),text="UserName:",bg=X,fg=Y)
                    user.grid(row=0,column=0,sticky=W)
                    pas=Label(Entr,font=("futura",12,"bold"),text="Password:",bg=X,fg=Y)
                    pas.grid(row=1,column=0,sticky=W)
                    user11=Entry(Entr,font=("futura",19,"bold"),width="25",bd=2)
                    user11.grid(row=0,column=1)
                    pas11=Entry(Entr,font=("futura",19,"bold"),width="25",bd=2,show="*")
                    pas11.grid(row=1,column=1)
                    lg=Button(Butt,text="Create Account",font=("futura",12,"bold"),command=lambda:[Create(),wind11.destroy()])
                    lg.pack(side=RIGHT)
                    def Create():
                        A111=user11.get()
                        B111=pas11.get()
                        curs1.execute("insert into accounts values('{}','{}')".format(A111,B111))
                        con.commit()
                        messagebox.showinfo("Success","Account Created Successfully")
                    break
                elif(A111==""and B111==""):
                                messagebox.showinfo("SIGN UP FAILED","Please Enter A Valid Account")
                                break
                else:
                    if(i==len(d)-1):
                        messagebox.showinfo("SIGN UP FAILED","Please Enter A Valid Account")      
        wind11.mainloop()      
#=================================================================SIGIN_FRONTEND_&_BACKEND==================================================================#
def Sign_in(x,y,X,Y):
    Afin=x
    Bfin=y
    a112=Afin
    a113=Bfin
    b=curs1.execute("select * from accounts")
    d=b.fetchall()
    for i in range(0,len(d)):
        if(d[i][0]==a112 and d[i][1]==a113):
            Login_selection2(X,Y)
            break
        elif(a112==""and a113==""):
            messagebox.showinfo("SIGN UP FAILED","Please cheak your Username OR Password")
            break
        else:
            if(i==len(d)-1):
                messagebox.showinfo("SIGN UP FAILED","Please cheak your Username OR Password")
                d=open("Dark.txt","r")
                theme=d.read()
                if(theme=="2"):
                    Acess_verification("gray21","white")
                else:
                    Acess_verification("powder blue","black")
#=======================================================================EXECUTION===========================================================================#        
def Execution():
    curs.execute("select * from Theme")
    theme=curs.fetchall()
    if(theme==[]):
        Acess_verification("powder blue","black")
    else:
        Acess_verification("gray21","white")
Execution()
