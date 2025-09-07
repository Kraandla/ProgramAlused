def day_control() -> str:
    """Asks the current day and checks if the day is valid"""
    #Asks the user the current day and converts the input into an integer
    day = int(input("Palun sisesta  kuupäev:"))

    #defines the variable as 0 to keep the while loop running indefinetaly
    i = 0

    while i == 0:
        if day < 32:
            i = 1
        else:
            day = int(input("Palun sisestage korrektne kuupäev:"))

    return str(day)