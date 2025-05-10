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
header = tk.Label(
    root, 
    text="Budget Tracker GUI",
    font=("Arial", 32, "bold"),
    fg="white",
    bg="#0d1b2a"
)
header.pack(pady=(10, 0))

line_below_header = tk.Frame(root, height=2, width=700, bg="#778899")
line_below_header.pack(pady=(5, 10))

# Currency Selection Function
currency_var = tk.StringVar(value=CURRENCY_OPTIONS[0])
currency_frame = tk.Frame(root, bg="#0d1b2a")
currency_frame.pack(pady=5)

currency_label = tk.Label(
    currency_frame,
    text="SELECT CURRENCY:",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#0d1b2a"
)
currency_label.pack(side=tk.LEFT, padx=5)

currency_menu = ttk.Combobox(
    currency_frame,
    textvariable=currency_var,
    values=CURRENCY_OPTIONS,
    width=5,
    state="readonly"
)
currency_menu.pack(side=tk.LEFT, padx=5)


# Entry Section

entry_frame = tk.Frame(root, bg="#0d1b2a")
entry_frame.pack(pady=20)

#Income
income_frame = tk.Frame(entry_frame, bg="#1b263b", padx=20, pady=10,
                        highlightbackground="#778899", highlightthickness=1)
income_frame.pack(side=tk.LEFT, padx=25)

income_title = tk.Label(income_frame, text="INCOME", font=("Arial", 18, "bold"),
                        fg="white", bg="#1b263b")
income_title.pack(pady=2)

tk.Label(income_frame, text="Amount:", fg="white", bg="#1b263b").pack(anchor="w")   # Amount Label And Input
income_amount = tk.Entry(income_frame, width=27)
income_amount.pack(pady=2)

tk.Label(income_frame, text="Category:", fg="white", bg="#1b263b").pack(anchor="w") # Category Label And Dropdown Options
income_category = ttk.Combobox(
    income_frame,
    values=INCOME_CATEGORIES,
    width=25,
    state="readonly"
)
income_category.pack(pady=2)

tk.Label(income_frame, text="Description:", fg="white", bg="#1b263b").pack(anchor="w") # Description Label And Input
income_description = tk.Entry(income_frame, width=27)
income_description.pack(pady=2)

income_button = ttk.Button(income_frame, text="Add Income") # Button To Add Income
income_button.pack(pady=(10, 0))
    

root.mainloop()