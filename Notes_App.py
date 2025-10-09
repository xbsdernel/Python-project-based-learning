notes = []

def looping_on_notes():
    number = 1
    for note in notes:
        print(number, "-", note)
        number += 1


def add_notes():
    print("Write your note: ")
    note = input()
    notes.append(note)


def view_notes():
    looping_on_notes()


def delete_notes():
    print("You can choose a specific note to remove.")
    looping_on_notes()
    number = int(input("Enter the note`s number to delete: "))
    if number > 0 and number <= len(notes):
        notes.pop(number-1)
        print("note have been deleted suscessfully")
    else:
        print("The number is out of boundries! the note have not been deleted")


def save_notes():
    if len(notes) == 0:
        print("you have to write 1 note at least!")
    else:
        print("Write the file name")
        name = input()
        name = name + ".txt"
        with open(name, "w") as file:
            for note in notes:
                file.write(note + "\n")

def read_notes():
    print("Write the file name")
    name = input()
    name = name + ".txt"
    file = open(name)
    print(file.read())


def looping():
    while True:
        print("1- Add new note")
        print("2- view all notes")
        print("3- delete a note")
        print("4- Save notes to a file")
        print("5- Read notes from a file")
        print("6- Exit")
        choice = int(input("choose a number: "))
        if choice == 1:
            add_notes()
        elif choice == 2:
            view_notes()
        elif choice == 3:
            delete_notes()
        elif choice == 4:
            save_notes()
        elif choice == 5:
            read_notes()
        elif choice == 6:
            return 0
        else:
            print("number out of boundries, try again!")
            continue


looping()