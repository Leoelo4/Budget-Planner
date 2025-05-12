# This Project Is To Track Income/Expenses & Display Clearly To Users Through Tkinter (GUI) with a good design.

# Importing necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
    text="BUDGET TRACKER",          # Application Title
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
    padx=20, 
    pady=25,
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
income_category.pack(pady=(0, 10))

# Input field for income description with a text label
tk.Label(income_frame, text="Description:", fg="white", bg="#1b263b").pack(anchor="w") # Description Label And Input
income_description = tk.Entry(income_frame, width=27)
income_description.pack(pady=2)

# Button to confirm and add income
income_button = ttk.Button(income_frame, text="Add Income") # Button To Add Income
income_button.pack(pady=(25, 5))

# Income Logic
def add_income():
    global total_income
    try:
        amount = float(income_amount.get())
        category = income_category.get().strip() or "Uncategorised"
        description = income_description.get().strip()

        if amount <= 0:
            raise ValueError("Amount must be a positive number!")
        
        total_income  += amount
        entry = f"Income: {currency_var.get()} {amount:.2f} | Category: {category} | Description: {description}"
        entries.append(entry)

        update_summary()
        update_history()
        income_amount.delete(0, tk.END)
        income_category.set("")
        income_description.delete(0, tk.END)

        messagebox.showinfo("Success", "Income Was Added Successfully!")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number") 

income_button.config(command=add_income)
    
# ===========================
#       Expense Section
# ===========================
expense_frame = tk.Frame(
    entry_frame,
    bg="#1b263b",
    padx=20,
    pady=25,
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
expense_category = ttk.Combobox(
    expense_frame,
    values=EXPENSE_CATEGORIES,
    width=25,
    state="readonly"
)
expense_category.pack(pady=2)

# Expense description input field with a text label
tk.Label(expense_frame, text="Description:", fg="white", bg="#1b263b").pack(anchor="w")
expense_description = tk.Entry(expense_frame, width=27)
expense_description.pack(pady=2)

# Button to add expense
expense_button = ttk.Button(expense_frame, text="Add Expense")
expense_button.pack(pady=(25, 5))

# Expense Logic
def add_expense():
    global total_expense
    try:
        amount = float(expense_amount.get())
        category = expense_category.get().strip() or "Uncategorised"
        description = expense_description.get().strip()
        total_expense += amount

        if amount <= 0:
            raise ValueError("Amount must be a positive number!")
        
        entry = f"Expense: {currency_var.get()} {amount:.2f} | Category: {category} | Description: {description}"

        entries.append(entry)
        update_summary()
        update_history()
        expense_amount.delete(0, tk.END)
        expense_category.set("")
        expense_description.delete(0, tk.END)

        messagebox.showinfo("Success", "Expense Was Added Successfully!")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please Enter A Valid Number")

expense_button.config(command=add_expense)

# ==========================
#   Summary Section
# ==========================

summary_frame = tk.Frame(root, bg="#1b263b") 
summary_frame.pack(pady=20)

summary_frame = tk.Frame(
    root,
    bg = "#1b263b",
    padx = 10,
    pady = 15,
    highlightbackground = "#778899",
    highlightthickness = 1,
)
summary_frame.pack(pady=(0, 15,))

summary_title  = tk.Label(
    summary_frame,
    text = "BALANCE SUMMARY",
    font = ("Arial", 18, "bold"),
    fg = "white",
    bg = "#1b263b",
)
summary_title.pack(pady=(5, 5))

summary_separator = tk.Frame(
    summary_frame,
    height = 2,
    width = 400,
    bg = "#778899",
)
summary_separator.pack(pady=(3, 5))

summary_label = tk.Label(
    summary_frame,
    text = "",
    font = ("Arial", 14, "bold"),
    fg = "white",
    bg = "#1b263b",
    width = 77
)
summary_label.pack(pady = (5, 5))

seperator = tk.Frame(root, height = 2, width = 700, bg = "#778899")
seperator.pack(pady=(10, 10))

# ==========================
#   Entry History Section
# ==========================

history_title = tk.Label(
    root,
    text="ENTRY HISTORY",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#0d1b2a"
)
history_title.pack(pady=(5, 20))

history_text = tk.Text(
    root,
    height = 15,
    width = 107,
    state = "disabled",
    bg = "#1b263b",
    fg = "white",
    font = ("Courier New", 10),
    highlightbackground="#778899",      # Frame border color
    highlightthickness=1                # Frame border thickness    
)
history_text.pack(pady=(5, 20))

# Summary section logic
total_income = 0
total_expense = 0
entries = []

def update_summary():
    balance = total_income - total_expense
    summary = (
        f"Total Income: {currency_var.get()} {total_income:.2f}   ┃   "
        f"Total Expense: {currency_var.get()} {total_expense:.2f}   ┃   "
        f"Balance: {currency_var.get()} {balance:.2f}"
    )
    summary_label.config(text=summary)

def update_history():
    history_text.config(state="normal")
    history_text.delete(1.0, tk.END)
    for entry in entries:
        history_text.insert(tk.END, entry + "\n")
    history_text.config(state="disabled")

update_summary()

root.mainloop()