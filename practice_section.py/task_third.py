grade =[]
print (grade)
marks1 = int(input("Enter marks for subject 1: "))
grade.append(marks1)
marks2 = int(input("Enter marks for subject 2: "))  
grade.append(marks2)
marks3 = int(input("Enter marks for subject 3: "))
grade.append(marks3)
average = sum(grade)/len(grade)
result = "pass" if average >=40 else "fail"
print(f"average: {average:.1f} - result: {result}")

