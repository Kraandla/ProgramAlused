def first_exercise():
    """
    1.	Küsi kasutajalt 3 arvu TEHTUD
    2.	Väikseim arv korruta kahega TEHTUD
    3.	Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
    4.	Teata kas kasutaja vastas õigesti või valesti
    5.	Programmi lõpus näita kasutaja valesti vastatud ruutude õiged tulemused (Järjend)
    """
    number_input = []
    number_position_list = ["first", "second", "third"]

    for x in number_position_list:
        while True:
            try:
                number_input.append(int(input(f"Insert the {x} number: ")))
                break
            except ValueError:
                print("Invalid input try again.")

    smallest = int(min(number_input) * 2)

    correct_answers_list = []
    for i in range(3):
        for x in range(1, smallest + 1):
            correct_answers_list.append(number_input[i] ** x)
            answer = input(f"Number {number_input[i]} exponentiation with {x} answer: ")
            while True:
                try:
                    answer = int(answer)
                    break
                except ValueError:
                    answer = "Wrong"
                    break

            if answer == number_input[i] ** x:
                print("Correct answer")
            else:
                print("Wrong answer")
        print("Correct answers: ", correct_answers_list)
        correct_answers_list = []


def second_exercise():
    """
    1.	Küsi kasutaja nime ja vanust
    2.	Kui vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
    3.	Muidu küsi koostatud nime pikkuse jagu arvutus tehteid juhuarvudega (Järjend)
    4.	Kuva tehteid ja lase kasutajal vastata, teata kas said õige tulemuse.
    5.	Programmi lõpus õnnitle kasutajat erineva tekstiga olenevalt programmi käigust
    """
    import random
    name = input("What is your name?: ")
    age = input("What is your age?: ")
    while True:
        try:
            age = int(age)
            break
        except ValueError:
            age = input("Please input a valid age: ")
    if age < 5:
        for x in range(3):
            print(f"Hello {name}")

    correct_answers = []
    correct_answer_count = 0

    for p in range(len(name)):
        operator = random.randint(0,3)
        operators = ["+","-","*","/"]
        first_number = float(random.randint(1,20))
        second_number = float(random.randint(1, 20))

        answer = input(f"{first_number} {operators[operator]} {second_number} = ")
        while True:
            try:
                answer = float(answer)
                break
            except ValueError:
                answer = 0
                break

        match operator:
            case 0:
                correct_answers.append(first_number + second_number)
            case 1:
                correct_answers.append(first_number - second_number)
            case 2:
                correct_answers.append(first_number * second_number)
            case 3:
                correct_answers.append(round(first_number / second_number,2))
        if answer == correct_answers[p]:
            print("Right answer!")
            correct_answer_count += 1
        else:
            print("Wrong answer!")

    if correct_answer_count > len(correct_answers) / 2:
        print(f"Congratulations you got {correct_answer_count} questions correct!")
    else:
        print(f"Unfortunately you got {correct_answer_count} answers correct.")


def third_exercise():
    """
    1.	Küsi kasutaja vanust ja nime
    2.	Õnnitle kasutajat iga täisealisena veedetud aasta eest (Kordus)
    3.	Iga õnnitluse järel küsi ja salvest antud aasta meeleolu (Järjend)
    4.	Programmi lõpus kuva meeleolud nende pikkuse järjekorras
    """
    name = input("Name: ")
    age = input("Age: ")
    mood = []
    while True:
        try:
            age = int(age)
            break
        except ValueError:
            age = input("Valid age: ")
    for x in range(age):
        print(f"Congratulations {name} for living through your {x + 1} age!")
        mood.append(input("What was your mood at that age?: "))
    mood.sort(key=len)
    print("Your moods throughout the years: ", mood)


def fourth_exercise():
    """
    1.	Küsi kasutaja sugu ja vanus yes
    2.	Kasuta eale vastavaid tervitusi nii mehele kui ka naisele. yes
    3.	Korda tervitust vanuse suurendamisega kuni tervitus vahetub või 10 korda. yes
    4.	Salvesta järjendisse iga kolmas tervitus ja viimane yes
    5.	Kuva ekraanile järjendis olevate tervituste eelviimased sõnad
    """
    import random
    gender = input("Gender(M/F): ").lower()
    while True:
        if gender == "m" or gender == "f":
            break
        else:
            gender = input("Input valid gender(M/F):").lower()

    age = input("Age: ")
    greetings = ["Hello pre teen!","Hello tea ager", "Hello young adult!","Hello middle ager!","Hello mac oldie!"]
    greetings_2 = ["Hello dust ball", "Hello immortal monarch", "Hello alzheimers patient", "Hello pool party"]
    saved_greetings = []

    list_position = 0
    which_list = 0
    while True:
        try:
            age = int(age)
            break
        except ValueError:
            age = input("Valid age: ")

    for x in range(1, age + 1):
        random_list_number = random.randint(0, 3)
        if x % 50 == 0:
            which_list = 1
        elif x % 10 == 0:
            list_position += 1

        if which_list == 0:
            greeting = greetings[list_position]
            split = greeting.split()
            print(greeting)
            if x % 3 == 0 or x == age:
                saved_greetings.append(split[-2])
        else:
            greeting = greetings_2[random_list_number]
            split = greeting.split()
            print(greeting)
            if x % 3 == 0 or x == age:
                saved_greetings.append(split[-2])
    print(saved_greetings)


