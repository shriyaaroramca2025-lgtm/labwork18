
# Salary Processing System

salaries = [25000, 60000, 45000, 80000, 30000, 52000]
minimum_wage = 30000

# Remove below minimum wage
valid_salaries = [s for s in salaries if s >= minimum_wage]

# Add 5% bonus if salary > 50000
updated = []
for s in valid_salaries:
    if s > 50000:
        s *= 1.05
    updated.append(s)

# Sort descending
updated.sort(reverse=True)

# Top 3 salaries
top3 = updated[:3]

print("Processed Salaries:", updated)
print("Top 3 Salaries:", top3)
