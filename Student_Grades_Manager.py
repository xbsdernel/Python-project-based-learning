def greeting():
    print("Welcome to our grade tracking system for students")


student_names = []
student_grades = []


def Compute_average_grades():
    average = 0
    for index in student_grades:
        average += index
    return average / len(student_grades)


def Compute_highest_grades():
    highest = 0
    for index in student_grades:
        highest = max(index, highest)
    return highest


def Compute_lowest_grades():
    lowest = 0
    for index in student_grades:
        lowest = min(index, lowest)
    return lowest


def adding_students_with_grades():
    name = input("Enter the student name: ")
    grade = int(input("Enter the student grade: "))
    student_names.append(name)
    student_grades.append(grade)


def printing_student_grades():
    number = 1
    for index in student_names:
        print(number, "-", index, ":", student_grades[number - 1])
        number += 1


def remove_student_entries():
    print("Choose the student number to remove: ")
    printing_student_grades()
    index = int(input())
    if index < 0 or index > len(student_grades):
        print("invalid index, can`t delete the student entrie")
    else:
        student_names.pop(index - 1)
        student_grades.pop(index - 1)


def printing_report():
    lowest = Compute_lowest_grades()
    highest = Compute_highest_grades()
    average = Compute_average_grades()
    print("The formal report o the students")
    printing_student_grades()
    print("The highest grade:", highest)
    print("The lowest grade:", lowest)
    print("The average grade:", average)


def choices():
    choice = int(input("enter a number: "))
    if choice == 1:
        adding_students_with_grades()
    elif choice == 2:
        remove_student_entries()
    elif choice == 3:
        printing_report()
    elif choice == 4:
        return 0
    else:
        print("invalid choice try again")


def menu():
    while True:
        greeting()
        print("1- Add new student with his grade")
        print("2- Remove a student with his grade")
        print("3- Display the Final Report")
        print("4- exit")
        choices()


menu()