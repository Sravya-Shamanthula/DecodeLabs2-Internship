import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file with headers if not exists
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass


# Add Expense
def add_expense():
    try:
        category = input("Enter category (Food/Travel/Shopping/etc): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])

        print("\nExpense added successfully ✔")

    except ValueError:
        print("Invalid amount entered!")


# View Expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n========== ALL EXPENSES ==========")

            for row in reader:
                print("{:<20} {:<15} {:<10} {}".format(
                    row[0], row[1], row[2], row[3]
                ))

    except FileNotFoundError:
        print("No expenses found!")


# Calculate Total Expenses
def total_expenses():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                total += float(row[2])

        print(f"\nTotal Expenses = ₹{total:.2f}")

    except FileNotFoundError:
        print("No data available!")


# Category-wise Summary
def category_summary():
    summary = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                category = row[1]
                amount = float(row[2])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        print("\n====== CATEGORY SUMMARY ======")

        for category, amount in summary.items():
            print(f"{category:<15} ₹{amount:.2f}")

    except FileNotFoundError:
        print("No expense data found!")


# Main Program
def main():
    initialize_file()

    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run Program
main()