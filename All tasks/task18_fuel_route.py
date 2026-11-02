distance = 450
vehicles = [("Car", 15, 105, 5, 45), ("Bike", 40, 105, 2, 12), ("SUV", 10, 98, 8, 60), ("Truck", 5, 90, 10, 100)]
best = ""
best_cost = 0
for name, mileage, price, reserve, tank in vehicles:
    fuel = distance / mileage
    cost = fuel * price
    if fuel + reserve <= tank:
        print(name, "| fuel", round(fuel, 2), "L | cost Rs.", round(cost, 2), "| feasible")
        if best == "" or cost < best_cost:
            best = name
            best_cost = cost
    else:
        print(name, "| fuel", round(fuel, 2), "L + reserve", reserve, "exceeds tank", tank, "| not feasible")
print("Lowest cost feasible option:", best, "Rs.", round(best_cost, 2))
