import mysql.connector
import pandas as pd
from tabulate import tabulate


con=mysql.connector.connect(host='localhost',user='root',password='1234',charset='utf8',database='library')
cur=con.cursor()

def book_add():
	bid=int(input('Enter id:\t'))
	bname=input("Enter Book name:\t")
	bauthor=input("Enter author name:\t")
	price=float(input("Enter price:\t"))
	bcopies=int(input("Enter total number of available copies:\t"))
	remcopies=bcopies
	qry="insert into book values({},'{}','{}',{},{},{});".format(bid,bname,bauthor,price,bcopies,remcopies)
	cur.execute(qry)
	con.commit()
	print("One record added successfully....")


def book_edit():
	bid=int(input("Enter book id to be edited:\t"))
	qry="select * from book where bid={};".format(bid)
	cur.execute(qry)
	result=cur.fetchone()
	if result:
		newPrice=float(input("Enter new price for book:\t"))
		qry="update book set price={} where bid={};".format(newPrice,bid)
		cur.execute(qry)
		con.commit()
		print("Record edit successfully...")

	else:
		print("Wrong book id: Not exists in database ")


def book_delete():
	bid=int(input("Enter book id:\t"))
	qry="select * from book where bid={};".format(bid)
	cur.execute(qry)
	result=cur.fetchone()
	if result:
		qry="delete from book where bid={};".format(bid)
		cur.execute(qry)
		con.commit()
		print("{} book id is deleted successfully...".format(bid))
	else:
		print("Wrong book id: Not exists in database")


def book_search():
	bid=int(input("Enter book id to be search:\t"))
	qry="select * from book where bid={};".format(bid)
	cur.execute(qry)
	result=cur.fetchone()
	if result:
		df=pd.read_sql(qry,con)
		print(tabulate(df,showindex=False,tablefmt='psql',headers="keys"))
	else:
		print("Wrong book id:Not exists in database")












































