print("==== Student Grade calculator====")
name = input("Enter student name:")
subjects=int(input("Enter number of subjects:"))
marks = []
for i in range(subjects):
    mark=float(input(f"enter marks for subject{i+1}:"))
    marks.append(mark)
    total=sum(marks)
    percentage=total / subjects

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"    
    elif percentage >= 70:
        grade = "B"  
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

print("\n==== Result ====")
print("Student Name:",name)
print("Total Marks:",total)
print("Percentage:",
      round(percentage,2),"%")
print("Grade:",grade)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")    

                     