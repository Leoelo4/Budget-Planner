# Due to tkinter GUIs being difficult to test, this file mimics the logic of the main.py file and tests the functions,
# Testing adding income & expenses as well as calculations
# This is kept seperate to keep 'main.py' clean and fully functional for users without the test files

# Importing library for 'unittest'
import unittest

# Budget logic which mirrors 'main.py'
class BudgetTracker:
    def __init__(self):
        # Default totals and entry storage (Mirroring global variables in main.py)
        self.total_income = 0
        self.total_expense = 0
        self.entries = []

    # Mirrors add_income in main.py  to add income entry and update total income & stores entry
    def add_income(self, amount, category, description, currency):
        # If amount is 0 or less, raise the value error message
        if amount <= 0:
            raise ValueError("Amount must be larger than 0!")
        self.total_income += amount
        # Represents the income entry in the same format as main.py
        entry = {
            "Type": "Income",
            "Amount": amount,
            "Category": category,
            "Description": description,
            "Currency": currency
        }
        self.entries.append(entry)

    # Mirrors add_expense in main.py to add expense entry, update total expense & store the entry
    def add_expense(self, amount, category, description, currency):
        # If amount is 0 or less, raise a ValueError to users
        if amount <= 0:
            raise ValueError("Amount must be larger than 0!")
        self.total_expense += amount
        # Represents the expense entry in the same format as main.py
        entry = {
            "Type": "Expense",
            "Amount": amount,
            "Category": category,
            "Description": description,
            "Currency": currency
        }
        self.entries.append(entry)

    # Returns the total amount of all income entries (Used in summary section of main.py)
    def get_total_income(self):
        return sum(entry["Amount"] for entry in self.entries if entry["Type"] == "Income")

    # Returns the total amount of all expense entries (Used in summary section of main.py)
    def get_total_expenses(self):
        return sum(entry["Amount"] for entry in self.entries if entry["Type"] == "Expense")

    # Returns the total balance through calculation 
    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

    # Returns all entries for the history section in main.py
    def get_entries(self):
        return self.entries

# This class tests the logic in the BudgetTracker class
class TestBudgetTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = BudgetTracker()

    # Tests adding a valid income entry 
    def test_add_income(self):
        self.tracker.add_income(100, "Salary", "Test income", "£")
        self.assertEqual(self.tracker.total_income, 100)
        self.assertEqual(self.tracker.entries[0]["Type"], "Income")
        self.assertEqual(self.tracker.entries[0]["Amount"], 100)

    # Tests 0 and negative numbers to check if an error is raised
    def test_add_income_invalid(self):
        with self.assertRaises(ValueError):
            self.tracker.add_income(0, "Salary", "Zero income", "£")
        with self.assertRaises(ValueError):
            self.tracker.add_income(-50, "Salary", "Negative income", "£")

    # Tests adding a valid expense entry
    def test_add_expense(self):
        self.tracker.add_expense(50, "Food", "Test expense", "£")
        self.assertEqual(self.tracker.total_expense, 50)
        self.assertEqual(self.tracker.entries[0]["Type"], "Expense")
        self.assertEqual(self.tracker.entries[0]["Amount"], 50)

    # Tests entries including 0 or negative numbers to ensure an error is raised
    def test_add_expense_invalid(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense(0, "Food", "Zero expense", "£")
        with self.assertRaises(ValueError):
            self.tracker.add_expense(-10, "Food", "Negative expense", "£")

    # Tests the total income is all of the income entries added
    def test_get_total_income(self):
        self.tracker.add_income(100, "Salary", "Income1", "£")
        self.tracker.add_income(200, "Bonus", "Income2", "£")
        self.assertEqual(self.tracker.get_total_income(), 300)

    # Tests the total expenses is all of the expense entries added
    def test_get_total_expenses(self):
        self.tracker.add_expense(40, "Food", "Expense1", "£")
        self.tracker.add_expense(60, "Rent", "Expense2", "£")
        self.assertEqual(self.tracker.get_total_expenses(), 100)

    # Tests the balance is calculated through income - expense (Equation stored as get_balance function earlier)
    def test_get_balance(self):
        self.tracker.add_income(200, "Salary", "Income", "£")
        self.tracker.add_expense(50, "Food", "Expense", "£")
        self.assertEqual(self.tracker.get_balance(), 150)

    # Tests entries are stored in order correctly
    def test_entries_storage(self):
        self.tracker.add_income(100, "Salary", "Income", "£")
        self.tracker.add_expense(40, "Food", "Expense", "£")
        entries = self.tracker.get_entries()
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["Type"], "Income")
        self.assertEqual(entries[1]["Type"], "Expense")

# Running the program
if __name__ == "__main__":
    unittest.main()
