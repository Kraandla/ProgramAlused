"""
1.	Küsi kasutaja vanust ja nime
2.	Õnnitle kasutajat iga täisealisena veedetud aasta eest (Kordus)
3.	Iga õnnitluse järel küsi ja salvest antud aasta meeleolu (Järjend)
4.	Programmi lõpus kuva meeleolud nende pikkuse järjekorras

"""


def ask_name():
    """Asks name and returns it."""
    name = input("Palun sisesta nimi: ")
    return name


def ask_age():
    """Asks the user how old they are and returns the age as an integer if a valid input was inserted."""
    age = input("Kui vana oled sa?: ")
    while True:
        try:
            age = int(age)
            return age
        except ValueError:
            age = input("Palun sisesta korrektne vanus: ")


def adult_age_congratulations(age, name):
    """
    Takes age and name and congratulates the user if their age is above 18.

    """
    adult_age = 18

    for i in range(1, age + 1):
        if i > adult_age:
            print(f"Palju õnne {i} veedetud aasta eest {name}!")
            mood = input("Kuidas sa tunned ennast?: ")
            mood_array.append(mood)


def age_check(age, name):
    if age == 18:
        print(f"Just said täisealiseks {name}, mida sul tähistada on?")
        return False
    elif age < 18:
        print(f"Kahjuks oled liiga noor õnnitluseks {name}. Kasva suureks!")
        return False
    else:
        return True


if __name__ == '__main__':
    user_name = ask_name()
    user_age = ask_age()

    mood_array = []
    age_more_than_18 = age_check(user_age, user_name)

    if age_more_than_18:
        adult_age_congratulations(user_age, user_name)
        print("Siin on sinu meeleolud: ", sorted(mood_array, key=len))
