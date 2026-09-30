# This function perfoms a conversion from Celcius to Farenhite and vice versa
def conversion(initial_unit, given_temp):
    if unit == 'f':
        return (temperature - 32) / 1.8
    else:
        return (temperature * 9/5) + 32

# User inputs inital temperature unit and degrees
unit = input("Choose a unit, 'f' for Fahrenheit or 'c' for Celcius: ")
temperature = float(input("Input the temperature: "))

# Calls the conversion function and prints the results
print(f"The converted temperature is {conversion(unit, temperature)} degrees.")