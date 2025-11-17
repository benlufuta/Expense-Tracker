# expense_io.py
# -------------------------------------------
# Expense Tracker Application
# Author: Ben Lufuta
# Date Created: November 14th, 2025
# -------------------------------------------

import json
import os

file_path = "expenses_data.json"

def load_expenses():

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)
    
    try:
        with open(file_path, "r") as f:
            content = f.read().strip()

        if content:
            return json.loads(content)
        
        else:
            return []
        
    except Exception as e:
        print(f"An unexpected error occurred while loading data: {e}")
        return []


def save_expenses(expenses):
    
    try:
        with open(file_path, "w") as f:
            json.dump(expenses, f,  indent=4)

    except TypeError as e:
        print(f"Error: Data not JSON serializable - {e}")

    except PermissionError as e:
        print(f"Error: Permission denied for file {file_path} - {e}")

    except FileNotFoundError as e:
        print(f"Error: Directory for file {file_path} not found - {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
