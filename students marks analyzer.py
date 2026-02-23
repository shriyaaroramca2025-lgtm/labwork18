
# Student Marks Analyzer

marks = [78, 95, -5, 102, 88, 67, 95, 45]

# Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

# Calculate average
average = sum(valid_marks) / len(valid_marks)

# Find topper(s)
top_score = max(valid_marks)
toppers = [m for m in valid_marks if m == top_score]

# Display grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Valid Marks:", valid_marks)
print("Average:", average)
print("Topper Score:", toppers)
print("Grade:", grade)
