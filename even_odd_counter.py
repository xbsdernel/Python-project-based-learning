oddCounter = 0
evenCounter = 0

def greeting():
    print("Welcome to even / odd counter")

def entering_numbers(count, oddCounter, evenCounter):
    while count > 0:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            evenCounter+=1
            count -= 1
        elif number % 2 != 0:
            oddCounter+=1
            count -= 1
        else:
            print("try again and enter a valid number!")
    return evenCounter, oddCounter

def result(evenCounter, oddCounter):
    print("There are",evenCounter,"even numbers")
    print("There are",oddCounter,"odd numbers")
greeting()
count = int(input("write the number of numbers you wanna enter: "))
evenCounter, oddCounter = entering_numbers(count, oddCounter, evenCounter)
result(evenCounter, oddCounter)