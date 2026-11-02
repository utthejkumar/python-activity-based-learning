subjects = [("Maths", 30, 40), ("Physics", 25, 40), ("Python", 35, 40)]
required = 75
scenarios = [0, 2, 5]
for name, attended, total in subjects:
    print(name, "current attendance:", round(attended / total * 100, 2), "%")
    for missed in scenarios:
        x = 0
        while (attended + x) / (total + x + missed) * 100 < required:
            x += 1
        print("  if", missed, "other classes are missed, attend", x, "consecutive classes")
