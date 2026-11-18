from expense import Expense

expenses = []

for i in range(3):
    name = input("Enter your name:")
    amount = float(input("enter amount:"))
    category = input("enter category:")
    date = input("enter date:")

exp = Expense(1,name,amount,category,date)
expenses.append(exp)

for exp in expenses:
    exp.display_expense()

total = 0
for exp in expenses:
    total += exp.amount

print("total expenses:",total)


