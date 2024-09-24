FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Function takes a temperature in Fahrenheit and returns the temperature converted to Celsius"""
    Temp_in_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return print(f'{fahrenheit}°F is {Temp_in_celsius}°C')
    
def convert_to_fahrenheit(celsius):
    """Function takes a temperature in Celsius and returns the temperature converted to Fahrenheit"""
    Temp_in_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return print(f'{celsius}°C is {Temp_in_fahrenheit}°F') 

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
if unit == "c":
    convert_to_fahrenheit(temperature)
elif unit == 'f':
    convert_to_celsius(temperature)
else:
    print("Incorrect Temperature unit")
