# This Project Is To Track Income/Expenses & Display Clearly To Users Through Tkinter (GUI) with a good design.

# Importing necessary libraries
import tkinter as tk
from tkinter import ttk

# Global constants 
# Storing options for currency, income categories, and expense categories
CURRENCY_OPTIONS = ["£", "$", "€"]                  # Constant for currency options
INCOME_CATEGORIES = ["Salary", "Bonus", "Other"]    # Constant for income categories
EXPENSE_CATEGORIES = ["Food", "Rent", "Utilities", "Entertainment", "Other"] # Constant for expense categories

# Creating the main window
root = tk.Tk()
root.title("Budget Tracker GUI")    # Title of the application window                
root.geometry("800x700")            # Application size
root.configure(bg="#0d1b2a")        # Application background color
root.minsize(800, 700)              # Minimum size of the application 


# Widget Styling
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", font=("Arial", 10, "bold"))                      # Button font and style
style.configure("TComboBox", font=("Arial", 10), padding=(2,2,2,2))         # Dropdown menu font and style

# Main title header
header = tk.Label(
    root, 
    text="Budget Tracker GUI",      # Application Title
    font=("Arial", 32, "bold"),     # Title font/style and size
    fg="white",                     # Title font color   
    bg="#0d1b2a"                    # Title background color
)
header.pack(pady=(10, 0))           # Padding surrounding the title

# Creating a line below the header for aesthetics
line_below_header = tk.Frame(root, height=2, width=700, bg="#778899")
line_below_header.pack(pady=(5, 10))

# ==========================
#   Currency Selection 
# ==========================
currency_var = tk.StringVar(value=CURRENCY_OPTIONS[0])      # Creating default currency to £
currency_frame = tk.Frame(root, bg="#0d1b2a")               # Currency selection frame       
currency_frame.pack(pady=5)                                 # Padding surrounding the frame

# Currency text and dropdown menu with set options
currency_label = tk.Label(
    currency_frame,
    text="SELECT CURRENCY:",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#0d1b2a"
)
currency_label.pack(side=tk.LEFT, padx=5)

# Dropdown menu to select type of currency
currency_menu = ttk.Combobox(
    currency_frame,
    textvariable=currency_var,
    values=CURRENCY_OPTIONS,
    width=5,
    state="readonly"
)
currency_menu.pack(side=tk.LEFT, padx=5)


# ==========================
#   Income/Expense Entry
# ==========================
entry_frame = tk.Frame(root, bg="#0d1b2a") 
entry_frame.pack(pady=20)

#Income frame 
income_frame = tk.Frame(
    entry_frame, 
    bg="#1b263b",                       # Frame background color
    padx=20, pady=10,
    highlightbackground="#778899",      # Frame border color
    highlightthickness=1                # Frame border thickness    
)
income_frame.pack(side=tk.LEFT, padx=25) # Forcing the frame to the left with padding

# Income title
income_title = tk.Label(
    income_frame, 
    text="INCOME", 
    font=("Arial", 18, "bold"),
    fg="white", 
    bg="#1b263b"
)
income_title.pack(pady=2)

# Input field for income amount with label
tk.Label(income_frame, text="Amount:", fg="white", bg="#1b263b").pack(anchor="w")   # Amount Label And Input
income_amount = tk.Entry(income_frame, width=27)
income_amount.pack(pady=2)

# Dropdown menu for income category with set options
tk.Label(income_frame, text="Category:", fg="white", bg="#1b263b").pack(anchor="w") # Category Label And Dropdown Options
income_category = ttk.Combobox(
    income_frame,
    values=INCOME_CATEGORIES,   # Referencing the constant for income categories
    width=25,
    state="readonly"
)
income_category.pack(pady=2)

# Input field for income description with a text label
tk.Label(income_frame, text="Description:", fg="white", bg="#1b263b").pack(anchor="w") # Description Label And Input
income_description = tk.Entry(income_frame, width=27)
income_description.pack(pady=2)

# Button to confirm and add income
income_button = ttk.Button(income_frame, text="Add Income") # Button To Add Income
income_button.pack(pady=(15, 10))
    
# ===========================
#       Expense Section
# ===========================
expense_frame = tk.Frame(
    entry_frame,
    bg="#1b263b",
    padx=20,
    pady=15,
    highlightbackground="#778899",
    highlightthickness=1
)
expense_frame.pack(side=tk.LEFT, padx=25)

# Expense title and design
expense_title = tk.Label(expense_frame, text="EXPENSE", font=("Arial", 18, "bold"), fg="white", bg="#1b263b") # Expense box and title
expense_title.pack(pady=(0, 10))

# Input field for expense amount with text label
tk.Label(expense_frame, text="Amount:", fg="white", bg="#1b263b").pack(anchor="w")
expense_amount = tk.Entry(expense_frame, width=27)
expense_amount.pack(pady=2)

# Expense category dropdown meny with set options
tk.Label(expense_frame, text="Category", fg="white", bg="#1b263b").pack(anchor="w")
category_expense = ttk.Combobox(
    expense_frame,
    values=EXPENSE_CATEGORIES,
    width=25,
    state="readonly"
)
category_expense.pack(pady=2)

# Expense description input field with a text label
tk.Label(expense_frame, text="Description:", fg="white", bg="#1b263b").pack(anchor="w")
expense_description = tk.Entry(expense_frame, width=27)
expense_description.pack(pady=2)

# Button to add expense
income_button = ttk.Button(expense_frame, text="Add Expense")
income_button.pack(pady=(15, 10))



root.mainloop()