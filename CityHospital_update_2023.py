import sys
import datetime
from tabulate import tabulate
from colored import fg, bg, attr
import time 
from maskpass import askpass
import mysql.connector as msql
def l():
    print("="*100)
print("="*100)
print("""This Project is Made By:
Abhinav Kumar
School:Jusco School South Park""")
l()
print("%s**********Welcome To City Hospital Estd.1920 **********%s"%(fg(10),attr(0)))
try:
    global mycon
    print("\n")
    print("Enter Password For Database: ")
    pd=askpass()
    mycon=msql.connect(host="localhost",user="root",password=pd)
    medthon=mycon.cursor()
    try:
        medthon.execute("create database test;")
        medthon.execute("use test;")
        medthon.execute("create table patient(PID int(5) unique,Name varchar(40),Blood_group varchar(3),Registration_Date varchar(20),Admitted_on varchar(20),Discharged_on varchar(20),Ailment varchar(30),Age int(3),Contact_number varchar(11),SEX char(1),Ward varchar(20),Bill int(7) default 500);")
        medthon.execute("insert into patient(PID,Name,Blood_group,Registration_Date,Admitted_on,Age,SEX,ward,Ailment,Contact_number) values(10007,'Sham','B+','2021-01-05 12:34','2021-01-28 12:34',34,'M','General_W.','Malaria',912173314),(10006,'Sheily','B+','2021-01-25 02:34','2021-01-15 19:34',18,'F','Isolation_W.','Covid19',9192345678);")
        medthon.execute("create table ward(WID int(3),Name varchar(15), Fees int(7),Total_beds integer(5) ,Available integer(5)); ")
        medthon.execute("insert into ward values(01,'General_W.',499,350,172),(02,'VIP_W.',6980,80,47),(03,'ICU_W.',2500,50,39),(04,'Isolation_W.',1699,150,90);")
        medthon.execute("create table doctors(DID int(5) , Name varchar(40), Department varchar(20),Post varchar(20));")
        medthon.execute("insert into doctors values(10001,'Dr.Divyanshu','Ophthalmology','Sr. Asst.'),(10002,'Dr.Astha','Cardiology','Sr.'),(10003,'Dr.Abhinav','Psychiatry','Jr.'),(10004,'Dr.Pooja','Oncology','Jr.');")
        medthon.execute("create table Supplies(SID int(5),Item varchar(50),Quantity int(100));")
        medthon.execute("insert into supplies values(100,'Bandages',300);")
    except:
        medthon.execute("use test;")


except:
    print("Invalid Details, Check MySql Directory and Try again..")
    time.sleep(10)
    sys.exit()

print("Initialized.... ")
#Password_AdminMode:<420>
#i1---- for option1
#i ---- mainmenu
#i4---- passscodeOfAdminMode
#i5---- adminMenuInput
limit=3
def l1():
    print("-"*100)
def pcall():
    medthon.execute("select Name,Available from ward group by name;")
    b=medthon.fetchall()
    beds=tabulate(b)
    print(beds)
p=6
def welcome():
    print("\n")
    print("%s**********Welcome To City Hospital **********%s"%(fg(10),attr(0)))
    print("\n")
def mainmenu():
    l()
    print("%s####MAIN MENU####%s"%(fg(172),attr(0)))
    print("1.Check Availability")
    print("2.Registration")
    print("3.Patient Profile")
    print("4.Admin Access")
    print("5.Discharge Patient")
    print("%s6.QUIT%s"%(fg(9),attr(0)))
    l1()
    global i 
    i=input("Enter Your Choice: ")
def AdminMenu():
    print("1.Doctor details")
    print("2.Staff details")
    print("3.Patient details")
    print("4.Supplies")
    print("5.Back To Main Menu")
    

def option1(): #for availability
    l()
    print("%s####Available####%s"%(fg(29),attr(0)))
    print("1.Doctors")
    print("2.Hospital Beds")
    print("3.Facilities")
    print("4.Back To Main Menu")
    l1()
    i1=input("Enter Your Choice: ")
    l()
    if i1=='1':
            medthon.execute("select name,department from doctors")
            output=medthon.fetchall()
            print("Doctors Availaible: ")
            print(tabulate(output,headers=["Name","Department"]))
            print("\n")
            a=input("Press ENTER to jump to AVAILABILITY MENU")
            option1()
    elif i1=='2':
        print("%sNumber of Beds Available are: %s"%(fg(142),attr(0)))
        pcall()
        print("\n")
        a=input("Press ENTER to jump to AVAILABILITY MENU ")
        option1()
    elif i1=='3':
        print("""%sList Of World-Class facilities:

>OPD (Allopathy & Homeopathy)
>Dental facility
>Ward/ Indoor facility
>Minor OT/ Dressing Room
>Physiotherapy
>Laboratory services
>ECG Services
>Pharmacy
>Radiology/X-ray facility
>Ambulance Services
\n%s"""%(fg(136),attr(0)))
        print("RETURNING TO AVAILABILITY MENU....")
        time.sleep(4)
    else:
        mainmenu()
        
