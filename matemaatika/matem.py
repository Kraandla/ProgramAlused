"""Python kontrolltöö"""

"""
1.	Küsi kasutaja sugu ja vanus
2.	Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
3.	Korda tervitust vanuse suurendamisega kuni tervitus vahetub või 10 korda.
4.	Salvesta järjendisse iga kolmas tervitus ja viimane
5.	Kuva ekraanile järjendis olevate tervituste eelviimased sõnad
"""

def user_greeting():
    """Funktsioon tervitab kastajat vastavalt tema vanusele ja sugule kuni tervitus vahetub või 10 korda.
    iga kolmas ja viimane tervitus salvestatakse ning programm kuvab ekraanile järjendis olevate tervituste eelviimased sõnad"""

    user_gender = str(input("Hello user, what is your gender? Answer 'm' for male or 'f' for female? "))
    user_age = int(input("Now tell me, how old you are? "))

    age_limit1 = range(1, 18)
    age_limit2 = range(18, 30)
    age_limit3 = range(30, 50)
    age_limit4 = range(50, 100)

    title = ""
    age_gap = None

    if user_gender == "m":
        if user_age in age_limit1:
            title = "young man"
            age_gap = age_limit1
        elif user_age in age_limit2:
            title = "Mr"
            age_gap = age_limit2
        elif user_age in age_limit3:
            title = "sir"
            age_gap = age_limit3
        elif user_age in age_limit4:
            title = "gentelman"
            age_gap = age_limit4

    elif user_gender == "f":
        if user_age in age_limit1:
            title = "young lady"
            age_gap = age_limit1
        elif user_age in age_limit2:
            title = "Miss"
            age_gap = age_limit2
        elif user_age in age_limit3:
            title = "madam"
            age_gap = age_limit3
        elif user_age in age_limit4:
            title = "ma'am"
            age_gap = age_limit4

    else:
        print("Invalid input")

    greeting = f"Good day to you, {title}!"

    counter = user_age
    iteration_counter = 0
    list_of_greetings = []
    last_iteration = 0

    if (len(age_gap)-1) - user_age > 10:
        last_iteration = 10
    else:
        last_iteration = (len(age_gap)+1) - user_age

    while counter in age_gap and iteration_counter < 10:
        output_greeting = (f"{iteration_counter + 1}. {greeting}")
        print(output_greeting)
        counter += 1
        iteration_counter += 1

        if iteration_counter % 3 == 0 or iteration_counter == last_iteration:
            list_of_greetings.append(output_greeting)
            print(f"this is third greeting")


    print(list_of_greetings)
    print(last_iteration)
    for item in list_of_greetings:
        find


if __name__ == "__main__":
    user_greeting()