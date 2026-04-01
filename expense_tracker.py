import argparse
from objects import add_expense, delete_expense, view_expenses, update_expense


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command",help="Available commands")

    add_parser = subparsers.add_parser("add", help="Add new expense")
    add_parser.add_argument('--description', '-d', required=True, help="Description")
    add_parser.add_argument('--amount', '-a', required=True, type=float, help="Amount")
    add_parser.add_argument('--category', '-c', required=True, help="Category")

    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument('--id', required=True, type=int, help='Expense ID')

    view_parser = subparsers.add_parser("view", help="View expenses, can filter with --month")
    view_parser.add_argument('--month', '-m', required=False, type=int, help="Month")
    view_parser.add_argument('--category', '-c', required=False, help="Category")

    update_parser = subparsers.add_parser("update", help="Update expense, provide --date, --description or --amount")
    update_parser.add_argument('--id', required=True, type=int, help='Expense ID')
    update_parser.add_argument('--description', '-d', required=False, help="Description")
    update_parser.add_argument('--amount', '-a', required=False, type=float, help="Amount")
    update_parser.add_argument('--date', '-t', required=False, help="Date")
    update_parser.add_argument('--category', '-c', required=False, help="Category")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, args.category)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "view":
        view_expenses(month=args.month, category=args.category)
    elif args.command == "update":
        update_expense(args.id,args.description,args.amount,args.date,args.category)
    elif args.command is None:
        parser.print_help()

if __name__ == "__main__":
    main()