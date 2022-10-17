y='y'
from BMS import admin
from BMS import bank_customer
def initialfirsttime():
    import random
    import mysql.connector
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bank_management_system")
    cur=con.cursor()
    cur.execute("CREATE TABLE bank_customer(Aadharno char(12) NOT NULL PRIMARY KEY, Accountno integer NOT NULL, Name varchar(30) NOT NULL, DateofBirth date NOT NULL, Gender char(1) NOT NULL,Contact integer,PanCard char(10),Amount integer,BankAccountType integer, PinNo integer NOT NULL, Billamount numeric)")
    cur.execute("INSERT INTO bank_customer VALUES(123456781234,456789,'Somesh Ghosh','2004-08-04','M',3975,NULL,1000000,1,5645,NULL)")
    cur.execute("INSERT INTO bank_customer VALUES(253454568234,892623,'Subham Sen','2003-07-01','M',9975,NULL,10045,2,4863,NULL)")
    cur.execute("CREATE TABLE bc456789 ( Typeoftransaction char(20) , Date char(30) , Time char(30) , Amount char(20) , Type char(10))")
    cur.execute("CREATE TABLE bc892623 ( Typeoftransaction char(20) , Date char(30) , Time char(30) , Amount char(20) , Type char(10))")
    con.commit()
print("")
print("")
print("************ SOMESH BANK ************")
print("")
print("Welcome to our Bank's console application")
print("")
initialfirsttime()
while y=='y':
    print("Are you an Admin or Customer")
    print(" A=Admin")
    print(" B=Bank Customer")
    x=input("==>")
    if x=="A":
        print("")
        y='a'
        admin.run()
    elif x=="B":
        print("")
        y='a'
        bank_customer.run()
    else:
        print("Invalid Choice!! Try again")
        y='y'

