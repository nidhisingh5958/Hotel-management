import os
import platform
import mysql.connector

from time import gmtime, strftime
n=strftime("%a, %d %b %Y", gmtime())
n=str(n)
today=n[5:]


global z
mydb = mysql.connector.connect(user='root', password='tiger',host='localhost',database='hotel')
mycursor=mydb.cursor()

print ("\n\n*****WELCOME TO SUNSHINE PARADISE HOTEL*****")
print("            ",n)
print("*" * 126)
print()

import random

def registercust():
             global cid
             
             L = []
             sql = "select * from custdata;"
             mycursor.execute(sql)
             rows = mycursor.fetchall()
             count =len(rows)
             cid= (count+1)

             L.append(cid)
             name=input("enter name:")
             L.append(name)
             addr=input("enter address:")
             L.append(addr)
             indate=input("enter check in date(yyyy-mm-dd):")
             L.append(indate)
             outdate=input("enter check out date(yyyy-mm-dd):")
             L.append(outdate)
             cust=(L)
             sql="insert into custdata(cid,name,addr,indate,outdate)values(%s,%s,%s,%s,%s)"
             mycursor.execute(sql,cust)
             mydb.commit()

             print("Customer Id - ",cid)
def roomtypeview():
              print("Do you want to see room type available? Enter 1 for yes ")
              ch=int(input("enter your choice:"))
              if ch==1:
                           sql="select * from roomtype;"
                           mycursor.execute(sql)
                           rows=mycursor.fetchall()
                           print(rows)
def roomrent():
             global rn
             roomno = []
             # randomly generating room no.
             rn = random.randrange(40)+300
             while rn in roomno:
                          rn = random.randrange(60)+300
                          roomno.append(rn)
             global s        
             print ("We have the following rooms for you:-") 
             print ("1. general---->rs 1000 PN\-")
             print ("2. double bedroom---->rs 4000 PN\-")
             print ("3. deluxe---->rs 10000 PN\-")
             print ("4. suite---->rs 25000 PN\-")
             x=int(input("Enter Your Choice Please->"))
             n=int(input("For How Many Nights Do You Want To Stay:"))
             if(x==1):
                           print ("you have opted room type A")
                           s=1000*n
             elif (x==2):
                           print ("you have opted room type B")
                           s=4000*n
             elif (x==3):
                           print ("you have opted room type C")
                           s=10000*n
             elif (x==4):
                           print ("you have opted room type D")
                           s=25000*n
             else:
                          print ("please choose a room")
                           
             print ("your room rent is =",s,"\n")
             print("your room number is=",rn)
             
             y=input(print('Do you want to continue(y/n):'))
             if y=='n':
                          print("Visit again!!")
                          quit()
             
def restaurentmenuview():
              print("Do you want to see menu available? Enter 1 for yes ")
              ch=int(input("enter your choice:"))
              if ch==1:
                           sql="select * from restaurent;"
                           mycursor.execute(sql)
                           rows =mycursor.fetchall()
                           for x in rows:
                               print(x)
                           y=input(print('Do you want to continue(y/n):'))
                           if y=='n':
                                        print("Visit again!!")
                                        quit()
def orderitem():
             rc=[]
             global r
             print("Do you want to see menu available? Enter 1 for yes ")
             ch=int(input("enter your choice:"))
             if ch==1:
                           sql="select * from restaurent"
                           mycursor.execute(sql)
                           rows=mycursor.fetchall()
                           for x in rows:
                               print(x)
             print("ENTER ZERO(0) WHEN YOU ARE FINISHED GIVING YOUR ORDER")
             d=1
             print("do you want to purchase from above list")
             r=0
             while(ch!=0):
                          d=int(input("enter your choice:"))
                          if(d==1):
                                       print("you have ordered tea")
                                       a=int(input("enter quantity"))
                                       v=10*a
                                       print("your amount for tea is :",v,"\n")
                                       r=r+v
                          elif (d==2):
                                       print("you have ordered coffee")
                                       a=int(input("enter quantity"))
                                       v=10*a
                                       print("your amount for coffee is :",v,"\n")
                                       r=r+v
                          elif(d==3):
                                       print("you have ordered colddrink")
                                       a=int(input("enter quantity"))
                                       v=20*a
                                       print("your amount for colddrink is :",v,"\n")
                                       r=r+v
                          elif(d==4):
                                       print("you have ordered samosa")
                                       a=int(input("enter quantity"))
                                       v=10*a
                                       print("your amount fopr samosa is :",v,"\n")
                                       r=r+v
                          elif(d==5):
                                       print("you have ordered sandwich")
                                       a=int(input("enter quantity"))
                                       v=50*a
                                       print("your amount for sandwich is :",v,"\n")
                                       r=r+v
                          elif(d==6):
                                       print("you have ordered dhokla")
                                       a=int(input("enter quantity"))
                                       v=30*a
                                       print("your amount for dhokla is :",v,"\n")
                                       r=r+v
                          elif(d==7):
                                       print("you have ordered kachori")
                                       a=int(input("enter quantity"))
                                       v=10*a
                                       print("your amount for kachori is :",v,"\n")
                                       r=r+v
                          elif(d==8):
                                       print("you have ordered milk")
                                       a=int(input("enter quantity"))
                                       v=20*a
                                       print("your amount for kachori is :",v,"\n")
                                       r=r+v
                          elif(d==9):
                                       print("you have ordered noodles")
                                       a=int(input("enter quantity"))
                                       v=50*a
                                       print("your amount for noodles is :",v,"\n")
                                       r=r+v
                          elif(d==10):
                                       print("you have ordered pasta")
                                       a=int(input("enter quantity"))
                                       v=50*a
                                       print("your amount for pasta is :",v,"\n")
                                       r=r+v
                          elif (d==0):
                                       break
                          else:
                                       print("please enter your choice from the menu")
             print("Total Bill:",r)
             r=r+1
             rc.append(r)
             y = input(print('Do you want to continue(y/n):'))
             if y == 'n':
                 print("Visit again!!")
                 quit()
             
