# 💰 Expense Tracker Using Python & CSV

A simple command-line Expense Tracker application built with Python that helps users record, manage, and analyze their daily expenses. All expense data is stored permanently in a CSV file, making it easy to track spending over time.

## 🚀 Features

* Add new expenses with category, amount, and description
* Automatically records date and time
* Store expense data in a CSV file
* View all recorded expenses
* Calculate total expenses
* Generate category-wise expense summaries
* User-friendly menu-driven interface
* Basic error handling for invalid inputs

## 📂 Project Structure

```text
expense_tracker.py
expenses.csv
README.md
```

## 🛠 Technologies Used

* Python 3
* CSV Module
* Datetime Module

## ▶️ How to Run

1. Install Python on your system.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the application:

```bash
python expense_tracker.py
```

## 📋 Menu Options

| Option | Description      |
| ------ | ---------------- |
| 1      | Add Expense      |
| 2      | View Expenses    |
| 3      | Total Expenses   |
| 4      | Category Summary |
| 5      | Exit             |

## 📊 Expense Data Format

Expenses are stored in a CSV file with the following columns:

| Date                | Category | Amount | Description |
| ------------------- | -------- | ------ | ----------- |
| 2026-06-03 10:30:00 | Food     | 250    | Lunch       |

## 💡 Example Usage

```text
========== EXPENSE TRACKER ==========
1. Add Expense
2. View Expenses
3. Total Expenses
4. Category Summary
5. Exit

Enter your choice: 1

Enter category (Food/Travel/Shopping/etc): Food
Enter amount: 250
Enter description: Lunch

Expense added successfully ✔
```

## 📈 Sample Category Summary

```text
====== CATEGORY SUMMARY ======

Food            ₹1250.00
Travel          ₹850.00
Shopping        ₹2000.00
```

## 🎯 Learning Outcomes

This project demonstrates:

* File handling in Python
* CSV file operations
* Functions and modular programming
* Dictionary usage
* Exception handling
* Date and time management
* Data aggregation and reporting

## 🔮 Future Enhancements

* Delete expenses
* Edit existing expenses
* Monthly expense reports
* Expense charts and graphs
* Budget tracking
* Export reports to Excel/PDF

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is open-source and available under the MIT License.
