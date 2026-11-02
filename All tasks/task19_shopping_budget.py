items = [["Shoes", 1500, 2], ["Shirt", 800, 3], ["Bag", 1200, 1], ["Cap", 300, 4]]
budget = 5000
original = [i[2] for i in items]
while True:
    total = 0
    for n, p, q in items:
        line = p * q
        if line >= 2000:
            line *= 0.9
        total += line
    if total <= budget:
        break
    pick = -1
    for i in range(len(items)):
        if items[i][2] > 0 and (pick == -1 or items[i][1] > items[pick][1]):
            pick = i
    items[pick][2] -= 1
for i in range(len(items)):
    n, p, q = items[i]
    print(n, "| wanted", original[i], "| buy", q, "| reduced by", original[i] - q)
print("Final total: Rs.", round(total, 2), "Budget: Rs.", budget)
