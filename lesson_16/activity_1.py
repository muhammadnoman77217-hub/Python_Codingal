try:
    num = int(input("Enter a number"))
    print("the number is", num)
except ValueError as ex:
    print("Error : ", ex)