def option2(): #for registration
    l()
    print("---Welcome To Registration Window---")
    #Name|Age|Gender|BloodGroup|AppointmentDate|Problem/Error|Contact No.|Ward
    medthon.execute("select max(pid) from patient;")
    s=medthon.fetchone()
    global idp
    idp=s[0]+1
    global name
    name=input("Enter Patient's Name: ")
    global age
    age=input("Enter Patient's Age: ")
    global gender
    gender=input("Enter Sex(M/F/T): ")
    global bldgrp
    bldgrp=input("Enter Blood Group(OPTIONAL): ")
    global aptdate
    aptdate=dt()
    global er
    er=input("Describe Ailment (UNDER 15 CHARACTERS): ")
    global num
    num=input("Enter Contact Number: ")
    ask()
    print("Updated Successfully")
    l1()
    print("Your patient ID generated is: ",idp,"\nPLEASE SAVE THIS FOR FUTURE REFERENCE")
    print("\n")
    a=input("Press ENTER to jump to MAIN MENU")
    mainmenu()
def option3():#for profile and Bill
    try:
        l()
        pid=input("Enter Your Patient ID: ")
        l1()
        medthon.execute("select * from patient where PID=%s"%(pid,))
        output=medthon.fetchone()
        print("Patient name      >",output[1])
        print("Blood group       >",output[2])
        print("Registration Date >",output[3])
        print("Admitted on       >",output[4])
        print("Discharged on     >",output[5])
        print("Ailment           >",output[6])
        print("Age               >",output[7])
        print("Sex               >",output[9])
        print("Contact Number    >",output[8])
        print("Ward              >",output[10])
        print("Bill              >Rs.",output[11])
        print("\n")
        a=input("Press ENTER to jump to MAIN MENU")
    except:
        print("\n")
        print("Patient Not Found!!")
        print("\n")
        mainmenu()
    mainmenu()
def adminpassword(limit):
    if limit!=0:
        l()
        print("%s*****Encrypted Window Enter Pass Code To Enter*****%s"%(fg(96),attr(0)))
        password=askpass()
        if password=="420":
            global p
            p=420
            adminmenue()
        else:
            print("%sWRONG PASS CODE%s"%(fg(9),attr(0)), limit-1,"chances left")
            adminpassword(limit-1)
    else:
        print("%s*** UNAUTHORIZED ACCESS***%s"%(fg(5),attr(0)))
        print("\n")
        print("***Going Back To Main Menu***")
        print("\n")
        p=0
        mainmenu()
        
