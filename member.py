import mysql.connector
import pandas as pd 
from tabulate import tabulate


con=mysql.connector.connect(host='localhost',user="root",password="1234",charset="utf8",database="library")
cur=con.cursor()


def member_add():
	mid=int(input("Enter id:\t"))
	mname=input("Enter name:\t")
	maddress=input("Enter address:\t")
	mmobile=input("Enter Mobile number:\t")
	qry="insert into member values({},'{}','{}','{}');".format(mid,mname,maddress,mmobile)
	cur.execute(qry)
	con.commit()
	print("one record added successfully...")


def member_edit():
	mid=int(input("Enter member id to be edited:\t"))
	qry="select * from member where mid={};".format(mid)
	cur.execute(qry)
	result=cur.fetchone()
	if result:
		mname=input("Enter updated name:\t")
		mmobile=input("Enter updated mobile:\t")
		maddress=input("Enter updated address:\t")
		qry="update member set mname='{}',mmobile='{}',maddress='{}'  where mid={};".format(mname,mmobile,maddress,mid)
		cur.execute(qry)
		con.commit()
		print("Record edit successfully...")

	else:
		print("Wrong member id:Not exists in database ")


def member_delete():
	mid=int(input("Enter member id:\t"))
	qry="select * from member where mid={};".format(mid)
	cur.execute(qry)
	result=cur.fetchone()
	if result:
		qry="delete from member where mid={};".format(mid)
		cur.execute(qry)
		con.commit()
		print("{} member id record is delete successfully...".format(mid))
	else:
		print("Wrong member id:Not exists in database")


def member_search():
	mid=int(input("Enter member id to be search:\t"))
	qry="select * from member where mid={};".format(mid)
	cur.execute(qry)
	result=cur.fetchone()
	if result:
		df=pd.read_sql(qry,con)
		print(tabulate(df,showindex=False,tablefmt="psql",headers="keys"))
	else:
		print("Wrong member id: Not exists in database")


















