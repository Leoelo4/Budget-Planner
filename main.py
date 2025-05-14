# This Project Is To Track Income/Expenses & Display Clearly To Users Through Tkinter (GUI) with a good design.

# Importing necessary libraries
import tkinter as tk                # Renaming tkinter to tk for easier use
from tkinter import ttk             # Importing ttk for tk themed widgets
from tkinter import messagebox      # Importing messagebox to popup messages to user

# Global constants 
# Storing options for currency, income categories, and expense categories
CURRENCY_OPTIONS = ["£", "$", "€"]                  # Constant for currency options
INCOME_CATEGORIES = ["Salary", "Bonus", "Other"]    # Constant for income categories
EXPENSE_CATEGORIES = ["Food", "Rent", "Utilities", "Entertainment", "Other"] # Constant for expense categories

# Global variables 
total_income = 0        # Set default total income to 0
total_expense = 0       # Set default total expenses to 0
entries = []            # Empty list to store income & expense inputs

# Creating the main window
root = tk.Tk()
root.title("Budget Tracker GUI")    # Title of the application window                
root.geometry("800x950")            # Application size
root.configure(bg="#0d1b2a")        # Application background color
root.minsize(800, 700)              # Minimum size of the application 

# Widget Styling
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", font=("Arial", 10, "bold"))                      # Button font and style
style.configure("TComboBox", font=("Arial", 10), padding=(2,2,2,2))         # Dropdown menu font and style

