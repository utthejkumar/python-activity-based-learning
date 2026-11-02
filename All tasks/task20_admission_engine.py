courses = [("CSE", 60, 75), ("ECE", 50, 65)]
candidates = [("Arun", "CSE", 80, 75, 70), ("Esha", "CSE", 75, 75, 75), ("Farid", "CSE", 55, 90, 90), ("Bala", "CSE", 80, 70, 80), ("Gita", "ECE", 60, 60, 60), ("Hari", "ECE", 70, 65, 70), ("Indu", "ECE", 65, 70, 66)]
for cname, minsub, cutoff in courses:
    eligible = []
    rejected = []
    for name, course, m, p, c in candidates:
        if course == cname:
            agg = (m + p + c) / 3
            if m >= minsub and p >= minsub and agg >= cutoff:
                eligible.append((-agg, -m, name))
            else:
                rejected.append(name)
    eligible.sort()
    print(cname, "ranked list (ties broken by maths, then name):")
    rank = 1
    for a, m, name in eligible:
        print("  ", rank, name, "aggregate", round(-a, 2), "maths", -m)
        rank += 1
    print("   Not eligible:", rejected)
