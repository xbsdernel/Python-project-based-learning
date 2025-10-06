def greeting():
    print("Welcome to The Grade Calculator")

Grades = {
    "A": 100,
    "B": 90,
    "C": 80,
    "D": 70,
    "E": 60,
    "F": 50,
}

def enteringGrades():
    Total_grades = 0
    for i in range(1,7,1):
        print("Enter your Subject", i,"Grade: ")
        Subject = input()
        #if Grades[Subject] != number:
            #print("enter a valid graid !")
            #continue
        Total_grades += Grades[Subject]
    return Total_grades

def calculate_grade(Total_grades):
    return (Total_grades / 600 ) * 100

def printing(Grade):
    print("Your total grades is", Grade, "%")

greeting()
Total_grades = enteringGrades()
Grade = calculate_grade(Total_grades)
printing(Grade)