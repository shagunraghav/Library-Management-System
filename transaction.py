import mysql.connector
import pandas as pd 
from tabulate import tabulate

con=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
cur=con.cursor()


def book_issue():
	qry1="select max(iid) from issue;"
	cur.execute(qry1)
	result=cur.fetchone()[0]
	if result:
		iid=result+1
	else:
		iid=9001
	mid=int(input("Enter member id:\t"))
	qry2="select * from member where mid={};".format(mid)
	cur.execute(qry2)
	result=cur.fetchone()
	if result:
		bid=int(input("Enter book id:\t"))
		qry3="select bid,remcopies from book where bid={};".format(bid)
		cur.execute(qry3)
		result=cur.fetchone()
		if result:
			if result[1]>0:
				qry4="select current_date();"
				cur.execute(qry4)
				idate=cur.fetchone()[0]
				icopies=int(input("Enter no. of issue copies:\t"))
				remcopies=result[1]-icopies
				qry5="insert into issue values({},'{}',{},{},{});".format(iid,idate,mid,bid,icopies)
				cur.execute(qry5)
				qry6="update book set remcopies={} where bid={};".format(remcopies,bid)
				cur.execute(qry6)
				con.commit()
				print("Book issued successfully..")
			else:
				print("Book is not available")
		else:
			print("Wrong book id:Not exists in database")
	else:
		print("Wrong member id:Not exists in database")




def book_returns():
	qry1="select max(rid) from returns;"
	cur.execute(qry1)
	result=cur.fetchone()[0]
	if result:
		rid=result+1
	else:
		rid=18001
	mid=int(input("Enter member id:\t"))
	bid=int(input("Enter book id:\t"))
	qry2="select * from issue where mid={} and bid={};".format(mid,bid)
	cur.execute(qry2)
	result=cur.fetchone()
	if result:
		qry3="select current_date();"
		cur.execute(qry3)
		rdate=cur.fetchone()[0]
		rcopies=int(input("Enter no. of return copies:\t"))
		qry4="select remcopies from book where bid={};".format(bid)
		cur.execute(qry4)
		result=cur.fetchone()[0]
		remcopies=result+rcopies
		qry5="insert into returns values({},'{}',{},{},{});".format(rid,rdate,mid,bid,rcopies)
		cur.execute(qry5)
		qry6="update book set remcopies={} where bid={}; ".format(remcopies,bid)
		cur.execute(qry6)
		con.commit()
		print("Book returns successfully")

	else:
		print("Wrong member or book id: details mismatch")















