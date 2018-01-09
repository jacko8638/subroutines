def multiples(table, startnum, endnum, pupilName):
    print("Hi,", pupilName , "... here is your times table")
    for x in range(startnum, endnum + 1):
        ans = table * x
        print(table, 'x', x , "=", ans)
pupilName = input("What is your name?")
table = input("Enter your Table:")
startnum = input("Enter your start number:")
endnum = input("Enter your end number")
multiples(int(table), int(startnum), int(endnum), pupilName)
