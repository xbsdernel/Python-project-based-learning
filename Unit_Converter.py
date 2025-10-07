def greeting():
    print("Welcom to our Unit Converter")

def converstions():
    print("1- Millimeters to Centimeters")
    print("2- Centimeters to Meters")
    print("3- Meters to Kilometers")
    print("4- Inches to Centimeters")
    print("5- Feet to Meters")
    print("6- Yards to Meters")
    print("7- Miles to Kilometers")
    print("8- Celsius to Fahrenheit")
    print("9- Celsius to Kelvin")
    print("10- Milliliters to Liters")
    print("0- Exit")

def converting():
    while True:
        print("Choose your converstions: ")
        converstions()
        choice = int(input())
        if choice == 1:
            number = float(input("Enter the number: "))
            print(number / 10 ,"Centimeters")

        elif choice == 2:
            number = float(input("Enter the number: "))
            print(number / 100 ,"Meters")

        elif choice == 3:
            number = float(input("Enter the number: "))
            print(number / 1000 ,"Kilometers")

        elif choice == 4:
            number = float(input("Enter the number: "))
            print(number / 2.54 ,"Centimeters")

        elif choice == 5:
            number = float(input("Enter the number: "))
            print(number * 0.3048 ,"Meters")

        elif choice == 6:
            number = float(input("Enter the number: "))
            print(number * 0.9144 ,"Meters")

        elif choice == 7:
            number = float(input("Enter the number: "))
            print(number / 1.609 ,"Kilometers")

        elif choice == 8:
            number = float(input("Enter the number: "))
            print((number - 32 ) * (5/9) ,"Fahrenheit")

        elif choice == 9:
            number = float(input("Enter the number: "))
            print(number - 273.15,"Kelvin")

        elif choice == 10:
            number = float(input("Enter the number: "))
            print(number / 1000,"Liters")
        elif choice == 0:
            break
        else:
            print("Choose a valid number and try again")
            continuo


greeting()
converting()