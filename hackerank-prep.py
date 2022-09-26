def gradingStudents(grades):
    arr = []
    for grade in grades:
        if grade < 38:
            arr.append(grade)
        else:
            for i in range(1, 3):
                temp = grade + i
                if temp % 5 == 0:
                   arr.append(temp)
                   break
                elif i == 2:
                    arr.append(grade)
    return arr