def adminmenue():
    if p==420:
        print("="*100)
        print("%s********Welcome Admin*******%s"%(fg(35),attr(0)))
        print("1.Doctor Details")
        print("2.Ward Details")
        print("3.Patient Details")
        print("4.Supplies")
        print("5.Back To Main Menu")
        print('\n')
        i5=input("Enter Your Choice: ")
        if i5=='5':
            print("\n")
            mainmenu()
        elif i5=='4':
            l1()
            print("""1.To View Supplies
2.To Add Supplies
3.To Delete Supplies
4.To Update Supplies""")
            print("\n")
            i6=input("Enter Your Choice: ")
            if i6=='1':
                l1()
                print("-----Supplies-----")
                medthon.execute("select * from supplies")
                output=medthon.fetchall()
                print(tabulate(output,headers=["SID","Name","Quantity"]))
                print("\n")
                a=input("Press ENTER to Continue")
            elif i6=='2':
                try:
                    medthon.execute("select max(sid) from supplies;")
                    s=medthon.fetchone()
                    did=s[0]+1
                    name=input("Enter Name Of Item: ")
                    quan=input("Enter Quantity: ")
                    medthon.execute("insert into supplies values('{0}','{1}','{2}')".format(int(did),name,quan))
                    mycon.commit()
                    print("%sUpdated Successfully%s"%(fg(35),attr(0)))
                except:
                    print("Invalid Entry, Try Again")
                adminmenue()
            elif i6=='3':
                try:
                    medthon.execute("select * from supplies")
                    output=medthon.fetchall()
                    print(tabulate(output,headers=["SID","Name","Quantity"]))
                    print("\n")
                    a=input("Enter Item ID to be Deleted: ")
                    medthon.execute("delete from supplies where sid='{0}'".format(int(a)))
                    print("Data Deleted!")
                except:
                    print("Invalid Entry, Try Again")
                adminmenue()
            elif i6=='4':
                medthon.execute("select * from supplies")
                output=medthon.fetchall()
                print(tabulate(output,headers=["SID","Name","Quantity"]))
                print("\n")
                a=input("Enter Item ID to be Updated: ")
                n=input("Enter Quantity: ")
                try:
                    medthon.execute("update supplies set quantity='{0}' where sid='{1}';".format(int(n),int(a)))
                    mycon.commit()
                    print("%sUpdated Successfully%s"%(fg(35),attr(0)))
                except:
                    print("Invalid Entry, Try Again")
                adminmenue()
                
                
        elif i5=='1':
            l1()
            print('''Options: 
1.To View DocDetails
2.To Add DocDetails
3.To Delete DocDetails
4.To Update DocDetails
5.To Search DocDetails
6.Return To AdminMenu''')
            print("\n")
            i6=input("Enter Your Choice: ")
            if i6=='1':
                medthon.execute("select * from doctors")
                output=medthon.fetchall()
                l1()
                print("-----DOCTORS-----")
                print(tabulate(output,headers=["ID","Name","Department","Post"]))
                print('\n')
                a=input("Press ENTER to jump to Admin Menu")
                option4()   
            elif i6=='2':
                medthon.execute("select max(did) from doctors;")
                s=medthon.fetchone()
                did=s[0]+1
                name=input("Enter Name Of Doctor: ")
                dept=input("Enter Department: ")
                post=input("Enter Post: ")
                medthon.execute("insert into doctors values('{0}','{1}','{2}','{3}')".format(int(did),name,dept,post))
                mycon.commit()
                print("%sUpdated Successfully%s"%(fg(35),attr(0)))
                print("\n")
                a=input("Press ENTER to jump to AdminMenu")
                adminmenue()
            elif i6=='3':
                medthon.execute("select * from doctors")
                output=medthon.fetchall()
                print("\n")
                print("-----DOCTORS-----")
                print(tabulate(output,headers=["ID","Name","Department","Post"]))
                print('\n')
                a=input("Enter ID to be deleted: ")
                medthon.execute("select * from doctors where DID='{0}'".format(a,))
                t=medthon.fetchall()
                if len(t)==0:
                    print("Doctor Not Found!!")
                else:    
                    medthon.execute("delete from doctors where DID='{0}'".format(a,))
                    mycon.commit()
                    print("Data Deleted!")
                    adminmenue()
            elif i6=='4':
                    medthon.execute("select * from doctors")
                    output=medthon.fetchall()
                    l1()
                    print("-----DOCTORS-----")
                    print(tabulate(output,headers=["ID","Name","Department","Post"]))
                    print('\n')
                    z=int(input("Enter Doctor's ID To Be Updated: ")) 
                    print("""Select Field To Be Updated:
1.Name
2.Department
3.Post""")
                    n=input("Enter Your Choice(1~3): ")
                    if n=='1':
                        c=input("Enter Updated Name: ")
                        medthon.execute("update doctors set Name='{0}' where DID='{1}';".format(c,z))
                        mycon.commit()
                        print("\n")
                        print("Updated Succesfully")
                    elif n=='2':
                        c=input("Enter Updated Department: ")
                        medthon.execute("update doctors set Department='{0}' where DID='{1}';".format(c,z))
                        mycon.commit()
                        print("\n")
                        print("Updated Succesfully")
                    elif n=='3':
                        c=input("Enter Updated Post: ")
                        medthon.execute("update doctors set Post='{0}' where DID='{1}';".format(c,z))
                        mycon.commit()
                        print("\n")
                        print("Updated Succesfully")
            elif i6=='5':
                try:
                    z=int(input("Enter Doctor's ID To Be Searched: "))
                    medthon.execute("select * from doctors where DID='{0}';".format(int(z)))
                    output=medthon.fetchall()
                    if output==[]:
                        huhu()
                    l1()
                    print(tabulate(output,headers=["ID","Name","Department","Post"]))
                    l1()
                    adminmenue()
                except:
                    print("Invalid Entry Detected ... Try Again")
                    adminmenue()    
            else:
                option4()
        elif i5=='3':
            l1()
            medthon.execute("select * from patient")
            output=medthon.fetchall()
            print("-----PATIENTS-----")
            print(tabulate(output,headers=["PID","Name","BloodGroup","Registered.ON","Admitted.ON","Discharged.ON","Ailment","Age","Contact","SEX","Ward","Bill"]))
            print("\n")
            a=input("Press ENTER to Continue")
        elif i5=='2':
            l1()
            medthon.execute("select * from ward;")
            output=medthon.fetchall()
            print("-----WARDS-----")
            print('''Options: 
1.To View Ward Details
2.To Add  New Ward Details
3.To Delete Ward Details
4.To Update Ward Details
5.Return To AdminMenu\n''')
            iw=input ("Enter your choice(1~4): ")
            l1()
            if iw=='1':
               print(tabulate(output,headers=["WID","Name","Fees","Total Beds","Available"]))
               print("\n")
               a=input("Press ENTER to Continue")
            elif iw=='2':
                medthon.execute("select max(wid) from ward;")
                s=medthon.fetchone()
                wid=s[0]+1
                name=input("Enter Name Of Ward: ")
                fee=input("Enter Fees: ")
                fee=int(fee)
                dept=input("Enter Total Beds: ")
                post=input("Enter Available Beds: ")
                medthon.execute("insert into ward values('{0}','{1}','{2}','{3}','{4}')".format(int(wid),name,int(fee),int(dept),int(post)))
                mycon.commit()
                print("%sUpdated Successfully%s"%(fg(35),attr(0)))
                l1()
                print("\n")
                a=input("Press ENTER to jump to AdminMenu")
                adminmenue()
            elif iw=='3':#Deleting empyty wards only
                print(tabulate(output,headers=["WID","Name","Fees","Total Beds","Available"]))
                print("\n")
                al=input("Enter Ward ID to be deleted: ")
                medthon.execute("select ward from patient where Admitted_on is not null and discharged_on is null")
                oL=medthon.fetchall()#List of wards which is not empty
                medthon.execute("select name from ward where wid='{0}';".format(int(al)))
                oN=medthon.fetchone()
                oN=oN[0]
                oN=(oN,)#Name of Ward
                l=len(oL)
                if oN in oL:
                    print("%sWard Is Not Empyty, Unable To Remove Data!!%s"%(fg(1),attr(0)))
                    iw=''
                else:
                    medthon.execute("delete from ward where wid='{0}';".format(int(al)))
                    print("Data Deleted!")
                    mycon.commit()
                    l1()
                adminmenue()
            elif iw=='4':#Updating
                print(tabulate(output,headers=["WID","Name","Fees","Total Beds","Available"]))
                print("\n")
                al=input("Enter Ward ID to be Updated: ")
                fee=input("Enter New Fees: ")
                fee=int(fee)
                dept=input("Enter New Total Beds: ")
                medthon.execute("select name from ward where wid={0};".format(int(al)))
                sn=medthon.fetchone()
                sn=sn[0]
                medthon.execute("select count(*) from patient where Admitted_on is not null and discharged_on is null and ward='{0}' group by ward;".format((sn)))
                A=medthon.fetchone()
                if A==None:
                    A=0
                else:
                    A=A[0]
                post=int(dept)-int(A)
                medthon.execute("update ward set available='{0}',fees='{1}',Total_beds='{2}' where wid='{3}';".format(int(post),int(fee),int(dept),int(al)))
                mycon.commit()
                print("%sUpdated Successfully%s"%(fg(35),attr(0)))
                l1()
        elif i5=='5':
            mainmenu()           
