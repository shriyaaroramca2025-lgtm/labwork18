
# Create a list of 20 numbers
nums = [1, 5, 3, 7, 5, 9, 2, 5, 8, 6, 5, 4, 3, 5, 10, 11, 5, 12, 13, 5]

print("Original List:")
print(nums)

# Take input from user
n = int(input("Enter a number to delete its extra occurrences: "))

# Check if number exists
if n in nums:
    first_index = nums.index(n)   # first occurrence

    # Create new list keeping only first occurrence
    result = []
    count = 0

    for x in nums:
        if x == n:
            count += 1
            if count == 1:
                result.append(x)  # keep first occurrence
        else:
            result.append(x)

    print("Updated List:")
    print(result)
else:
    print("Number not found in list.")
