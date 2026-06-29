import csv


# ------------------ Add Expense ------------------

def add_expense():

    desc = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        month = input("Enter Month: ")

        with open("expenses.csv", "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([desc, amount, category, month])

        print("\nExpense Added Successfully!\n")

    except ValueError:

        print("\nInvalid Amount! Please enter a valid number.\n")


# ------------------ View Expenses ------------------

def view_expenses():

    try:

        with open("expenses.csv", "r") as f:

            reader = csv.reader(f)

            print("\n========== ALL EXPENSES ==========\n")

            for row in reader:

                print("--------------------------------")
                print("Description :", row[0])
                print("Amount      :", row[1])
                print("Category    :", row[2])
                print("Month       :", row[3])

            print("--------------------------------")

    except FileNotFoundError:

        print("No expenses found.")


# ------------------ Search Category ------------------

def search_category():

    category = input("Enter Category to Search: ")

    found = False

    try:

        with open("expenses.csv", "r") as f:

            reader = csv.reader(f)

            print("\n===== SEARCH RESULT =====\n")

            for row in reader:

                if row[2].lower() == category.lower():

                    print("--------------------------------")
                    print("Description :", row[0])
                    print("Amount      :", row[1])
                    print("Category    :", row[2])
                    print("Month       :", row[3])

                    found = True

            if not found:

                print("No Expense Found.")

    except FileNotFoundError:

        print("No expenses found.")


# ------------------ Total Per Category ------------------

def total_per_category():

    category = input("Enter Category: ")

    total = 0

    try:

        with open("expenses.csv", "r") as f:

            reader = csv.reader(f)

            for row in reader:

                if row[2].lower() == category.lower():

                    total += float(row[1])

        print("\nTotal", category, "Expense =", total)

    except FileNotFoundError:

        print("No expenses found.")


# ------------------ Monthly Spending ------------------

def monthly_spending():

    month = input("Enter Month: ")

    total = 0

    try:

        with open("expenses.csv", "r") as f:

            reader = csv.reader(f)

            for row in reader:

                if row[3].lower() == month.lower():

                    total += float(row[1])

        print("\nTotal Spending in", month, "=", total)

    except FileNotFoundError:

        print("No expenses found.")


# ------------------ Main Menu ------------------

def main():

    while True:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total Per Category")
        print("5. Monthly Spending")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            search_category()

        elif choice == "4":

            total_per_category()

        elif choice == "5":

            monthly_spending()

        elif choice == "6":

            print("\nProgram Closed Successfully!")
            break

        else:

            print("\nInvalid Choice! Please Try Again.")


# ------------------ Program Starts ------------------

main()