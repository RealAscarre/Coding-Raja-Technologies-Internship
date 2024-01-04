# Made By Ascarre
import json
import os
from collections import defaultdict

# Check if the file exists
if not os.path.exists('budget_data.json'):
    # Create an empty file
    with open('budget_data.json', 'w') as file:
        file.write('{}')
    print("Storage file created successfully.")
else:
    print("Storage file already exists.")

# Initialize empty data structure for expenses and income
transactions = defaultdict(list)

def save_data():
    with open('budget_data.json', 'w') as file:
        json.dump(transactions, file)

def load_data():
    global transactions
    try:
        with open('budget_data.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = defaultdict(list)

    # Ensure keys exist even if the file was created newly
    transactions.setdefault('income', [])
    transactions.setdefault('expense', [])

def add_transaction(transaction_type, category, amount):
    transactions[transaction_type].append({'category': category, 'amount': amount})
    save_data()

def get_valid_amount_input(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Please enter a non-negative amount.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_balance():
    total_income = sum(transaction['amount'] for transaction in transactions['income'])
    total_expense = sum(transaction['amount'] for transaction in transactions['expense'])
    return total_income - total_expense

def analyze_expenses():
    expense_categories = defaultdict(int)
    for expense in transactions['expense']:
        expense_categories[expense['category']] += expense['amount']
    
    print("\nExpense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ₹{amount}")

def clear_data():
    while True:
        confirmation = input("Are you sure you want to clear all data? (Yes/No) or (y/n): ").lower()
        if confirmation in ['yes', 'y']:
            global transactions
            transactions = defaultdict(list)
            save_data()
            print("\nAll data cleared successfully.")
            break
        elif confirmation in ['no', 'n']:
            print("Clear data operation canceled.")
            break
        else:
            print("Invalid input. Please enter 'Yes/No' or  'Y/N'.")
def main():
    load_data()
    
    while True:
        print("\n===== Main Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Clear Data")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter income category: ")
            amount = get_valid_amount_input("Enter amount: ")
            add_transaction('income', category, amount)
            print("\nIncome added successfully!")
        
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = get_valid_amount_input("Enter amount: ")
            add_transaction('expense', category, amount)
            print("\nExpense added successfully!")
        
        elif choice == '3':
            balance = calculate_balance()
            print(f"\nRemaining Budget: ₹{balance}")
        
        elif choice == '4':
            analyze_expenses()
        
        elif choice == '5':
            clear_data()
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
  
# Made By Ascarre
