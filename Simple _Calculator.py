def greating():
    print("Welcome to our calculator")

def inputs():
    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))
    return number_1, number_2
def printing_operations():
    print("1 for +")
    print("2 for -")
    print("3 for *")
    print("4 for /")
    print("5 for Exit")


greating()
number_1, number_2 = inputs()
while True:
    printing_operations()
    operation = int(input("choose a number for the operation: "))
    if operation == 1:
        print(number_1, "+", number_2, "= ", number_1 + number_2)
        break
    elif operation == 2:
        print(number_1, "-", number_2, "= ", number_1 - number_2)
        break
    elif operation == 3:
        print(number_1, "*", number_2, "= ", number_1 * number_2)
        break
    elif operation == 4:
        if number_2 != 0:
            print(number_1, "/", number_2, "= ", number_1 / number_2)
            break
        else:
            print("can`t divison by ZERO! choose another operation or close the program")
    elif operation == 5:
        break
    else:
        print("Invalid number! try again")