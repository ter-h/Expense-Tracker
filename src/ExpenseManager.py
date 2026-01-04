import json
from pathlib import Path
from Expense import Expense
import operator

class ExpenseManager:
    def __init__(self):
        self.app_dir = Path.home() / ".expense-cli"
        self.app_dir.mkdir(exist_ok=True)  # create folder if missing
        self.data_file = self.app_dir / "expenses.json"

        self.expenses = []
        self._id_count = 0
        self.load_from_file()

    def expense_add(self, desc, amnt):
        new_expense = Expense(self._id_count, desc, amnt)
        self.expenses.append(new_expense)
        self._id_count += 1
        self.save_to_file()
        return new_expense

    def expense_update(self, id, desc=None, amnt=None):
        expense = self._find_expense(id)
        expense.expense_update(desc)
        self.save_to_file()

    def expense_delete(self, id):
        expense = self._find_expense(id)
        self.expenses.remove(expense)
        self.save_to_file()

    def expense_list(self, amount_filter=None):
        if amount_filter is None:
            return self.expenses

        op, value = amount_filter

        ops = {
            "<": operator.lt,
            "<=": operator.le,
            ">": operator.gt,
            ">=": operator.ge,
        }

        cmp = ops[op]
        return [e for e in self.expenses if cmp(e.amount, value)]
    
    def summary(self, year=None, month=None):
        """
        Returns total expense amount.
        - year: int or None
        - month: int (1–12) or None
        """
        expenses = self.expenses

        if year is not None:
            expenses = [e for e in expenses if e.date.year == year]

        if month is not None:
            expenses = [e for e in expenses if e.date.month == month]

        return sum(e.amount for e in expenses)

    def save_to_file(self):
        with self.data_file.open('w') as f:
            json.dump([t.to_dict() for t in self.expenses], f, indent=2)

    def load_from_file(self):
        if not self.data_file.exists() or self.data_file.stat().st_size == 0:
            # File missing or empty, start fresh
            self.expenses = []
            self._id_count = 0
            return

        try:
            with self.data_file.open('r') as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(d) for d in data]
                if self.expenses:
                    self._id_count = max(t.id for t in self.expenses) + 1
        except json.JSONDecodeError:
            print(f"Warning: {self.data_file} is corrupted. Starting fresh.")
            self.expenses = []
            self._id_count = 0