products = [("Pen", 100, 50, 80, 70, 100), ("Book", 60, 40, 30, 70, 80), ("Bag", 20, 10, 25, 3, 30), ("Ink", 50, 0, 20, 35, 40)]
for name, opening, incoming, dispatched, closing, target in products:
    expected = opening + incoming - dispatched
    diff = closing - expected
    if diff == 0:
        status = "matches"
    elif diff < 0:
        status = "shortage of " + str(-diff)
    else:
        status = "surplus of " + str(diff)
    refill = max(0, target - closing)
    print(name, "| expected", expected, "| actual", closing, "|", status, "| replenish", refill)
