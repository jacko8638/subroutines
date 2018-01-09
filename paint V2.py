import time
def input_width():
    #this gets the user to input a value for width and checks if they both entered something and that it is a number.
    global width
    width = input('Please enter the width of the room in metres:')
    if len(width) > 0 and width.isnumeric():
        time.sleep(0.1)
    else:
        print ('You have enterd something that is not a number, please try again.')
        input_width()
input_width()
def input_depth():
    #this gets the user to input a value for depth and checks if they both entered something and that it is a number.
    global depth
    depth = input('Please enter the depth of the room in metres:')
    if len(depth) > 0 and depth.isnumeric():
        time.sleep(0.1)
    else:
        print ('You have enterd something that is not a number, please try again.')
        input_depth()
input_depth()
def input_height():
    #this gets the user to input a value for height and checks if they both entered something and that it is a number.
    global height
    height = input('Please enter the height of the room in metres:')
    if len(height) > 0 and height.isnumeric():
        time.sleep(0.1)
    else:
        print ('You have enterd something that is not a number, please try again.')
        input_height()
input_height()
def input_non_paint():
    #this gets the user to input a value for the unpaintable areas and checks if they both entered something and that it is a number.
    global non_paint
    non_paint = input('Please enter the total area of any un-paintable areas such as windows or doors.')
    if len(non_paint) > 0 and non_paint.isnumeric():
        time.sleep(0.1)
    else:
        print ('You have enterd something that is not a number, please try again.')
        input_non_paint()
input_non_paint()
def input_coats():
    #this gets the user to input a value for the amount of coats they want and checks if they both entered something and that it is a number.
    global coats
    coats = input('How many coats would you like to put on (the suggested is two)')
    if len(coats) > 0 and coats.isnumeric():
        time.sleep(0.1)
    else:
        print ('You have enterd something that is not a number, please try again.')
        input_coats()
input_coats()
ceiling = int(width, base=10) * int(depth, base=10)
wall = int(height, base=10) * int(depth, base=10)
paintable = wall + wall + wall + wall + ceiling - int(non_paint, base=10)
paintable = paintable * int(coats, base=10)
#this module works out the total area that needs painting
paint_needed = paintable / 11    #it is assumed that 11 litres is needed per metre squared
print (' You will need %s litres of paint' % paint_needed) 
#the final module relays the result of the calculations back to the user
