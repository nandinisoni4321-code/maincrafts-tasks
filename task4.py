import csv
import os
from datetime import datetime

CSV_FILE = "expenses.csv"
HEADERS = ["id", "date", "description", "amount", "category"]


# Create CSV file if it doesn't exist
def ensure_csv():

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(HEADERS)


# Add Expense
def add_expense():

    description = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))

    except ValueError:
        print("Invalid Amount!")
        return

    category = input("Enter Category: ")

    expense_id = int(datetime.now().timestamp())

    date = datetime.now().strftime("%Y-%m-%d")

    with open(CSV_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([expense_id, date, description, amount, category])

    print("Expense Added Successfully!")


# View All Expenses
def view_all():

    try:

        with open(CSV_FILE, "r") as f:

            reader = csv.reader(f)

            next(reader)

            print("\n------ ALL EXPENSES ------")

            total = 0

            for row in reader:

                print("----------------------------")
                print("ID          :", row[0])
                print("Date        :", row[1])
                print("Description :", row[2])
                print("Amount      :", row[3])
                print("Category    :", row[4])

                total += float(row[3])

            print("----------------------------")
            print("Grand Total =", total)

    except FileNotFoundError:

        print("No Expenses Found")


# Search by Category
def search_category():

    category = input("Enter Category: ")

    found = False

    with open(CSV_FILE, "r") as f:

        reader = csv.reader(f)

        next(reader)

        for row in reader:

            if row[4].lower() == category.lower():

                print("----------------------------")
                print("ID :", row[0])
                print("Date :", row[1])
                print("Description :", row[2])
                print("Amount :", row[3])
                print("Category :", row[4])

                found = True

    if not found:

        print("No Expense Found")


# Monthly Total
def monthly_total():

    month = input("Enter Month (YYYY-MM): ")

    total = 0

    with open(CSV_FILE, "r") as f:

        reader = csv.reader(f)

        next(reader)

        for row in reader:

            if row[1].startswith(month):

                total += float(row[3])

    print("Monthly Total =", total)


# Delete Expense
def delete_expense():

    delete_id = input("Enter ID to Delete: ")

    rows = []

    with open(CSV_FILE, "r") as f:

        reader = csv.reader(f)

        rows = list(reader)

    with open(CSV_FILE, "w", newline="") as f:

        writer = csv.writer(f)

        for row in rows:

            if row[0] != delete_id:

                writer.writerow(row)

    print("Expense Deleted Successfully!")


# Main Menu
def main():
    

    ensure_csv()

    while True:

        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All")
        print("3. Search by Category")
        print("4. Monthly Total")
        print("5. Delete by ID")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_all()

        elif choice == "3":

            search_category()

        elif choice == "4":

            monthly_total()

        elif choice == "5":

            delete_expense()

        elif choice == "6":

            print("Program Closed")
            break

        else:

            print("Invalid Choice")


main()

