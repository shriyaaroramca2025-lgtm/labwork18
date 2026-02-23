
temperatures = [32, 41, 45, 47, 39, 50, 28, 42]

# Hottest and coldest day
hottest = max(temperatures)
coldest = min(temperatures)

# Replace temperatures above 45°C
updated_temp = ["Heat Alert" if t > 45 else t for t in temperatures]

# Count extreme days (>40°C)
extreme_days = len([t for t in temperatures if t > 40])

print("Hottest Temperature:", hottest)
print("Coldest Temperature:", coldest)
print("Updated List:", updated_temp)
print("Extreme Days:", extreme_days)
