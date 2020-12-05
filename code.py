import re
import sqlite3
con=sqlite3.connect('student.db')
c=con.cursor()
c.execute("""  CREATE TABLE IF NOT EXISTS Studentdata
(
    stid VARCHAR(10) NOT NULL,
    stfirstname VARCHAR(10) NOT NULL ,
    stlastname VARCHAR(10) NOT NULL,
    stdob VARCHAR(10) NOT NULL,
    stmobile VARCHAR(10) NOT NULL

)""" )
con.commit()
class Student:
    def __init__(self):
        self.stid=""
        self.stfirstname=""
        self.stlastname=""
        self.stdob=""
        self.stmobile=""

    def datafilling(self):
        while True:
            self.stid=input("Enter The Student ID : ")
            if self.stid.isnumeric() and len(self.stid)==10:
                print("Student ID Is Successfully Added To Database")
                break
            else:
                print("Enter The Valid Student ID")
                continue
        while True:
            self.stfirstname=input("Enter The First Name OF The Student : ")
            if self.stfirstname.isalpha():
                print("First Name Added To The Database")
                break
            else:
                print("Enter The Correct Name ")
                continue
        
        while True:
            self.stlastname=input("Enter The Last Name Of The Student")
            if self.stlastname.isalpha():
                print("Last Name Added To Database")
                break
            else:
                print("Enter The Correct Name ")
                continue
        
        while True:
            self.stdob=input("Enter The DOB DD-MM-YYYY : ")
            patterndob=r"((?:0[1-9])|(?:[0-2]))\/((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/(\d{4})"
            if re.search(patterndob,self.stdob):
                print("DOB Added")
                break
            else:
                print("Enter Correct DOB Make Sure Placeholder Are Correct")
                continue

        while True:
            self.stmobile=str(input("Enter Your Mobile No."))
            if len(self.stmobile)!=10:
                print("Enter The Correct Mobile Number")
                continue
            else:
                break
    def databasee(self):
        c.execute(" INSERT INTO Studentdata(stid,stfirstname,stlastname,stdob,stmobile) VALUES(?,?,?,?,?) ",(self.stmobile,self.stfirstname,self.stlastname,self.stdob,self.stmobile))
        con.commit()
        print("Database Created")
obj=Student()
obj.datafilling()
obj.databasee()
c.close()
con.close()