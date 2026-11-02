balance = 5000
limit = 2000
transactions = [("D", 1000), ("W", 3000), ("W", 1500), ("D", -200), ("W", 7000), ("X", 100), ("W", 2000)]
deposits = 0
withdrawals = 0
rejected = 0
for kind, amt in transactions:
    reason = ""
    if kind not in ("D", "W") or amt <= 0:
        reason = "invalid transaction"
    elif kind == "W" and amt > limit:
        reason = "withdrawal limit exceeded"
    elif kind == "W" and amt > balance:
        reason = "insufficient balance"
    if reason:
        rejected += 1
        print(kind, amt, "rejected:", reason)
    elif kind == "D":
        balance += amt
        deposits += amt
        print(kind, amt, "done, balance", balance)
    else:
        balance -= amt
        withdrawals += amt
        print(kind, amt, "done, balance", balance)
print("Deposited:", deposits, "Withdrawn:", withdrawals, "Rejected:", rejected, "Final balance:", balance)
