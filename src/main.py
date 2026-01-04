import argparse

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

    add_p.add_argument()

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
        type=float,
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
        help="month"
    )
    summary_p.add_argument(
        "-y", "--year",
        type=int,
        help="year"
    )
    