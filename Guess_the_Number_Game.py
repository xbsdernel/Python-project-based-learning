import random


def greeting():
    print("welcome to out game :/)")


number = random.randint(1, 100)

print(number)
def looping():
    heart = 20
    while True:
        if heart == 0:
            print("you have 0 heart now, you have lost !")
        guess = int(input("guess a number: "))
        if guess == number:
            print("You have won! congrats")
            break
        elif abs(number - guess) <= 10:
            print("You're very close")
        else:
            print("try again :/(")
        heart -= 1


greeting()
looping()


