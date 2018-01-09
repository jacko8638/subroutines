pupilName = input("What is your name?")
table = input("Enter your Table:")
startnum = input("Enter your start number:")
endnum = input("Enter your end number: ")
def multiples():
    print("Hi,", pupilName, "here is your times tables")
    for x in range(int(startnum), int(endnum) + 1):
        ans = int(table) * x
        print(table, " x ", x, " = ", ans)
multiples()