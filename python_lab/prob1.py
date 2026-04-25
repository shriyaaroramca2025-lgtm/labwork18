def second_largest(lst):
    largest = second = float('-inf')
    
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
            
    return second

# Example
print(second_largest([10, 20, 4, 45, 99]))  # 45

# Output: 45
