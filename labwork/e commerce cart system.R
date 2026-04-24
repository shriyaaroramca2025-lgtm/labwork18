
# E-Commerce Cart System

prices = [1200, 1500, 1200, 2000, 800]

# Remove duplicates
unique_prices = list(set(prices))

# Total amount
total = sum(unique_prices)

# Apply discount
if total > 5000:
    total *= 0.9   # 10% discount

# Add GST 18%
final_amount = total * 1.18

print("Unique Items:", unique_prices)
print("Final Payable Amount:", final_amount)
