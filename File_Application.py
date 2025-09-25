def calculate_grade(line):
    line = line[:-1]
    data_list = line.split(':')

    student_name = data_list[0]
    grades = data_list[1].split(',')

    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    average = (grade1 + grade2 + grade3) / 3

    if 90 <= average <= 100: letter_grade = "AA"
    elif 80 <= average < 90: letter_grade = "BA"
    elif 75 <= average < 80: letter_grade = "BB"
    elif 70 <= average < 75: letter_grade = "CB"
    elif 65 <= average < 70: letter_grade = "CC"
    elif 60 <= average < 65: letter_grade = "DC"
    elif 50 <= average < 60: letter_grade = "DD"
    elif 40 <= average < 50: letter_grade = "FD"
    else: letter_grade = "FF"

    return f"{student_name} : {letter_grade} - ({average})\n"


def input_grades():
    first_name = input("Student First Name: ")
    last_name = input("Student Last Name: ")
    grade1 = input("Grade 1: ")
    grade2 = input("Grade 2: ")
    grade3 = input("Grade 3: ")

    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(first_name + " " + last_name + ":" + grade1 + "," + grade2 + "," + grade3 + "\n")


def read_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))


def save_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        results_list = []

        for line in file:
            results_list.append(calculate_grade(line))

        with open("results.txt", "w", encoding="utf-8") as file2:
            file2.writelines(results_list)


while True:
    operation = int(input("1-Input Grades\n2-Read Grades\n3-Save Grades\n4-Exit\nSelection: "))
    if operation == 1:
        input_grades()
    elif operation == 2:
        read_grades()
    elif operation == 3:
        save_grades()
    else:
        break
