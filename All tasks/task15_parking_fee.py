records = [("car", "09:30", "12:10"), ("bike", "22:00", "06:00"), ("truck", "08:00", "19:30"), ("car", "25:10", "10:00"), ("van", "10:00", "11:00")]
for v, a, b in records:
    if v == "car":
        rate, cap = 20, 200
    elif v == "bike":
        rate, cap = 10, 100
    elif v == "truck":
        rate, cap = 40, 400
    else:
        print(v, a, b, "-> invalid vehicle")
        continue
    ok = True
    for t in (a, b):
        if not (len(t) == 5 and t[2] == ":" and t[:2].isdigit() and t[3:].isdigit() and int(t[:2]) < 24 and int(t[3:]) < 60):
            ok = False
    if not ok:
        print(v, a, b, "-> invalid time")
        continue
    mins = int(b[:2]) * 60 + int(b[3:]) - int(a[:2]) * 60 - int(a[3:])
    overnight = mins < 0
    if overnight:
        mins += 1440
    fee = min(((mins + 59) // 60) * rate, cap)
    if overnight:
        fee += 50
    if mins > 600:
        fee += 100
    print(v, a, b, "-> fee Rs.", fee, "| overnight" if overnight else "", "| penalty" if mins > 600 else "")