# Main title header
header = tk.Label(
    root,                           # Placing the main title within the root window
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

# Currency text and dropdown menu with set options from global constant
currency_label = tk.Label(
    currency_frame,                     # Placing the currency label within the currency frame
    text="SELECT CURRENCY:",            # Text label next to currency dropdown menu
    font=("Arial", 18, "bold"),         # Text font and design
    fg="white",                         # Text font colour
    bg="#0d1b2a"                        # Background colour
)
currency_label.pack(side=tk.LEFT, padx=5)

# Dropdown menu to select type of currency with set options
currency_menu = ttk.Combobox(
    currency_frame,                 # Placing the dropdown within the currency frame
    textvariable=currency_var,      # Variable to store user's selected currency
    values=CURRENCY_OPTIONS,        # Referencing the constant for set currency options
    width=5,
    state="readonly"                # Enforces the dropdown is read-only
)
currency_menu.pack(side=tk.LEFT, padx=5)    # Currency dropdown menu padding

# ==========================
#   Income/Expense Entry
# ==========================
entry_frame = tk.Frame(root, bg="#0d1b2a")      # Creating the frame for income/expense frames to sit within
entry_frame.pack(pady=20)    # Entry frame padding

# Income frame 
income_frame = tk.Frame(
    entry_frame,                        # Placing the entry frame within the entry (main) frame
    bg="#1b263b",                       # Frame background color
    padx=20,                            # Horizontal padding
    pady=25,                            # Vertical padding
    highlightbackground="#778899",      # Frame border color
    highlightthickness=1                # Frame border thickness    
)
income_frame.pack(side=tk.LEFT, padx=25)    # Forcing the frame to the left with padding

# Income title and design
income_title = tk.Label(
    income_frame,                       # Placing the income title within the income frame
    text="INCOME",                      # Text title for income section/frame
    font=("Arial", 18, "bold"),         # Font, style and size of title
    fg="white",                         # Title font colour
    bg="#1b263b"                        # Title background colour
)
income_title.pack(pady=2)               # Income title padding

# Input field for income amount with label
tk.Label(income_frame, text="Amount:", fg="white", bg="#1b263b").pack(anchor="w")   # Amount Label And Input
income_amount = tk.Entry(income_frame, width=27)
income_amount.pack(pady=2)

# Dropdown menu for income category with set options
tk.Label(income_frame, text="Category:", fg="white", bg="#1b263b").pack(anchor="w") # Category Label And Dropdown Options
income_category = ttk.Combobox(
    income_frame,                       # Placing the dropdown within the income frame
    values=INCOME_CATEGORIES,           # Referencing the constant for income categories
    width=25,                           # Width of dropdown menu
    state="readonly"                    # Forcing the dropdown into being read-only
)
income_category.pack(pady=(0, 10))      # Income dropdown menu padding

# Input field for income description with a text label
tk.Label(income_frame, text="Description:", fg="white", bg="#1b263b").pack(anchor="w") # Description Label And Input
income_description = tk.Entry(income_frame, width=27) # Description input field
income_description.pack(pady=2)

# Button to confirm and add income
income_button = ttk.Button(income_frame, text="Add Income") # Button To Add Income
income_button.pack(pady=(25, 5))    # Income button padding

# Income Logic
# This function is used to get user input for income and add it to the summary & history
def add_income():
    # Reference to global variable to store total income
    global total_income
    try:
        amount = float(income_amount.get())                                 # Amount is equal to input from the income amount field
        category = income_category.get().strip() or "Uncategorised"         # Category = input from category dropdown, if empty set Uncategorised
        description = income_description.get().strip()                      # Description is equal to input from the description field  

        if amount <= 0:                                                     # Check if the amount is a valid positive number
            raise ValueError("Amount must be a positive number!")           # If not, raise a ValueError to show invalid input
        
        # Adding the amount to the total income for future calculations in the program
        total_income  += amount
        entry = f"Input Type: Income | {currency_var.get()} {amount:.2f} | Category: {category} | Description: {description}"   # Entry history income format
        entries.append(entry)

        # Updating summary and history sections
        update_summary()
        update_history()

        # Clearing input fields once the button is pressed
        income_amount.delete(0, tk.END)
        income_category.set("")
        income_description.delete(0, tk.END)

        # Message box to show user the income was added without error
        messagebox.showinfo("Success", "Income Was Added Successfully!")

    # ValueError to check number is valid with message box to display error to user
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number") 

# Command to add income once the button is pressed
income_button.config(command=add_income)
    
# ===========================
#       Expense Section
# ===========================
# Expense frame
expense_frame = tk.Frame(
    entry_frame,                            # Placing the expense frame within the entry frame to align with income frame horizontally
    bg="#1b263b",                           # Background colour
    padx=20,                                # Horizontal padding
    pady=25,                                # Vertical padding
    highlightbackground="#778899",          # Expense frame border colour
    highlightthickness=1                    # Border thickness amount
)
expense_frame.pack(side=tk.LEFT, padx=25)   # Forcing the expense frame to the left & padding

# Expense title and design
expense_title = tk.Label(expense_frame, text="EXPENSE", font=("Arial", 18, "bold"), fg="white", bg="#1b263b") # Title design
expense_title.pack(pady=(0, 10))        # Expense title padding

# Input field for expense amount with text label & design
tk.Label(expense_frame, text="Amount:", fg="white", bg="#1b263b").pack(anchor="w")
expense_amount = tk.Entry(expense_frame, width=27)
expense_amount.pack(pady=2)

# Expense category dropdown menu with set options & design
tk.Label(expense_frame, text="Category", fg="white", bg="#1b263b").pack(anchor="w")
expense_category = ttk.Combobox(
    expense_frame,
    values=EXPENSE_CATEGORIES,          # Referencing the constant for set expense categories
    width=25,                           # Width of dropdown menu
    state="readonly"                    # Forcing the dropdown menu to be read-only
)
expense_category.pack(pady=2)           # Dropdown menu padding

# Expense description input field with a text label & Design
tk.Label(expense_frame, text="Description:", fg="white", bg="#1b263b").pack(anchor="w")
expense_description = tk.Entry(expense_frame, width=27)
expense_description.pack(pady=2)

# Button to add expense & Padding
expense_button = ttk.Button(expense_frame, text="Add Expense")
expense_button.pack(pady=(25, 5))

# Expense Logic
def add_expense():
    # Reference to global variable to store the total expense
    global total_expense
    try:
        amount = float(expense_amount.get())                            # Amount = input from expense amount field
        category = expense_category.get().strip() or "Uncategorised"    # Category = input from dropdown menu, if empty set Uncategorised
        description = expense_description.get().strip()                 # Description is the input from expense description field
        total_expense += amount

        # If the amount is 0 or less, raise a ValueError
        if amount <= 0:
            raise ValueError("Amount must be a positive number!")
        
        # Expense entry format for the history section
        entry = f"Input Type: Expense | Amount: {currency_var.get()} {amount:.2f} | Category: {category} | Description: {description}"

        # Adding the entry to the entries list
        entries.append(entry)
        update_summary()
        update_history()

        # Deleting the input fields once add expense button has been pressed
        expense_amount.delete(0, tk.END)
        expense_category.set("")
        expense_description.delete(0, tk.END)

        # Message box to show user's the expense was added without any error
        messagebox.showinfo("Success", "Expense Was Added Successfully!")

    # ValueError to check the number is valid & display error message box to user
    except ValueError:
        messagebox.showerror("Invalid Input", "Please Enter A Valid Number")

expense_button.config(command=add_expense)          # Setting the expense button to add expense through function once pressed

# ==========================
#       Summary Section
# ==========================

# Summary frame title, padding and border
summary_frame = tk.Frame(
    root,
    bg = "#1b263b",                     # Entire frame background colour
    padx = 10,                          # Summary frame horizontal padding
    pady = 15,                          # Summary frame vertical padding
    highlightbackground = "#778899",    # Frame border colour
    highlightthickness = 1              # Frame border thickness
)
summary_frame.pack(pady=(15, 15))       # Summary frame padding

# Summary frame title and design
summary_title  = tk.Label(
    summary_frame,                      # Placing the summary title within the summary frame
    text = "BALANCE SUMMARY",           # Frame title text
    font = ("Arial", 18, "bold"),       # Title font and style
    fg = "white",                       # Title font colour
    bg = "#1b263b"                      # Title background colour to blend with the frame background
)
summary_title.pack(pady=(5, 5))         # Summary title padding

# Line below the summary title for design and clarity
summary_separator = tk.Frame(
    summary_frame,                      # Placing the seperator inside of the summary frame
    height = 2, width = 400,            # Height & width of the line
    bg = "#778899",                     # Setting line colour
)
summary_separator.pack(pady=(7.5, 15))  # Summary separator padding

# Display total income
summary_label = tk.Label(
    summary_frame,                      # Placing the summary label within the summary frame
    text = "",                          # Setting the text to empty default as the function will update this
    font = ("Arial", 14, "bold"),       # Summary label font, size and style
    fg = "white", bg = "#1b263b",       # Summary label background colour
    width = 77                          # Summary label width
)
summary_label.pack(pady = (5, 5))       # Summary label padding

# Seperator line below the summary section for design & clarity
seperator = tk.Frame(root, height = 2, width = 700, bg = "#778899")
seperator.pack(pady=(10, 10))

# Function to calculate balance and update the summary
def update_summary():
    # Equation to calculate balance
    balance = total_income - total_expense
    # Summary text format to display total income, expense and balance
    # Using currency_var.get() to get the user's selected currency choice and display this to them
    summary = (
        f"Total Income: {currency_var.get()} {total_income:.2f}   ┃   "
        f"Total Expense: {currency_var.get()} {total_expense:.2f}   ┃   "
        f"Balance: {currency_var.get()} {balance:.2f}"
    )
    summary_label.config(text=summary)

# ==========================
#   Entry History Section
# ==========================

# Creating the history frame
history_title = tk.Label(
    root,
    text="ENTRY HISTORY",                       # Title for history section for clarity
    font=("Arial", 18, "bold"), fg="white",     # Title font colour, size and style
    bg="#0d1b2a"                                # Title background colour
)
history_title.pack(pady=(5, 20))                # History title padding

history_text = tk.Text(
    root,
    height = 15, width = 107,                               # Text box height and width
    state = "disabled",                                     # Setting text box to read-only
    bg = "#1b263b",                                         # Text box background colour
    fg = "white", font = ("Courier New", 10),               # Text font, size and style
    highlightbackground="#778899", highlightthickness=1     # Frame border colour & thickness    
)
history_text.pack(pady=(5, 20))

# Refreshes entry history to show recent entries
def update_history():
    history_text.config(state="normal")
    history_text.delete(1.0, tk.END)
    for entry in entries:
        history_text.insert(tk.END, entry + "\n")
    history_text.config(state="disabled")

update_summary()

# ==========================
#       Footer Section
# ==========================

# Creating the footer frame & background colour
footer_frame = tk.Frame(root, bg = "#1b263b")   # Footer frame crated with background colour
footer_frame.pack(side=tk.BOTTOM, fill="x")     # Forces the footer at the bottom of the window & fills entire width

# Line above the footer to divide sections
footer_separator = tk.Frame(
    footer_frame,               # Placing the separator within the footer frame
    height = 2,                 # Separator line height
    bg = "#778899"              # Separator line colour
)
footer_separator.pack(side = tk.TOP, fill = "x")    # Forces the separator at the top of the footer frame & fills the entire x axis (width)

# Footer text and design
footer = tk.Label(
    footer_frame,                                       # Placing the footer text within the footer frame
    text = " © GUI Created By Leos  |   2025",          # Footer text
    font = ("Arial", 10),                               # Footer font and font size
    fg = "white", bg = "#1b263b"                        # Footer text and background colour
)
footer.pack(side=tk.BOTTOM, pady = (5, 5))              # Footer padding & forcing to be at the bottom

# Running the main loop
if __name__ =="__main__":
    root.mainloop()