def option4(): #for admin mode
    if p==420:
        adminmenue()
    elif p==6:
        adminpassword(3)
    elif p==0:
        print("%s ### PASSWORD LIMIT EXCEEDED ###%s"%(fg(9),attr(0)))
        mainmenu()
def option5():
    mycon.close()
    l()
    print("%sThank You For Visiting......%s"%(fg(14),attr(0)))
    time.sleep(3.5)
    sys.exit()
def option6():
     l1()
     medthon.execute("select Pid,name,Admitted_on,ward from patient where Admitted_on is not null and discharged_on is null")
     output=medthon.fetchall()
     print("-----PATIENTS-----")
     print(tabulate(output,headers=["PID","Name","Admitted.ON","Ward"]))
     print("\n")
     if output==[]:
         print("No Patient To Be Discharge!")
         mainmenu()
     global d
     try:
         d=int(input("Enter PID to be Discharged: "))
         bill(d)
     except:
         print("Invalid Entry..")
         mainmenu()
def bill(a):
    medthon.execute("select admitted_on from patient where pid='{0}'".format(int(a)))
    output=medthon.fetchone()
    s=output[0]
    str(s)
    y=s[0:4]
    y=int(y)
    m=s[5:7]
    m=int(m)# 2021-01-05 12:34
    d=s[8:10]
    d=int(d)
    now=datetime.datetime.now()
    q=str(now)
    y1=q[:4]
    y1=int(y1)
    m1=q[5:7]
    m1=int(m1)
    d1=q[8:10]
    d1=int(d1)
    from datetime import date
    f_date=date(y1,m1,d1)
    l_date=date(y,m,d)
    delta=f_date-l_date
    c=delta.days
    c=int(c)+1
    medthon.execute("select ward from patient where pid='{0}'".format(int(a)))
    output=medthon.fetchone()
    med=10.5*c
    i1=output[0]
    medthon.execute("select fees from ward where name='{0}'".format(i1))
    output=medthon.fetchone()
    i=output[0]
    i=int(i)
    r2=c*i
    r=r2+199+500+int(med)
    medthon.execute("select wid from ward where name='{0}'".format(i1))
    output1=medthon.fetchone()
    i1=output1[0]
    i1=int(i1)
    medthon.execute("select available from ward where wid='{0}';".format(int(i1)))
    b=medthon.fetchone()
    z=b[0]+1
    c=int(z)
    medthon.execute("update ward set available='{0}' where wid='{1}';".format(int(c),int(i1)))
    mycon.commit()
    q=dt()
    global r1
    r1=r
    global r3
    r3=r2
    medthon.execute("update patient set bill='{0}' where pid='{1}';".format(int(r),int(a)))
    medthon.execute("update patient set Discharged_on='{0}' where pid='{1}';".format(q,int(a)))
    mycon.commit()
    billshow(r1,a,q,med,r3)
