import random

# Creates empty list for random numbers
numbers = []

# For loop that adds 20 random intergers to list between the range 1-100
for x in range(20):
    numbers.append(random.randint(1, 100))

# Prints list of random numbers
print(numbers)

# Initializes a total variable
total = 0

# For loop prints every even number and adds it to total 
for number in numbers:
    if number % 2 == 0:
        total += number
        print(number)

# Prints the total of all even numbers in the list
print(f"The total of all even numbers in the list is: {total}")

# Creates an empty list for second number set
numbers2 = []

# Adds 20 random numbers to list 2
for x in range(20):
    numbers2.append(random.randint(1, 100))

# Prints every number that the lists numbers and numbers2 share
for num in numbers2:
    if num in numbers:
        print(num)