def laundryview():
              print("Do you want to see rate for laundry? Enter 1 for yes ")
              ch=int(input("enter your choice:"))
              if ch==1:
                           sql="select * from laundryview;"
                           mycursor.execute(sql)
                           rows =mycursor.fetchall()
                           for x in rows:
                               print(x)
                           y=input(print('Do you want to continue(y/n):'))
                           if y=='n':
                                        print("Visit again!!")
                                        quit()
                          
def laundrybill():
              global z
              sql = "select * from laundryview;"
              mycursor.execute(sql)
              rows = mycursor.fetchall()
              for x in rows:
                           print(x)
                          
              y=int(input("Enter your number of clothes->"))
              z=y*10
              print("your laundry bill:",z,"\n")
              return z

def viewbill():
             a=input("enter customer id:")
             print("customer id :",a,"\n")
             K=[]
             K.append(cid)
             K.append(rn)
             K.append(s)
             K.append(r)
             K.append(z)
             Total=(s+r+z)
             K.append(Total)
             tol=(K)
             sql="insert into combill(cid,rno,room_rent,restaurent_bill,laundry_bill,total_bill)values(%s,%s,%s,%s,%s,%s)"
             mycursor.execute(sql,tol)
             mydb.commit()

             print("        *** SUNSHINE PARADISE RECORD ***\n")
             
             ql = ("select * from custdata where cid="+str(a))
             mycursor.execute(ql)
             data = mycursor.fetchone()
             
             print("Customer id --",a)
             print("Name --",data[1])
             print("Address --",data[2])
             print("Check-In date --",data[3])
             print("Check-Out date --",data[4])

             sql=("select * from combill where cid="+str(a))
             mycursor.execute(sql)
             rows =mycursor.fetchone()
             print("Room number --",rows[1])
             print("Room cost -- Rs",rows[2])
             print("Restaurent Bill -- Rs",rows[3])
             print("Laundry Bill -- Rs",rows[4])
             print("Total Price -- Rs",rows[5])

             print(" ")
             print("----------------------------------------------------------------------------------------------------------------------")
      
             

def Menuset():
             print("enter 1: To enter customer data")
             print("enter 2 : To view roomtype")
             print("enter 3 : for calculating room bill")
             print("enter 4 : for viewing restaurent menu")
             print("enter 5 : for restaurent bill")
             print("enter 6 : for viewing laundry rates")
             print("enter 7 : for laundry bill")
             print("enter 8 : for complete bill")
             print("enter 9 : for exit:")
             
             try:
                           userinput=int(input("please select an above option:"))
             except ValueError:
                           exit("\n hi that's not a valid choice")

             if(userinput==1):
                          registercust()
             elif(userinput==2):
                          roomtypeview()
             elif(userinput==3):
                          roomrent()
             elif(userinput==4):
                          restaurentmenuview()
             elif(userinput==5):
                          orderitem()
             elif (userinput == 6):
                          laundryview()
             elif(userinput==7):
                          laundrybill()
             elif(userinput==8):
                          viewbill()
             elif(userinput==9):
                          quit()
             else:
                          print("enter correct choice")
Menuset()

def runagain():
              runagn=input("\n want to run again y/n:")
              while(runagn.lower()=='y'):
                           if(platform.system()=="windows"):
                                       print(os.system('cls'))
                           else:
                               print(os.system('clear'))
                           Menuset()
                           runagn=input("\n want to run again y/n:")
runagain()

