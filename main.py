# This Project Is To Track Income/Expenses & Display Clearly To Users Through Tkinter (GUI) with a good design.

# Importing necessary libraries
import tkinter as tk
from tkinter import ttk

# Global constants 
# Storing options for currency, income categories, and expense categories
CURRENCY_OPTIONS = ["£", "$", "€"]
INCOME_CATEGORIES = ["Salary", "Bonus", "Other"]
EXPENSE_CATEGORIES = ["Food", "Rent", "Utilities", "Entertainment", "Other"]

# Creating the main window
root = tk.Tk()
root.title("Budget Tracker GUI")                    
root.geometry("800x700")
root.configure(bg="#0d1b2a")
root.minsize(800, 700)


# Widget Styling
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", font=("Arial", 10, "bold"))
style.configure("TComboBox", font=("Arial", 10), padding=(2,2,2,2))

# Header
header = tk.Label(root, text="Budget Tracker GUI", font=("Arial", 24, "bold"), fg="white", bg="#0d1b2a")
header.pack(pady=(10, 0))
line_below_header = tk.Frame(root, height=2, width=700, bg="#778899")
line_below_header.pack(pady=(5, 10))

# Currency Selection Function
currency_var = tk.StringVar(value=CURRENCY_OPTIONS[0])
currency_frame = tk.Frame(root, bg="#0d1b2a")
currency_frame.pack(pady=5)

tk.Label(currency_frame, text="SELECT CURRENCY:", font=("Arial", 12, "bold"), fg="white", bg="#0d1b2a").pack(side=tk.LEFT, padx=5)

currency_menu = ttk.Combobox(currency_frame, textvariable=currency_var, values = CURRENCY_OPTIONS, width=5, state="readonly")
currency_menu.pack(side=tk.LEFT)
 

root.mainloop()