subjects = ["Maths", "Physics", "Python"]
students = [("Asha", [[70, 65, 80], [40, 45, 38], [55, 60, 62]]), ("Ravi", [[80, 75, 70], [60, 55, 50], [90, 85, 82]]), ("Meena", [[45, 48, 40], [70, 60, 75], [30, 35, 40]])]
for name, scores in students:
    print(name)
    weak = []
    e1 = e2 = e3 = 0
    for s in range(3):
        a, b, c = scores[s]
        print("  ", subjects[s], "E1->E2:", b - a, "E2->E3:", c - b)
        if a < 50 and b < 50 and c < 50:
            weak.append(subjects[s])
        e1 += a
        e2 += b
        e3 += c
    if e1 < e2 < e3:
        trend = "Improving"
    elif e1 > e2 > e3:
        trend = "Declining"
    else:
        trend = "Inconsistent"
    print("   Exam totals:", e1, e2, e3, "| Trend:", trend, "| Weak subjects:", weak)
