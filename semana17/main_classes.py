class MoneyMovement:
    def __init__(self, reason, amount, category, date):
        self.reason = reason
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            "reason": self.reason,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

class NewCategory:
    def __init__(self, category, list_val):
        self.category = category
        self.list = list_val

    def to_dict(self):
        return {
            "name": self.category,
            "category": self.list
        }