# print() #funktiokutsu
# print("Hello World") #"Hello" on funktion parametri
# len()



# while True: #Koodiblokki
#     print("I can do this forever.") 

# def greet(name):
#     print(f"Hello {name}!")

# print("Here i am")
# name = "Janne"
# greet(name)

# def greet(name):
#     return f"Hello, {name}"

# print(greet("Janne"))

# def greeting_airport(person, age):
#     print(f"How do you do {person}?")
#     if age >= 18:
#         print("Welcome to your flight!")
#     else:
#         print(f"Your need to wait for {18-age} years to flight solo.")

# greeting_airport(age=26, person="Janne")

#Alkuluku joka on suurempi kuin 1 ja sillä on kaksi positiivista jakajaa
#Esimerkkejä alkuluvuista(prime number): 2, 3, 5, 7, 11, 13, 17, 19, 23…
#Tee ohjelma, joka kysyy käyttäjältä kokonaislukua. Testaa funktionnal onko se alkuluku vai ei. Kysy uutta lukua kunnes käyttäjä pyytää lopettamaan kysymisen.

print("Program starting.")

number = int(input("Insert number: "))

def prime(number):
    for i in range(2, number-1):
        if number % i == 0:
            print("Its not prime")
        else:
            print("Number is prime")

