# expense_core.py
# -------------------------------------------
# Expense Tracker Application
# Author: Ben Lufuta
# Date Created: November 14th, 2025
# -------------------------------------------


def add_expense(expenses):

    print("\n>> Adding expense...\n")

    expense_category = input("Enter category: ").strip()
    amount = float(input("Enter amount: ").strip())
    date = input("Enter date (YYYY-MM-DD): ").strip()

    current_expense = {"category": expense_category, "amount": amount, "date": date}

    expenses.append(current_expense)

    print("Expense added!\n")


def view_expenses(expenses):
    print("\n>> Viewing expenses...\n")


def total_by_category(expenses):
    print("\n>> Calculating totals...\n")

def delete_expense(expenses):
    print("\n>> Deleting Expense...\n")