def billshow(b,p,d,t,r3):
    l()
    medthon.execute("select name from patient where pid='{0}';".format(p))
    o=medthon.fetchone()
    n=o[0]
    l1()
    print("%sCity Hospital Estd.1920\n%s"%(fg(10),attr(0)))
    print(">Name            :Mr/Ms.",n)
    print(">Doctor Fees     :Rs. 199")
    print(">Medicine Charges:Rs.",t)
    print(">Basic Charge    :Rs. 500")
    print(">Bed Charges     :Rs.",r3)
    l1()
    print(">Patient's Total Bill:Rs.",b)
    print("\n")
    l()
    mainmenu()
def dt():
    now=datetime.datetime.now()
    s=str(now)
    z=s[:16]
    return z
def ask():
    print("""Select :
          1.OPD REGISTRATION
          2.Ward Admission \n""")
    s=input("Enter Your Choice(1~2): ")
    l1()
    if s=='2':
        medthon.execute("select Wid,Name,Fees from ward;")
        z=medthon.fetchall()
        print(tabulate(z,headers=["ID","Name","Fees"]))
        print("\n")
        A=input("Please Choose Desired Ward ID From List Above: ") 
        A1=int(A)
        medthon.execute("select available from ward where wid='{0}';".format(int(A1)))
        b=medthon.fetchone()
        z=b[0]-1
        c=int(z)
        medthon.execute("update ward set available='{0}' where wid='{1}';".format(int(c),int(A1)))
        mycon.commit()
        medthon.execute("select name from ward where wid='{0}';".format(int(A1)))
        output=medthon.fetchone()
        A=output[0]
        mycon.commit()
        try:
            medthon.execute("insert into patient(Name,Blood_group,Registration_Date,Ailment,Age,Contact_number,PID,SEX,Admitted_on,ward) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(name,bldgrp,aptdate,er,age,num,idp,gender,aptdate,A))
            mycon.commit()
        except:
            print("Invalid Entry Detected ... Try Again")
            option2()
    elif s=='1':
        try:
            medthon.execute("insert into patient(Name,Blood_group,Registration_Date,Ailment,Age,Contact_number,PID,SEX) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(name,bldgrp,aptdate,er,age,num,idp,gender))
            mycon.commit()
        except:
            print("Invalid Entry Detected ... Try Again")
            option2()
    else:
       print("Invalid Entry Detected ... Try Again")
       option2() 
#MainProgram
mainmenu()
while limit==3:
    if i=='1':
        option1()
    elif i=='2':
        option2()
    elif i=='3':
        option3()
    elif i=='4':
         option4()
    elif i=='5':
        option6()
    elif i=='6':
        option5()
    else:
        mainmenu()
 
                   
                                                                         
