
# List of yearly sale data 
sales = [
    [2020, 2.3, 2.2, 1.8, 3.1],
    [2021, 2.4, 2.0, 1.7, 3.0],
    [2022, 1.7, 1.2, 1.0, 1.8],
    [2023, 1.9, 1.0, 0.7, 2.0],
    [2024, 2.0, 2.4, 2.0, 3.2]
]

# A: Calculates the total sales of each year
for row in sales:
    year = row[0]
    total = sum(row[1:])
    print(f"In year {year}, total sales were: {total} ")

# B: Calculates average sales of each year
for row in sales:
    year = row[0]
    average = sum(row[1:]) / 4
    print(f"The average sales in year {year} were: {average}")

# C: Locates min and max sales of all data

max_sales = sales[0][1]
min_sales = sales[0][1]
max_year = sales[0][0]
min_year = sales[0][0]
max_quarter = 1
min_quarter = 1

for row in sales:
    year = row[0]

    for i in range(1, 5):
        if row[i] > max_sales:
            max_sales = row[i]
            max_year = year
            max_quarter = i

        if row[i] < min_sales:
            min_sales = row[i]
            min_year = year
            min_quarter = i
print(f"The maximum sales were: {max_sales} in {max_year} during quarter {max_quarter}")
print(f"The minimum sales were: {min_sales} in {min_year} during quarter {min_quarter}")