
# Online Exam Result Processor

scores = [25, 32, 34, 55, 41, 29, 60, 38]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count passed students
passed = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Number of Students Passed:", passed)
