# tehtävä:
# Jos käyttäjätunnus = omaNimi ja ikä >= 18 ja käyttäjä admin => avataan admin-sivu
# Jos käyttäjätunnus = omaNimi ja ikä >= 18 => avataan käyttäjäsivu
# Jos ikä < 18 => kerrotaan käyttäjälle: Ikä ei riitä
# Jos käyttäjätunnus != omaNimi => Pääsy kielletty

# Admin tunnuksilla valikko: 1. lisää uusi käyttäjä 2. tarkista laitteen toiminta 3. exit
# Käyttäjäsivulla valikko 1. Tarkista omat tiedot 2. exit

# print("Program starting")
# omaNimi = input("Oma nimi: ")
# omaIkä = int(input("Oma ikä: "))
# admin_nimi = "Janne Juntumaa"
# admin_ikä = 26

# if omaNimi == admin_nimi and omaIkä == admin_ikä:
#     print("\nAdmin-sivu:")
#     print("1 - Lisää uusi käyttäjä")
#     print("2 - Tarkista laitteen toiminta")
#     print("3 - Exit")
#     valinta = input("Valinta: ")

# elif omaNimi == admin_nimi and omaIkä >= 18:
#     print("\nKäyttäjäsivu:")
#     print("1 - Tarkista omat tiedot")
#     print("2 - Exit")
#     valinta = input("Valinta: ")

# elif omaIkä < 18:
#     print("Ikä ei riitä.")
# else:
#     print("Pääsy kielletty.")

#<-------------------------->

Children = 3
Hometown = "Lappeenranta"

#Lista
TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Jyväskylä", "Oulu"]

RandomInformation = ("Janne", 26, True, Children, Hometown)
print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NumOfTowns = len(TownsInFinland)
print(TownsInFinland[NumOfTowns-1])

Municipalities = ["Asikkala", "Hollola", "Lemi"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Jyväskylä", "Oulu"]

MunicipalitiesAndTowns = [Municipalities, Towns]

print(MunicipalitiesAndTowns [1][-2])

Towns.sort()
print(Towns)

Teacher = {
    'name': 'Juha',
    'age': 50,
    'city': 'Lahti'
}

print(Teacher["name"])

Teacher['email']= 'juha.hyytainen@lab.fi'

print(Teacher)

for key in Teacher:
    print(key, end=" ")
    print(Teacher[key])

Student = [
    {"name": "Mikko", "age": 25, "city": "Lahti"},
    {"name": "Janne", "age": 26, "city": "Lappeenranta"},
    {"name": "Maija", "age": 30, "city": "Oulu"}
]

print(Student[0])

Cities = {
    "Finland":["Tampere", "Espoo", "Lappeenranta", "Helsinki"],
    "Sweden":["Stockholm", "Malmö"]
}

print(Cities["Finland"][2])

#Towns = ["Lahti", "Helsinki", "Lappeenranta", "Jyväskylä", "Oulu"]

for town in Towns:
    print(f"The town of {town}")
print(f"All of the towns {Towns}")

for i in range(1,10):
    print(i)

for i in range(1,10):
    print(i, end=" ")

print(" ")
for i in range(1,10, 3):
    print(i)

Total = 0
for i in range(1,101):
    Total +=i
    print(Total)

print(Total)

for i in range(9):
    if i == 3:
        continue
    print(i)

#Opiskele loopit for ja while, sekä niihin liittyvät komennot continue ja break

# while 1 < 10:
#     print("Do not try me at home xD")

i = 0
while i < 10:
    print(f"Iteration number: {i}")
    i += 1

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False

while True:
    if input("Do you want to continue? ") != "yes":
        break
    else:
        continue