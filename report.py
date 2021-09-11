import mysql.connector
import pandas as pd 
from tabulate import tabulate
import matplotlib.pyplot as plt


con=mysql.connector.connect(host="localhost",user="root",password="1234",charset="utf8",database="library")
cur=con.cursor()


def book_all():
	df=pd.read_sql("select * from book",con)
	print(tabulate(df,showindex=False,tablefmt="psql",headers="keys"))


def member_all():
	df=pd.read_sql("select * from member ",con)
	print(tabulate(df,showindex=False,tablefmt="psql",headers="keys"))


def all_issue():
	df=pd.read_sql("select * from issue",con)
	print(tabulate(df,showindex=False,tablefmt="psql",headers="keys"))


def all_returns():
	df=pd.read_sql("select * from returns",con)
	print(tabulate(df,showindex=False,tablefmt="psql",headers="keys"))


def book_chart():
	qry="select bid,count(icopies) as TotalCopies from issue group by bid;"
	df=pd.read_sql(qry,con)
	plt.bar(df.bid,df.TotalCopies)
	plt.xlabel("Book Ids")
	plt.ylabel("Copies Issued")
	plt.title("Best Reading Book")
	plt.xticks(df.bid)
	plt.show()





