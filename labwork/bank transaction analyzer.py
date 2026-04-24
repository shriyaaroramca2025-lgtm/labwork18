transactions = [5000, -2000, 15000, -7000, 25000, -1000]

# Total balance
total_balance = sum(transactions)

# Largest withdrawal (most negative value)
withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals)

# Deposits greater than ₹10,000
large_deposits = [t for t in transactions if t > 10000]
count_large_deposits = len(large_deposits)

print("Total Balance:", total_balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", count_large_deposits)
