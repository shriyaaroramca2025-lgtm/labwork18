def is_armstrong(n):
    power = len(str(n))
    total = sum(int(digit) ** power for digit in str(n))
    return total == n

# Example
print(is_armstrong(153))  # True

#output-True