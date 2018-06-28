while 1:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print ("Not a valid number")