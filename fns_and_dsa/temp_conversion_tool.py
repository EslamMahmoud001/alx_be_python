FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Function takes a temperature in Fahrenheit and returns the temperature converted to Celsius"""
    Temp_in_celsius = (float(fahrenheit)- 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return print(f'{float(fahrenheit)}°F is {Temp_in_celsius}°C')
    
def convert_to_fahrenheit(celsius):
    """Function takes a temperature in Celsius and returns the temperature converted to Fahrenheit"""
    Temp_in_fahrenheit = (float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return print(f'{float(celsius)}°C is {Temp_in_fahrenheit}°F') 

temp_correct = False
while not temp_correct:
    temperature = input("Enter the temperature to convert: ")
    if temperature.isdigit():
        temp_correct = True
    else:
        print("Invalid temperature. Please enter a numeric value.")
        
unit_correct = False
while not unit_correct:
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if unit == "c":
        convert_to_fahrenheit(temperature)
        unit_correct = True
    elif unit == 'f':
        convert_to_celsius(temperature)
        unit_correct = True
    else:
        print("Invalid Temperature unit")
        
