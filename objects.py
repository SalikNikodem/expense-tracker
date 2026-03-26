from datetime import datetime
from pathlib import Path
import csv
EXPENSES = Path(__file__).resolve().parent / 'expenses.csv'

class Expense:
    ID = 1
    def __init__(self, id, description, amount):
        self.description = description
        self.amount = str(amount) + ' PLN'
        self.id = id
        self.date = datetime.now().strftime("%Y-%m-%d")


    def __str__(self):
        return f"{self.id}\t{self.date}\n{self.description}\{self.amount}"

    def to_list(self):
        return [self.id, self.date, self.description, self.amount]

def load_expenses():
    if not EXPENSES.exists():
        with open(EXPENSES, 'w', newline='', encoding='utf-8') as ff:
            editor = csv.writer(ff)
            editor.writerow(['ID', 'Date', 'Description', 'Amount'])
            return []
    else:
        with open(EXPENSES, 'r', encoding='utf-8') as ff:
            reader = csv.reader(ff)
            next(reader)
            return list(reader)



def add_expense(descritpion, amount):
    expenses = load_expenses()

    new_id = max([int(expense[0]) for expense in expenses if expense], default=0) + 1

    expense = Expense(new_id, descritpion, amount)

    with open(EXPENSES, 'a',  newline='', encoding='utf-8') as ff:
        editor = csv.writer(ff)
        editor.writerow(expense.to_list())