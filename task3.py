import csv
def add_expense():

    desc = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))

        category = input("Enter Category: ")

        with open("expenses.csv", "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([desc, amount, category])

        print("Expense Added Successfully!")

    except ValueError:

        print("Invalid Amount. Please enter a valid number.")
add_expense()

def view_expenses():

    try:

        with open("expenses.csv", "r") as f:

            reader = csv.reader(f)

            print("\n----- Expenses -----")

            for row in reader:

                print("Description :", row[0])
                print("Amount      :", row[1])
                print("Category    :", row[2])
                print()

    except FileNotFoundError:

        print("No expenses found.")
view_expenses()
def search_category():

    category = input("Enter Category: ")

    try:

        with open("expenses.csv", "r") as f:

            reader = csv.reader(f)

            print("\n----- Matching Expenses -----")

            for row in reader:

                if row[2].lower() == category.lower():

                    print("Description :", row[0])
                    print("Amount      :", row[1])
                    print("Category    :", row[2])
                    print()

    except FileNotFoundError:

        print("No expenses found.")
search_category()

def total_per_category():

    category = input("Enter Category: ")

    total = 0

    try:

        with open("expenses.csv", "r") as f:

            reader = csv.reader(f)

            for row in reader:

                if row[2].lower() == category.lower():

                    total += float(row[1])

        print("Total", category, "Expense =", total)

    except FileNotFoundError:

        print("No expenses found.")
total_per_category()

def main():

    while True:

        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total Per Category")
        print("5. Exit")

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

            print("Program Closed")
            break

        else:

            print("Invalid Choice")
main()