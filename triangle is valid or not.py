
# Input sides of triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check triangle validity
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle is valid")
else:
    print("Triangle is not valid")
