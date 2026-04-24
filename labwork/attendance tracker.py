
# Attendance Tracker

attendance = [1, 1, 0, 0, 1, 0, 0, 0, 1]

# Attendance percentage
percentage = (sum(attendance) / len(attendance)) * 100

# Below 75%
if percentage < 75:
    print("Warning: Attendance below 75%")

# Replace consecutive absences with warning flag
result = []
for i in range(len(attendance)):
    if i > 0 and attendance[i] == 0 and attendance[i-1] == 0:
        result.append("WARNING")
    else:
        result.append(attendance[i])

print("Attendance %:", percentage)
print("Updated Record:", result)
