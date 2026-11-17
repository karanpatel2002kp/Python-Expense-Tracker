from expense import Expense

name = input("Enter your name:")
amount = float(input("enter amount:"))
category = input("enter category:")
date = input("enter date:")

exp1 = Expense(1,name,amount,category,date)
exp1.display_expense()
