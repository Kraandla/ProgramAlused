"""
Kontrolltöö 1 (teemad kuni järjend ka.) /
Näidis ülesanne:
JÄRJEND

Koosta järjend loomad OLEMAS

Küsi kasutajalt looma nimesid OLEMAS

Kui seda nime pole järjendis, siis lisa see OLEMAS

Kui järjendis on loom, mis algab sama tähega kui sisestatud nimi lõppes, siis
kirjuta see ekraanile,ja küsi uus loom, kui ei ole, siis küsi kasutajalt uus loom,
mis algab tähega, millega eelmine lõppes.
"""
def animal_list_input(name):
    while True:
        if name not in animals:
            animals.append(name)
            break
        else:
            name = input("This animal already exists. Please give me another animal: ")

def new_animal_list_input(name, last_letter):
    print("NewInputStart")
    while True:
        if name[0].capitalize() != last_letter:
            name = input(f"2Please enter an animal starting with the letter {last_letter}: ").lower().capitalize()
        elif name in animals:
            name = input(f"This animal already exists. Please give me another animal starting with the letter {last_letter}: ").lower().capitalize()
        elif name not in animals:
            animals.append(name)
            break

def new_animal_name_input(name):
    new_name = name
    last_letter = name[-1].capitalize()
    list_check = [animal for animal in animals if animal[0] == last_letter]

    for first_letter in animals:
        if first_letter[0] == last_letter:
            list_check.append(first_letter)

    for first_letter in animals:
        if last_letter == first_letter[0]:
            print(f"Here's an animal starting with the letter that {new_name} "
                  f"ended with: {first_letter}")
            new_name = input("Please give me another animal name: ").lower().capitalize()
            animal_list_input(new_name)

    if len(list_check) == 0:
        new_name = input(f"There is no animal starting with the letter {last_letter}. Please enter an animal starting with the letter {last_letter}: ")
        new_animal_list_input(new_name, last_letter)

def loop_ending_check():
    while True:
        ending_input = input("Do you want to continue?(Y/N): ").lower()
        if ending_input == "y":
            return True
        elif ending_input == "n":
            return False
        else:
            print("Please enter a valid input.")


animals = ["Snake", "Human", "Coconut slug","Albatross"]

while True:
    animal_name_input = input("Please give me an animal name: ").lower().capitalize()
    animal_list_input(animal_name_input)
    new_animal_name_input(animal_name_input)

    print(animals)

    if not loop_ending_check():
        break

