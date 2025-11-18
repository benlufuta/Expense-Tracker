# expense_core.py
# -------------------------------------------
# Expense Tracker Application
# Author: Ben Lufuta
# Date Created: November 14th, 2025
# Last Modified: November 18th, 2025
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

    if not expenses:
        print("\nNo expenses to view!\n")

    else:
        #Print Header 
        print(f'{'Index':<4}{'Category':^18} {'Amount':<18} {'Date':^18}')
        print('-' * 60)
        #Print all expenses with index
        for index, expense in enumerate(expenses, 1):
            print(f"{index:<4} {expense['category']:^18} ${expense['amount']:<18} {expense['date']:^18}")

    print()

def total_by_category(expenses):
    print("\n>> Calculating totals...\n")

    # Get category from user
    category = input("Enter category: ").strip()

    category_total = 0

    # Loop until dictionary with match category is found.
    for expense in expenses:

        if expense["category"].lower() == category.lower():
            #If found, add all amount spent on that category
            category_total += expense["amount"]

    # Print total for entered category
    print(f"Total spent on {category.title()}: ${category_total}\n")


def delete_expense(expenses):
    print("\n>> Deleting Expense...\n")

    while True:

        try:
            # Get user input and convert to an integer
            index_input = input("Enter the number of the expense to delete: ").strip()
            index = int(index_input)

            # Check if the index is valid (within the bounds of the list)
            if 1 <= index <= len(expenses):
                # Valid index, perform the deletion and break the loop
                del expenses[index - 1]
                print("Expense Deleted Successfully!\n")
                break
            else:
                # Invalid index, prompt the user again
                print(f"Error: Index {index} is out of range. Enter a number between 1 and {len(expenses)}.\n")
                continue

        # Catch a ValueError if the input isn't a number
        except ValueError:
            print(f"Error: '{index_input}' is not a valid number. Enter a numerical index.\n")
            continue

        # Catch any other unexpected errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
            continue

