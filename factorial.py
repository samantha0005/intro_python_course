# Takes n as an input and finds its factorial
def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result

# Takes user input for variable n
n = int(input("Enter a number: "))

# Calls factorial function and prints the result 
print(f"The factorial of {n} is {factorial(n)}.")