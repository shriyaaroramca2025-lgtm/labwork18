
# List of product stock quantities
stock = [25, 0, 8, 3, 50, 0, 12]

# Remove items with 0 stock
stock = [item for item in stock if item != 0]

# Add restock (add 50 units) to items below 10
stock = [item + 50 if item < 10 else item for item in stock]

# Find total inventory count
total_inventory = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory:", total_inventory)
