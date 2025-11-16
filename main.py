# main.py
# -------------------------------------------
# Expense Tracker Application
# Author: Ben Lufuta
# Date Created: November 14th, 2025
# -------------------------------------------

#Import modules and needed libraries.
from expense_core import add_expense, view_expenses, total_by_category,  delete_expense
from expense_io import load_expenses, save_expenses
import sys


def main():
    
    print("\n=== Expense Tracker ===\n")

    #Load expenses from file.
    expenses = load_expenses()
    
    while True:

        #Print Menu to console
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Total By Category")
        print("4. Remove Expense")
        print("5. Exit\n")

        #Exception handling to process user input
        #If successful, then apply appropriate function/operation
        try:
            choice = int(input("Enter Choice (1-5): ").strip())

            if choice == 1:
                add_expense(expenses)

            elif choice == 2:
                view_expenses(expenses)

            elif choice == 3:
                total_by_category(expenses)

            elif choice == 4:
                delete_expense(expenses)

            elif choice == 5:
                print("\n--- Goodbye ---\n")
                # Save the data before exiting
                save_expenses(expenses) 
                break
            
            #Print message if choice entered is not between 1 and 5.
            else:
                print(f"'{choice}' is an invalid option. Please choose from 1 to 5.\n")
            
        #Print message if non numerial value was entered.
        except ValueError:
            print("Invalid input. Please enter a numerical choice (1, 2, 3, 4, or 5)")

        #Print message and gracefully exit program in case of unexpected error.
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()