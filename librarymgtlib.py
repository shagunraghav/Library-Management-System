import book
import member
import transaction
import report


while True:
  ch=input("Main-Menu:\n1.Book\t2.Member\t3.Transaction\t4.Report\t5.Exit\nEnter your choice:\t")
  if ch=="1":
    while True:
      ch=input("Book-Menu:\n1.New\t2.Edit\t3.Delete\t4.Search\t5.Return main menu\nEnter your choice:\t")
      if ch=="1":
        book.book_add()
      elif ch=="2":
        book.book_edit()
      elif ch=="3":
        book.book_delete()
      elif ch=="4":
        book.book_search()
      elif ch=="5":
        break
  elif ch=="2":
    while True:
      ch=input("Member-Menu:\n1.New\t2.Edit\t3.Delete\t4.Search\t5.Return main menu\nEnter your choice:\t")
      if ch=="1":
        member.member_add()
      elif ch=="2":
        member.member_edit()
      elif ch=="3":
        member.member_delete()
      elif ch=="4":
        member.member_search()
      elif ch=="5":
        break
  elif ch=="3":
    while True:
      ch=input("Transaction-Menu:\n1.Issue Books\t2.Return Book\t3.Return main menu\nEnter your choice:\t")
      if ch=="1":
        transaction.book_issue()
      elif ch=="2":
        transaction.book_returns()
      elif ch=="3":
        break
  elif ch=="4":
    while True:
      ch=input("Report-Menu:\n1.All Books\t2.All Members\t3.All issue\t4.All returns\t5.Best Book\t6.Return main menu\nEnter your choice:\t")
      if ch=="1":
        report.book_all()
      elif ch=="2":
        report.member_all()
      elif ch=="3":
        report.all_issue()
      elif ch=="4":
        report.all_returns()
      elif ch=="5":
        report.book_chart()
      elif ch=="6":
        break
  else:
    break
