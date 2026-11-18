class Expense:
    def __init__(self,expense_id,name,amount,category,date):
        self.expense_id = expense_id
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def display_expense(self):
        print(self.expense_id)
        print(self.name)
        print(self.amount)
        print(self.category)
        print(self.date)


exp1 = Expense(1,"Grocery",500,"Food","17-11-2026")
exp1.display_expense()
