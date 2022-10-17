def initialeverytime():
    import random
    import mysql.connector
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bank_management_system")
    cur=con.cursor()
    return con,cur
    
def run():
    initialeverytime()
    menu()
    a=0
    a=int(input("-->"))
    decide(a)

def dateandtime():
    import datetime
    today=datetime.date.today()
    date=datetime.date.isoformat(today)
    x=datetime.datetime.now()
    time=str(x.hour)+"-"+str(x.minute)+"-"+str(x.second)
    return date,time


def menu():
    print("")
    print("")
    print("*****  MAIN MENU  ********")
    print("")
    print("1. Create New Bank Account")
    print("2. Update self Intro")
    print("3. Transfer Money")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Apply for loan and Approval")
    print("7. Bill Payment")
    print("8. View Account Statement")
    print("0. Quit")

def redirecttomenu():
    print("To go back to main menu - enter yes")
    print("To end - enter no")
    while True:
        a=input("--->")
        if a=="yes":
            run()
            break
        elif a=="no":
            break
        else:
            print("Invalid Choice!! Try again")

def verify():
    con,cur=initialeverytime()
    a=0
    p=0
    while a==0:
        accno=int(input("Enter your Account No. : "))
        pin=int(input("Enter your Pin No. : "))
        cur.execute("SELECT Accountno,PinNo FROM bank_customer")
        for i in cur:
            if i[0]==accno and i[1]==pin:
                a=a+1
                x=accno
                y=pin
        if a==0:
            p=p+1
            print("Invalid Credentials. Try again")
            print('Number of attempts left:',3-p)
        if p==3:
            print("Attempts exhausted. The menu deriven program is stopped")
            print("Contacts your nearest branch to unlock your account")
            break
    return x

def balance(accno):
    con,cur=initialeverytime()
    cur.execute("SELECT Accountno, Amount FROM bank_customer")
    for i in cur:
        if accno==i[0]:
            return i[1]
    

def decide(a):
    if a==1:
        bc1()
    elif a==2:
        bc2()
    elif a==3:
        bc3()
    elif a==4:
        bc4()
    elif a==5:
        bc5()
    elif a==6:
        bc6()
    elif a==7:
        bc7()
    elif a==8:
        bc8()
    elif a==0:
        bc0()
    else:
        print("Invalid Choice!! Try again")
        run()

def loan(loanamount,tenure):
    from math import pow
    print("Which type of loan do you want to take?")
    print("1 : Personal Loan")
    print("2 : Car Loan")
    print("3 : Education Loan")
    print("4 : Home Loan")
    a=int(input("-->"))
    if a==1:
        print("Interest Rate : 10.5%")
        roi=10.5
        amount = loanamount * ( pow (( 1 + roi / 100 ), tenure))
        print("Total interest : ",amount-loanamount)
        print("Total amount you have to pay with interest : ",amount)
    elif a==2:
        print("Interest Rate : 10.5%")
        roi=10.5
        amount = loanamount * ( pow (( 1 + roi / 100 ), tenure))
        print("Total interest : ",amount-loanamount)
        print("Total amount you have to pay with interest : ",amount)
    elif a==3:
        print("Interest Rate : 10.5%")
        roi=10.5
        amount = loanamount * ( pow (( 1 + roi / 100 ), tenure))
        print("Total interest : ",amount-loanamount)
        print("Total amount you have to pay with interest : ",amount)
    elif a==4:
        print("Interest Rate : 10.5%")
        roi=10.5
        amount = loanamount * ( pow (( 1 + roi / 100 ), tenure))
        print("Total interest : ",amount-loanamount)
        print("Total amount you have to pay with interest : ",amount)
    else:
        print("Invalid Choice!! Try again")
    print("Congratulations! Your loan is successfully approved")
    redirecttomenu()


def bc0():
    print("Thank you for using bank management system.")
    print("Have a nice day !!")
    
    
def bc1():
    con,cur=initialeverytime()
    name=input("Enter your name : ")
    aadhar=int(input("Enter Aadhar Number : "))
    pan=input("Enter Pan Card Number : ")
    amt=input("Enter Amount deposited : ")
    contact=input("Enter Contact Number : ")
    dob=input("Enter your Date of Birth in YYYY-MM-DD format : ")
    gender=input("Enter your gender ( M,F,T ) : ")
    print("Which type of account you want to open?")
    while True:
        acctype=input("1. Saving  2. Current  3. Fixed Deposit : ")
        if acctype in "123":
            break
        print("Please use 1, 2 or 3 for selecting")
    import random
    acc=random.randint(100000,999999)
    pin=random.randrange(1000,9999)
    print("Your Account Number is : ", acc)
    print("Your Pin Number is : ", pin)
    t=(aadhar,acc,name,dob,gender,contact,pan,amt,acctype,pin)
    query="INSERT INTO bank_customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL)"
    cur.execute(query,t)
    con.commit()
    acc="bc"+str(acc)
    cur.execute("CREATE TABLE %s ( Typeoftransaction char(20) , Date DATE , Time TIME , Amount numeric , Type char(10))"%(acc,))
    con.commit()
    print("Your account details is successfully saved to the bank")
    redirecttomenu()
    
    
