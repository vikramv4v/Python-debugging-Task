print("Multi-Level Grade Engine")
subjects = int(input("Enter subjects: "))

i = 0
total = 0
fail = 0

while i < subjects:
    marks = int(input("Enter marks: "))
    total = total + marks
    if marks < 35:
        fail = fail + 1
    i = i + 1

percentage = total / subjects

if percentage > 100:
    print("Invalid percentage")
else:
    print("Percentage:", percentage)
    print("Fails:", fail)

    if fail > 0:
        print("Overall Result: Fail")
    elif percentage >= 85:
        print("Grade: A+")
    elif percentage >= 70:
        print("Grade: A")
    elif percentage >= 50:
        print("Grade: B")
    else:
        print("Grade: C")
