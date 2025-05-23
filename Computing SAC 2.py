# Prompt the user to enter the total number of students in the class. #
classroom= int(input("Enter the total number of students in your class"))
#Prompt the user to enter the total number of periods of the class held in the week (between 1 and 5).#
periods= int(input("Enter How many periods you had in this week (between 1-5)"))
#For each student, prompt the user to enter the student's name.
#For each student, prompt the user to enter attendance for each period (either 'P' for present or 'A' for absent).
for i in range (classroom):
    if i==3:
        break
    while True:
        pa=("P for present and A for absent")
        else:
            print("You havent put P or A please try again")
student = (str(input(f"Enter the name of student 1:")))
print(input(f"Enter attendance for {student} (P/A) for period 1:"))
print(input(f"Enter attendance for {student} (P/A) for period 2:"))
print(input(f"Enter attendance for {student} (P/A) for period 3:"))
print(input(f"Enter attendance for {student} (P/A) for period 4:"))
print(input(f"Enter attendance for {student} (P/A) for period 5:"))

student1 = (str(input(f"Enter the name of student 2:")))
print(input(f"Enter attendance for {student1} (P/A) for period 1:"))
print(input(f"Enter attendance for {student1} (P/A) for period 2:"))
print(input(f"Enter attendance for {student1} (P/A) for period 3:"))
print(input(f"Enter attendance for {student1} (P/A) for period 4:"))
print(input(f"Enter attendance for {student1} (P/A) for period 5:"))

student2 = (str(input(f"Enter the name of student 3:")))
print(input(f"Enter attendance for {student2} (P/A) for period 1:"))
print(input(f"Enter attendance for {student2} (P/A) for period 2:"))
print(input(f"Enter attendance for {student2} (P/A) for period 3:"))
print(input(f"Enter attendance for {student2} (P/A) for period 4:"))
print(input(f"Enter attendance for {student2} (P/A) for period 5:"))