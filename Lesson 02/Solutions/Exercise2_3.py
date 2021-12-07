# Exercise 2.3 Exam Attendance Checker
#
# A student is only allowed to attend the exam if their attendance is greater than or equal to 75%.
#
# Take the following inputs from the user:
#
# 1. The number of classes held.
# 2. The number of classes attended.
#
# and print:
#
# 1. The percentage of classes attended.
# 2. Whether or not the student is allowed to attend the exam.
#
# Note: You can get input from the user via the function input()
#
# Bonus: If the student has a medical cause, allow them to attend the exam.

# The input function gets the input from the user, the int function converts the input to a number
numberOfClassesHeld = int(input("Enter the number of classes held: "))
numberOfClassesAttended = int(input("Enter the number of classes attended: "))

attendancePercentage = (numberOfClassesAttended / numberOfClassesHeld) * 100


msg = ""

if attendancePercentage >= 75:
    msg = "You are allowed to enter than exam."
else:
    medicalCause = input(
        "Do you have a medical reason for missing classes? (Y/N) "
    ).upper()
    if medicalCause == "Y":
        msg = "You are allowed to enter than exam."
    else:
        msg = "You are not allowed to enter than exam."

print("The percentage of classes attended is: " + str(attendancePercentage) + "%")
print(msg)
