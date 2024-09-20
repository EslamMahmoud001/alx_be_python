# This script will ask the user about the current weather conditions and provide clothing recommendations based on the input

Weather = input("What's the weather like today? sunny/rainy/cold: ").lower()

if Weather == "sunny":
    text = f'Wear a t-shirt and sunglasses.'
elif Weather == "rainy":
    text = f"Don't forget your umbrella and a raincoat."
elif Weather == "cold":
    text = f'Make sure to wear a warm coat and a scarf.'
else: 
    text = "Sorry, I don't have recommendations for this weather."
    
print(text)
