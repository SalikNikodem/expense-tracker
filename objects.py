from datetime import datetime
from pathlib import Path
import csv

from urllib3.filepost import writer

EXPENSES = Path(__file__).resolve().parent / 'expenses.csv'

class Expense:
    ID = 1
    def __init__(self, id, description, amount):
        self.description = description
        self.amount = amount
        self.id = id
        self.date = datetime.now().strftime("%Y-%m-%d")


    def __str__(self):
        return f"{self.id}\t{self.date}\t{self.description}\t{self.amount}"

    def to_list(self):
        return [self.id, self.date, self.description, self.amount]

def load_expenses():
    if not EXPENSES.exists() or EXPENSES.stat().st_size == 0:
        with open(EXPENSES, 'w', newline='', encoding='utf-8') as ff:
            editor = csv.writer(ff)
            editor.writerow(['ID', 'Date', 'Description', 'Amount'])
            return []
    else:
        with open(EXPENSES, 'r', encoding='utf-8') as ff:
            reader = csv.reader(ff)
            next(reader)
            return list(reader)


def save_expenses(expenses):
    with open(EXPENSES, 'w', newline='', encoding='utf-8') as ff:
        writer = csv.writer(ff)
        writer.writerow(['ID', 'Date', 'Description', 'Amount'])
        writer.writerows(expenses)


def add_expense(description, amount):
    expenses = load_expenses()

    new_id = max([int(expense[0]) for expense in expenses if expense], default=0) + 1

    expense = Expense(new_id, description, amount)

    with open(EXPENSES, 'a',  newline='', encoding='utf-8') as ff:
        editor = csv.writer(ff)
        editor.writerow(expense.to_list())
        print(f"Expense id: {new_id} added")

def delete_expense(id):
    expenses = load_expenses()

    u_expenses = [expense for expense in expenses if expense[0] != str(id)]

    if len(expenses) == len(u_expenses):
        print(f"Error: Id {id} not found")
        return

    save_expenses(u_expenses)
    print(f"Expense id: {id} deleted")

def update_expense(id, description=None, amount=None):
    expenses = load_expenses()
    if description or amount:
        for expense in expenses:
            if expense[0] == str(id):
                if description: expense[2] = description
                if amount: expense[3] = amount
                save_expenses(expenses)
                print(f"Expense id: {id} updated")
                return
        print(f"Error: Id {id} not found")
        return
    print("Error: No description or amount provided")

# add_expense("jedzenie", 20)
# add_expense("picie", 30)
# add_expense("autobus", 10)
# add_expense("zakupy", 50)