#File Handling 
#using with function

# with open("notes.txt", "r") as f:
#     print(f.read())
    


# with open("notes.txt",  "w") as f:
#     f.write("maincrafts technology")
#     print("overwite the file")

    

# with open("notes.txt",  "a") as f :
#     f.write("\npython programing domain")


#CSV Basics

# import csv #import csv module
# with open("expenses.csv", "a", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["lunch", 120])

#mini project making function to save expenses in csv file

# import csv

# def add_expense(desc, amount):

#     with open("expenses.csv", "a", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow([desc, amount])
        

# #calling function

# add_expense("Lunch", 120)
# add_expense("Movie", 250)

#Function + menu driven program + while loop
# def greet():
#     print("Hello")
#calling function
# greet()


# while True:

#     num = input("Enter x to exit: ")

#     if num == "x":
#         break

# while True:
#     print("\n expenses tracker")
    
#     print("1. add expenses")
#     print("2. view expenses")
#     print("3.exit")
    
#     choice = input("enter choice")
    
#     if choice == "1":
#         print("add expenses selected")
#     elif choice == "2":
#         print("view expenses selected")
#     elif choice == "3":
#         print("program closed")
#         break
    
        
#     else:
#         print("invalid choice")    
    
# view expenses and total spent

# import csv

# with open("expenses.csv", "r") as f:

#     reader = csv.reader(f)

#     for row in reader:
#         print(row)

# import csv

# def view_expenses():

#     with open("expenses.csv", "r") as f:

#         reader = csv.reader(f)

#         for row in reader:

#             print(row[0], "-", row[1])

# view_expenses()
            
            
# import csv

# def total_spent():

#     total = 0

#     with open("expenses.csv", "r") as f:

#         reader = csv.reader(f)

#         for row in reader:

#             total = total + int(row[1])

#     print("Total =", total)
# total_spent()


# systamatic task 2 project

import csv
#add expenses function

def add_expenses():
    desc = input("enter description :")
    
    try:
        amount = float(input("enter amount :"))
        with open("expenses.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([desc, amount])
        print("expenses add succesfully! ")
    except ValueError:
        print("invalid amount, add valid number")
#view expenses function
def view_expenses():
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            print("\n-----------expenses-----------")
            for row in reader :
                print(row[0], "-", row[1])
    except FileNotFoundError:
        print("No expenses found")
        
#Total expenses function
def total_spent():
    total = 0
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total = total + float(row[1])
                print("\nTotal Spent =", total)

    except FileNotFoundError:

        print("No expenses found.")

#main function
def main():

    while True:

        print("\n===== Expense Tracker =====")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            add_expenses()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            total_spent()

        elif choice == "4":

            print("Program Closed")
            break

        else:

            print("Invalid Choice")


# Program Start
main()

        
        
        
        
        
            
        
    