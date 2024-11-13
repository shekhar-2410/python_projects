# Track all expenses and incomes
import json
expenses = []

#load exit expeneses
def load_expenses():
    try:
        with open("expenses.json","r")as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#save expenses
def save_expenses():
    with open("expenses.json","w")as file:
        json.dump(expenses,file)

#add expenses
def add_expenses():
    global expenses
    expenses = load_expenses()  # Load current expenses at the start
    amount = int(input("Enter the amount: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    expenses.append({"amount": amount, "category": category, "date": date})
    print("Expense added successfully!")
    save_expenses() 
    
print(add_expenses())
# show_expenses()
def show_expenses():
    # load_expenses()
    if expenses:
        print("\nYour expenses:")
        for expense in expenses:
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])
            print("_______")
    else:
        print("\nNo expenses to show.")

# calculate_total_expenses()
def calculate_total_expenses():
    show_expenses()
    total = 0
    for expense in expenses:
        total += expense["amount"]
        print("Total amount you spent is:",total)

calculate_total_expenses()
