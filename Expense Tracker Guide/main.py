def display_welcome_message():
    print("Welcome to the Expense Tracker!")

def get_expense():
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount <= 0:
                raise ValueError("Amount should be a positive number.")
            break
        except ValueError as e:
            print(e)
    
    categories = ["Food", "Transport", "Entertainment", "Other"]
    while True:
        category = input(f"Enter the category ({', '.join(categories)}): ").capitalize()
        if category not in categories:
            print("Please select a valid category.")
        else:
            break

    description = input("Enter a description of the expense: ")
    
    return {"amount": amount, "category": category, "description": description}

def add_expense(expenses):
    expense = get_expense()
    expenses.append(expense)
    print("Expense added successfully!")

def display_summary(expenses):
    total_amount = sum(exp['amount'] for exp in expenses)
    category_totals = {}
    for exp in expenses:
        category = exp['category']
        if category in category_totals:
            category_totals[category] += exp['amount']
        else:
            category_totals[category] = exp['amount']

    print("\nExpense Summary:")
    print(f"Total Amount Spent: ${total_amount:.2f}")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")
    print("\nAll Expenses:")
    for exp in expenses:
        print(f"{exp['amount']}: {exp['category']} - {exp['description']}")

def main():
    display_welcome_message()
    expenses = []
    
    while True:
        print("\nOptions:")
        print("1. Log a new expense")
        print("2. View expense summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid option. Please select again.")

if __name__ == "__main__":
    main()