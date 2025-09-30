print("Welcome to the temp app!")
Temp = int(input("What is the temperature of the CPU? "))
if(Temp > 80):
    print("Warning! Temperature too high!")
else:
    print("All cool, keep going!")

#Make a program, which tests if the user input number even or uneven

number = int(input("Insert number "))
if number % 2==0:
    print("Number is even.")
else:
    print("Number is odd.")

if(Temp > 80):
    if(Temp > 90):
        print("Your are TOAST!")
    else:
        print("Warning!")
else:
    print("You are okay.")

    if(Temp > 90):
        print("You are TOAST!")
    elif(Temp > 80):
        print("Warning!")
    else:
        print("You are okay!")

#tee ohjelma joka kysyy kahta nimeä. testaa, kumpi nimistä on pidempi, vai onko samanpituisia. Vinkki len()

print("Program starting")
name1 = input("Insert first name: ")
name2 = input("Insert second name: ")
if len(name1) > len(name2):
    print("First name is longer.")
elif len(name1) < len(name2):
    print("Second name is longer.")
else:
    print("Both are same lenght!")

Town = "Lahti"
Street = "Mukkulankatu"
Building = 19

if(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print("You are at LAB")
elif(Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):
    print("You are in the correct town, but check the street address again")
elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print("You are completely lost...")

import random
print(random. randint(1, 6))

# Tee KPS peli käyttämällä random metodia.

import random

choices = ["kivi", "paperi", "sakset"]
computer_choice = random.choice(choices)
player_choice = input("Valitse kivi, paperi tai sakset: ").lower()

print(f"Pelaaja valitsi: {player_choice}")
print(f"Tietokome valitsi: {computer_choice}")

if player_choice == computer_choice:
    print("Tasapeli!")
elif(player_choice == "kivi" and computer_choice == "sakset") or \
    (player_choice == "sakset" and computer_choice == "paperi") or \
    (player_choice == "paperi" and computer_choice == "kivi"):
    print("Pelaaja voittaa!")
else:
    print("Tietokone voittaa!")