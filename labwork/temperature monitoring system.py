ratings = [5, 4, 3, 6, 2, 5, 1, 0, 4]

# Remove invalid ratings (only 1–5 allowed)
ratings = [r for r in ratings if 1 <= r <= 5]

# Average rating
average = sum(ratings) / len(ratings)

# Count 5-star ratings
five_star = ratings.count(5)

# Sort ratings
ratings.sort()

print("Valid Ratings:", ratings)
print("Average Rating:", average)
print("5-Star Ratings:", five_star)
print("Sorted Ratings:", ratings)
