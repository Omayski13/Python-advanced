def forecast (*args):

    sunny = []
    cloudy =[]
    rainy =[]
    result = []

    for city,weather in args:
        if weather == "Sunny":
            sunny.append(city)
        if weather == "Cloudy":
            cloudy.append(city)
        if weather == "Rainy":
            rainy.append(city)

    sorted_sunny = sorted(sunny)
    sorted_cloudy = sorted(cloudy)
    sorted_rainy = sorted(rainy)

    for city in sorted_sunny:
        result.append(f"{city} - Sunny\n")
    for city in sorted_cloudy:
        result.append(f"{city} - Cloudy\n")
    for city in sorted_rainy:
        result.append(f"{city} - Rainy\n")

    return "".join(result)

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))



