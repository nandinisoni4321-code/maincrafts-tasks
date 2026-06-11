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

import csv

def add_expense(desc, amount):

    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])
        

#calling function

add_expense("Lunch", 120)
add_expense("Movie", 250)



