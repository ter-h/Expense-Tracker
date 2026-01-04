import argparse
from ExpenseManager import ExpenseManager
import re

def main():
    parser = argparse.ArgumentParser(
        prog="expense_tracker",
        description="CLI to track expenses"
    )

    sub = parser.add_subparsers(dest="command")

    # add
    add_p = sub.add_parser("add", help="Add a new expense")
    add_p.add_argument(
        "-d", "--description",
        type=str,
        help="description"
    )
    add_p.add_argument(
        "-a", "--amount",
        type=float,
        help="amount"
    )

    # Update
    update_p = sub.add_parser("update", help="Update expense amount or description")
    update_p.add_argument("id", type=int)
    update_p.add_argument(
        "-d", "--description",
        type=str,
        help="description"
    )
    update_p.add_argument(
        "-a", "--amount",
        type=parse_amount,
        help="amount"
    )

    # Delete
    delete_p = sub.add_parser("delete", help="Delete a task")
    delete_p.add_argument("id", type=int)

    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument(
        "-a", "--amount",
        type=str,
        help="list by amount"
    )

    summary_p = sub.add_parser("summary", help="Show summary")
    summary_p.add_argument(
        "-m", "--month",
        type=int,
        choices=range(1, 13),
        metavar="1-12",
        help="Filter by month (1-12, requires --year)"
    )
    summary_p.add_argument(
        "-y", "--year",
        type=int,
        help="year"
    )
    
    args = parser.parse_args()
    expenses = ExpenseManager()
    try:
        if args.command == "add":
            t = expenses.expense_add(args.description, args.amount)
            print(f"Expense added successfully (ID: {t.id})")

        elif args.command == "update":
            expenses.expense_update(args.id, args.description, args.amount)
            print("Expense updated.")

        elif args.command == "delete":
            expenses.expense_delete(args.id)
            print("Expense deleted.")

        elif args.command == "list":
            if args.amount:
                parse_amount(args.amount)
                
            expenses.expense_list(args.amount)
        
        elif args.command == "summary":
            expenses.expense_summary(args.amount, args.month, args.year)
        
    except ValueError as e:
        return e
    

def parse_amount(value):
    match = re.fullmatch(r"(<=|>=|<|>)\s*(\d+(\.\d+)?)", value)
    if not match:
        raise argparse.ArgumentTypeError(
            'Amount must be like "<10", "<=10", ">5", ">=5.5"'
        )

    op = match.group(1)
    amount = float(match.group(2))
    return op, amount