def fifth_exercise():
    """
    1.	Küsi kasutajalt lause
    2.	Kui lauses on vähem kui 5 sõna, jäta lause meelde ja küsi uus lause (Kordus, Järjend)
    3.	Kuva pikas lauses (5 või rohkem sõna) olevad sõnad eraldi real
    """
    sentence = input("Sentence: ")
    split = sentence.split()
    array = []
    while True:
        if len(split) < 5:
            array.append(sentence)
            sentence = input("New sentence:")
        else:
            for x in split:
                word = x
                word = word.replace(',','')
                word = word.replace('.','')
                print(word)
            break


def sixth_exercise():
    """
    1.	Kasutajalt küsitakse sõna. done
    2.	Kasutajalt küsitakse numbrit. done
    3.	Loo järjend, kus antud sõna on korrutatud kasvavalt kuni antud numbrini (kordus, järjend).
    4.	Juhul kui sisestatud number on suurem kui 10, tagastatakse „Viga“.
    5.	Kuva järjendi viimane väärtus
    """
    word = input("Input a word: ")
    while True:
        number_check = any(char.isdigit() for char in word)
        if number_check:
            word = input("Please do not include numbers in your word: ")
        elif len(word.split()) > 1:
            word = input("Enter only 1 word: ")
        else:
            break

    number = input("Insert a number: ")
    while True:
        try:
            number = int(number)
            if number > 10:
                print("Error")
                return
            else:
                break
        except ValueError:
            number = input("Please enter a valid number: ")

    word_repeat_list = []
    for x in range(number):
        word_repeat = ""
        for i in range(x + 1):
            word_repeat += word
        word_repeat_list.append(word_repeat)
    print(word_repeat_list[-1])


def seventh_exercise():
    """
    1.	Küsi kasutajalt 1 arv mille paned astmele 2, 3 ,4 ja 5 kasutades kordust ja järjendit
    2.	Lase kasutajal arvata, millises astmes on suvaline arv järjendis
    3.	Teata kas arvati õigesti ja kuva õige vastus
    4.	Peale seda küsi kasutajalt kas ta soovib teise arvuga programmi korrata või lõpetada. (Kordus)
    """
    import random
    number = input("Please insert a number: ")
    while True:
        try:
            number = int(number)
            break
        except ValueError:
            number = input("Please enter a valid number: ")

    number_exponents_array = []
    while True:
        array_position = random.randint(0,3)
        for x in range(1, 5):
            calculation = number ** (x + 1)
            number_exponents_array.append(calculation)
        guess = input("Guess the answer of your numbers exponent(2 to 5): ")
        try:
            guess = int(guess)
        except ValueError:
            guess = 0
        if guess == number_exponents_array[array_position]:
            print("Correct guess!")
        else:
            print(f"Wrong guess. The correct guess was {number_exponents_array[array_position]}, which is the {array_position + 2} exponent of {number}")

        while True:
            user_input = input("Do you want to continue(Y/N)?: ").lower()
            print(user_input)
            if user_input == "y":
                user_input = input("Do you want to continue with the same number(Y/N)?: ").lower()
                if user_input == "y":
                    break
                elif user_input == "n":
                    number = input("Please insert a number: ")
                    while True:
                        try:
                            number = int(number)
                            break
                        except ValueError:
                            number = input("Please enter a valid number: ")
                    print(number)
                    break
                else:
                    print("Please enter a valid input.")
            elif user_input == "n":
                return False
            else:
                print("Please enter a valid input.")

def eighth_exercise():
    """
    1.	Küsi kasutajalt arvu.
    2.	Kui arv on positiivne, ütle kasutajale, et ta prooviks pigem negatiivset arvu sisestada.
    3.	Kui arv on negatiivne, ütle kasutajale, et ta prooviks pigem positiivset arvu sisestada.
    4.	Kui arv on 0, õnnitlege kasutajat ja öelge, et olete mängule ära teinud ja pääsete igavesest kordusest.
    5.	Kuva ekraanile kasutaja sisestatud arvud kahanevas järjekorras (Järjend)
    """
    number_array = []
    while True:
        number = input("Give me a number: ")
        while True:
            try:
                number = float(number)
                break
            except ValueError:
                number = input("Give me a correct number")
        if number > 0:
            print("Could you insert a negative number instead?")
            number_array.append(number)
        elif number < 0:
            print("Could you insert a positive number instead?")
            number_array.append(number)
        elif number == 0:
            print("Congratulations on breaking out of this prison with your usage of 0!")
            break
        else:
            print("That wasn't correct. Please try again.")
    number_array.sort(reverse = True)
    print("Here are your numbers: ", number_array)

if __name__ == '__main__':
    first_exercise()
    second_exercise()
    third_exercise()
    fourth_exercise()
    fifth_exercise()
    sixth_exercise()
    seventh_exercise()
    eighth_exercise()