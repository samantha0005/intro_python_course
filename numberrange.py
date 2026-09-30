# Asks user for a number
chosen_num = int(input("Give a number: "))

# Prints every even number from 2 to the user's chosen_num
for x in range(2, chosen_num + 1, 2):
    print(x, end=" ")