def bc2():
    con,cur=initialeverytime()
    accno=verify()
    print("What do you want to update?")
    print("1 : Name")
    print("2 : Date of Birth")
    print("3 : Pan Card Number")
    print("4 : Contact Number")
    a=int(input("-->"))
    if a==1:
        name=input("Enter your name : ")
        t=(name,accno)
        query="UPDATE bank_customer SET Name=%s WHERE Accountno=%s"
        cur.execute(query,t)
        con.commit()
        print("Your details have been successfully updated.")
    elif a==2:
        dob=input("Enter your Date of Birth in YYYY-MM-DD format : ")
        t=(dob,accno)
        query="UPDATE bank_customer SET DateofBirth=%s WHERE Accountno=%s"
        cur.execute(query,t)
        con.commit()
        print("Your details have been successfully updated.")
    elif a==3:
        pan=input("Enter Pan Card Number : ")
        t=(pan,accno)
        query="UPDATE bank_customer SET PanCard=%s WHERE Accountno=%s"
        cur.execute(query,t)
        con.commit()
        print("Your details have been successfully updated.")
    elif a==4:
        contact=input("Enter Contact Number : ")
        t=(contact,accno)
        query="UPDATE bank_customer SET Contact=%s WHERE Accountno=%s"
        cur.execute(query,t)
        con.commit()
        print("Your details have been successfully updated.")
    else:
        print("Invalid Choice!! Try again")
    redirecttomenu()


def bc3():
    con,cur=initialeverytime()
    accno=verify()
    moneytransfer=int(input("Amount of money to be transferred : "))
    receiveraccno=int(input("Enter receiver account number : "))

    t1=(moneytransfer,accno)
    query1="UPDATE bank_customer SET Amount=Amount-%s WHERE Accountno=%s"
    t2=(moneytransfer,receiveraccno)
    query2="UPDATE bank_customer SET Amount=Amount+%s WHERE Accountno=%s"
    cur.execute(query1,t1)
    con.commit()
    cur.execute(query2,t2)
    con.commit()

    date,time=dateandtime()

    accno="bc"+str(accno)
    moneytransfer=str(moneytransfer)
    query="INSERT INTO "+accno+" VALUES( 'Money Transfer'" + " , '"+ date + "' , '" + time + "' , " + moneytransfer + " , " + " 'Debit' )"
    cur.execute(query)
    con.commit()

    receiveraccno="bc"+str(receiveraccno)
    query="INSERT INTO "+receiveraccno+" VALUES( 'Money Transfer'" + " , '"+ date + "' , '" + time + "' , " + moneytransfer + " , " + " 'Credit' )"
    cur.execute(query)
    con.commit()

    print("Amount successfully transferred.")
    redirecttomenu()


def bc4():
    con,cur=initialeverytime()
    accno=verify()
    moneydeposit=input("Amount of money to be deposited : ")
    t=(moneydeposit,accno)
    query="UPDATE bank_customer SET Amount=Amount+%s WHERE Accountno=%s"
    cur.execute(query,t)
    con.commit()
    date,time=dateandtime()
    accno="bc"+str(accno)
    moneydeposit=str(moneydeposit)
    query="INSERT INTO "+accno+" VALUES( 'Money Deposit'" + " , '"+ date + "' , '" + time + "' , " + moneydeposit + " , " + " 'Credit' )"
    cur.execute(query)
    con.commit()
    print("Amount successfully deposited.")
    redirecttomenu()

def bc5():
    con,cur=initialeverytime()
    accno=verify()
    moneywithdraw=input("Amount of money to be withdrawn : ")
    t=(moneywithdraw,accno)
    query="UPDATE bank_customer SET Amount=Amount-%s WHERE Accountno=%s"
    cur.execute(query,t)
    con.commit()
    date,time=dateandtime()
    accno="bc"+str(accno)

    moneywithdraw=str(moneywithdraw)
    query="INSERT INTO "+accno+" VALUES( 'Money Withdraw'" + " , '"+ date + "' , '" + time + "' , " + moneywithdraw + " , " + " 'Debit' )"
    
    cur.execute(query)
    con.commit()
    print("Amount successfully moneywithdrawn.")
    redirecttomenu()

def bc6():
    con,cur=initialeverytime()
    accno=verify()
    salary=input("Enter your annual salary : ")
    print("Are you working in Government Organisation/Public Sector Undertakings/PSBs, MNCs or any Reputed Companies")
    print("Enter yes or no")
    a=input("--->")
    while True:
        if a=="yes":
            break
        elif a=="no":
            break
        else:
            print("Invalid Choice!! Try again")
    gross10month=salary*0.83
    #The loan amount is normally equivalent to 10 months gross salary. 
    tenure=input("Enter your job tenure : ")
    loanamount=input("How much amount you want as loan")
    if tenure>=2 and loanamount<=gross10month and a=="yes":
        print("Congratulations! You are eligible for loan.")
        loan(loanamount,tenure)
    else:
        print("Sorry, you are not eligible for loan.")

    
def bc7():
    con,cur=initialeverytime()
    accno=verify() 
    billamount=input("Enter the amount you need to pay for the bill : ")
    x=balance(accno)
    print('Old balance : ',x)
    t=(billamount,accno)
    query="UPDATE bank_customer SET Billamount=Billamount-%s WHERE Accountno=%s"
    cur.execute(query,t)
    con.commit()
    t=(billamount,accno)
    query="UPDATE bank_customer SET Amount=Amount-%s WHERE Accountno=%s"
    cur.execute(query,t)
    con.commit()
    x=balance(accno)
    print('New balance : ',x)
    date,time=dateandtime()
    accno="bc"+str(accno)

    billamount=str(billamount)
    query="INSERT INTO "+accno+" VALUES( 'BILL PAYMENT'" + " , '"+ date + "' , '" + time + "' , " + billamount + " , " + " 'Debit' )"
    
    cur.execute(query)
    con.commit()
    
    print("Bill payment has been done successfully.")
    redirecttomenu()

def bc8():
    con,cur=initialeverytime()
    accno=verify()
    print("")
    accno="bc"+str(accno)
    query="SELECT * FROM "+accno
    cur.execute(query)
    for i in cur:
        print(i[0],"on",i[1],"at",i[2],"by",i[3],"type=",i[4])

    print("")
    redirecttomenu()
    
