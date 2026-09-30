# Variable set to be used as condition in while loop
more_items = "y"

# Variable to hold the toal value of all items
total = 0

# While loop that collects prices for each item and adds it to the total
while more_items == "y":
    item_price = float(input("Item price: "))
    total += item_price
    more_items = input("Have more items? (y/n): ")

# Prints final total price
print(f"TOTAL: {total}")
