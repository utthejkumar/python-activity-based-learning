capacity = 1000
level = 400
threshold = 800
inflow = [300, 250, 400, 100, 900, 600]
outflow = [200, 300, 150, 900, 100, 100]
first = 0
for i in range(len(inflow)):
    level += inflow[i] - outflow[i]
    note = ""
    if level > capacity:
        note = "overflow of " + str(level - capacity)
        level = capacity
    elif level < 0:
        note = "shortage of " + str(-level)
        level = 0
    if level >= threshold and first == 0:
        first = i + 1
    print("Interval", i + 1, "level", level, note)
if first:
    print("Threshold", threshold, "first reached in interval", first)
else:
    print("Threshold never reached")
