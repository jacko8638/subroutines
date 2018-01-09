from time import sleep
# Global variables
namelist = {}


# subroutines
def displaymenu():
    # this subroutine displays the menu and lets the user input their option
    print("Please pick an option:\n")
    sleep(0.5)
    print("1.Add a name.")
    print("2. Display all names.")
    print("3. Quit.")
    sleep(0.5)
    option = input("Please enter your choice(1,2 or 3):")
    return option


def addname():
    # this subroutine adds a name to the dictionary

    name = input("Enter the Name you wish to add the list: ")
    sleep(0.25)
    position = input("Enter where in the list you want to put the name(1-10):")

    # this checks if name and position are both correct and that they have entered something
    if name.isalpha() and len(name) > 0 and position.isnumeric() and len(position) > 0:
        #this checks if the position is between 1 and 10
        if int(position) > 0 and int(position) < 11:
            namelist[position] = name
            sleep(1)
            print("Name has been added to the list.")
            sleep(1)
        else:
            print("Error, position was not valid.")
    else:
        print("There was an error in what you entered."+"\n")
        sleep(0.25)
        print("Please try again."+"\n")
        sleep(1)


def displaynames():
    #prints all the names and their places
    print ("The names in the list are:")
    sleep(0.25)
    for keys,values in namelist.items():
        print(keys, values)
        sleep(0.1)


# main program
loop = 1
while int(loop) == 1:
    choice = displaymenu()
    if int(choice) == 1:
        addname()
    elif int(choice) == 2:
        displaynames()
    elif int(choice) == 3:
        loop = 2
        sleep(1)
        print("PROGRAM TERMIATING")
    else:
        print("Error, please try again")

