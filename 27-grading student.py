def gradingStudents(grades):
    # Write your code here
    for index in range(len(grades)):
        if grades[index] < 38:
            continue
        elif 5-(grades[index] % 5) < 3:
            grades[index] += 5-(grades[index]%5)
    return grades
