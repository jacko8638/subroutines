# variables
rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
columns = [1, 2, 3, 4, 5, 6]
carpark = {}
# subroutines
def options():
    #displays menu
    print("1. Reset all spaces in the car park to ‘empty’")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit\n")
    x = input("Enter your choice: ")
    return x
def emptycarpark(carpark):
        carpark.clear() # clears the carpark entries.
    print("All cars have been removed")
def parkacar(carpark):
    registration = input("Please enter your number plate: ") # inputs the registration
    r = input("Enter the row that you parked in: ") # inputs the row
    c = input("Enter the column that you are parked in: ") # inputs the column
    emp = 1
    while emp == 1:
        if registration in carpark.values()
            print("There is already a car parked in this space.")
            registration = input("Please enter your number plate:")
            r = input("Enter the row that you parked in: ")
            c = input("Enter the column that you are parked in: ")
        else:
            emp = 0 # changes emp so while loop is broken
    carpark[r, c] = registration
def removeacar(carpark):

def displaycarparkgrid(carpark):
    print (carpark)

    # main program
    # initialise car park grid to “empty”
    #display menu of options
    # accept choice
option = options()
while option != "5":
    if option == "1":
        emptycarpark(carpark)
    elif option == "2":
        parkacar(carpark)
    elif option == "3":
        removeacar(carpark)
    elif option == "4":
        displaycarparkgrid(carpark)
    else:
        option = ("Invalid choice - please re-enter: ")
print("Goodbye,don't forget to leave your keys at the office.")





