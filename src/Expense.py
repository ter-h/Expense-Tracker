from datetime import datetime
from incorrect_field_value import IncorrectFieldValue

class Expense:
    def __init__(self, id, description, amount, date=None):
        self.id = id
        self.description = description
        self.amount = amount
        self.date = date or datetime.now()

    def expense_update(self, new_desc=None, new_amnt=None):
        if new_desc is None and new_amnt is None:
            raise IncorrectFieldValue("Must enter either description or amount field")
        self.description = new_desc
        self.amnt = new_amnt
        

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "date": self.date.isoformat()
        }
    
    @staticmethod
    def from_dict(data):
        return Expense(
            id=data["id"],
            description=data["description"],
            amount=data["amount"],
            date=datetime.fromisoformat(data["date"])
        )