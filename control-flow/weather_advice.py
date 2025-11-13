"""weather_advice program is created to provide clothing recommendations for users based on specific user inputs.
 Input examples: rainy, sunny etc."""
 
weather_today = input("What's the weather like today? (sunny/rainy/cold): ")

if weather_today == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_today == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_today == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
    
