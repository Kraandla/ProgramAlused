def weather_control() -> str:
    weather = input("Kas ilm on päikseline, pilvine või vihmane?: ").lower()

    weather_array: list[str] = ["päikseline", "pilvine", "vihmane"]

    i = 0

    while i == 0:
        if weather in weather_array:
            i = 1
        else:
            print("Palun sisesta korrektne vastus")
            weather = input("Kas ilm on päikseline, pilvine või vihmane?: ").lower()

    return weather