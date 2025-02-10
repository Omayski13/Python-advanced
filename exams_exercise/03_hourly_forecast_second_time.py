def forecast(*args):
    result = []
    weather_dict = {"Sunny":[],"Cloudy": [],"Rainy":[]}
    for location, weather in args:
        if weather == "Sunny":
            weather_dict[weather].append(location)
        if weather == "Rainy":
            weather_dict[weather].append(location)
        if weather == "Cloudy":
            weather_dict[weather].append(location)
    for weather,location in weather_dict.items():
        for current_location in sorted(location):
            result.append(f"{current_location} - {weather}\n")
    return "".join(result)



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
