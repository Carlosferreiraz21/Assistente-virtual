from database.operations import DatabaseOperations
from utils.formatters import format_currency

class FinanceService:
    def __init__(self):
        self.db = DatabaseOperations()

    def register_income(self, amount: float, description: str):
        return self.db.insert_transaction("income", amount, description)

    def register_expense(self, amount: float, description: str):
        return self.db.insert_transaction("expense", amount, description)

    def generate_report(self):
        transactions = self.db.get_transactions()
        total_income = sum(t.amount for t in transactions if t.type == "income")
        total_expenses = sum(t.amount for t in transactions if t.type == "expense")
        balance = total_income - total_expenses
        
        return {
            "total_income": format_currency(total_income),
            "total_expenses": format_currency(total_expenses),
            "balance": format_currency(balance)
        }
    
    def calculate_net_profit(self):
        transactions = self.db.get_transactions()
        total_income = sum(t.amount for t in transactions if t.type == "income")
        total_expenses = sum(t.amount for t in transactions if t.type == "expense")
        return format_currency(total_income - total_expenses)
    
    def calculate_gross_profit(self):
        transactions = self.db.get_transactions()
        total_income = sum(t.amount for t in transactions if t.type == "income")
        return format_currency(total_income)
    
    def get_current_balance(self):
        return format_currency(self.db.get_balance()) 