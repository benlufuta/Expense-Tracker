#Author: Ben Lufuta
#Project: Expense Tracker, Version 1
#Date: 2025-11-01
#Features (first version):
  #Add an expense → enter category, amount, date (as string for now).
  #View all expenses → print each expense.
  #Total by category → sum amounts for a given category.
  #Exit option → quit program.


#Global Variable:
expenses = []

print("\n--- Expense Tracker ---\n")

#Functions:
def start():
    
  while True:

    print("1. Add expense")
    print("2. View expenses")
    print("3. Total by category")
    print("4. Exit\n")

    choice = input("Enter a choice: ").strip()

    if choice == "1":
      add_expense()

    elif choice == "2":
      view_expenses()

    elif choice == "3":
      total_by_category()

    elif choice == "4":
      print("\n--- Goodbye ---\n")
      break

    else:
      print("Invalid Option!")


def add_expense():

  expense_category = input("Enter category: ").strip()
  amount = float(input("Enter amount: ").strip())
  date = input("Enter date (YYYY-MM-DD): ")

  current_expense = {"category": expense_category, "amount": amount, "date": date}

  expenses.append(current_expense)
  print("Expense added!\n")

def view_expenses():

  if not expenses:
    print("No expenses to view!")

  else:
    for index, expense in enumerate(expenses, 1):
      print(f"{index}. {expense['category']} - {expense['amount']} on {expense['date']}")

  print()

def total_by_category():

  category = input("Enter category: ").strip()

  category_total = 0

  for expense in expenses:

    if expense["category"].lower() == category.lower():

      category_total += expense["amount"]

  print(f"Total spent on {category.title()}: ${category_total}")

if __name__ == "__main__":
  start()