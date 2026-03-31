def sort_by_marks(data):
    return sorted(data, key=lambda x: x[1])

# Example
students = [("A", 85), ("B", 92), ("C", 78)]
print(sort_by_marks(students))

#output-[('C', 78), ('A', 85), ('B', 92)]