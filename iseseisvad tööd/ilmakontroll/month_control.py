def month_control() -> str:
    #Küsib ja kontrollib kasutaja poolt sisestatud kuud.
    months_array: list[str] = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

    month = input("Palun sisesta  kuu:").lower()
    i = 0

    while i == 0:
        if month in months_array:
            # print(f"Kuu kontroll: {month}")
            i = 1
        else:
            month = input("Palun sisesta korrektne kuu:").lower()

    return month.capitalize()