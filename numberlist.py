# Asks user for num a 
a = int(input("Number A: "))

# Asks user for num b
b = int(input("Number B: "))

# For loop prints every number from A to B unless a > b
if a < b:
    for x in range(a, b + 1):
        print(x, end=" ")
else:
    print("Error, A must be less than B")