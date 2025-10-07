def greeting():
    print("Welcome to my tax / discount calculator")

def calculating():
    price = float(input("Enter the original price: "))
    tax = float(input("enter the tax rate or discount rate: "))
    total_cost = price + (price * (tax/100))
    print("The total cost now is:", total_cost)

greeting()
calculating()