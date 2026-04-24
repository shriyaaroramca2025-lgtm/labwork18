
points = [12, -5, 30, 25, -2, 18]

# Replace negative points with 0
points = [p if p >= 0 else 0 for p in points]

# Sort leaderboard (descending)
leaderboard = sorted(points, reverse=True)

# Winner and runner-up
winner = leaderboard[0]
runner_up = leaderboard[1]

print("Leaderboard:", leaderboard)
print("Winner Points:", winner)
print("Runner-Up Points:", runner_up)
