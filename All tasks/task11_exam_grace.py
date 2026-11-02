students = [("Asha", [45, 38, 60, 72, 34]), ("Ravi", [30, 35, 28, 50, 41]), ("Meena", [90, 85, 78, 92, 88]), ("Kiran", [34, 20, 55, 40, 36])]
pass_mark = 35
max_mark = 100
grace_limit = 5
for name, marks in students:
    original = marks[:]
    need = 0
    for m in marks:
        if m < pass_mark:
            need += pass_mark - m
    if need == 0:
        result = "Pass"
    elif need <= grace_limit:
        for i in range(len(marks)):
            if marks[i] < pass_mark:
                marks[i] = min(pass_mark, max_mark)
        result = "Pass with grace"
    else:
        result = "Fail"
    avg = sum(marks) / len(marks)
    if result == "Fail":
        grade = "Fail"
    elif avg >= 75:
        grade = "Distinction"
    elif avg >= 60:
        grade = "First Class"
    elif avg >= 50:
        grade = "Second Class"
    else:
        grade = "Pass Class"
    print(name, original, "->", marks, "|", result, "|", grade, "| avg", round(avg, 2))
