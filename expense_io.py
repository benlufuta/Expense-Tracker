# expense_io.py
# -------------------------------------------
# Expense Tracker Application
# Author: Ben Lufuta
# Date Created: November 14th, 2025
# -------------------------------------------

import json
import os

def load_expenses():

    if not os.path.exists("expenses_data.json"):
        with open("expenses_data.json", "w") as f:
            json.dump([], f)
    
    with open("expenses_data.json", "r") as f:

        content = f.read().strip()

        if content:

            return json.loads(content)
        
        else:
            return []


def save_expenses(expenses):
    
    with open("expenses_data.json", "w") as f:

        json.dump(expenses, f,  indent=4)