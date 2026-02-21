import csv

summary = {}

with open("transactions.csv") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        category = row["category"]
        amount = float(row["amount"])
        
        summary[category] = summary.get(category, 0) + amount

print("Spending by Category:")
print("----------------------")
sorted_summary = sorted(summary.items(), key=lambda x: x[1])
total_spent = sum(amount for amount in summary.values() if amount < 0)

for category, total in sorted_summary:
    if total < 0:
        print(f"{category:15} ${total:.2f}")

print("----------------------")
print(f"Total Spent: ${total_spent:.2f}")

total_earned = sum(amount for amount in summary.values() if amount > 0)
print(f"Total Earned: ${total_earned:.2f}")

net_income = total_earned + total_spent
print("----------------------")
print(f"Net Income: ${net_income:.2f}")
print()