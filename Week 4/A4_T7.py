# Pyydä arvo ja muuta se integeriksi
# Alusta muuttuja, joka laskee kierroksia
# Tee while loop, joka looppaa niin kauan kuin se ar ei ole 0
#     Testaa, onko arvo pienmpi kuin 10 > break
#     Muuta arvo inteheriksi, jotta saamme yksittäiset numerot esille
#     Tee for loop, joka käy läpi jokaisen luvun
#         Testaa onko numero viimeinen
#         tee laskutoimitus integereillä
#     Printtaa kertolaskun tulos
#     Muuta arvoksi edellisen kierroksen kertolaskun tulos
#     Jos arvo on nolla, printtaa no more steps
#     Lisää kierrokslaskuriin +1

# Printtaa kierokset

# Create program which prompts the user to insert an integer and then display the steps to calculate the multiplicative persistency based on the user input.

# In short, the steps in the multiplicative persistency is calculated by multiplying digits together in a given integer. This process is then repeated for the result which makes the result value smaller on each iteration till the result contains only one digit.

# The program must stop the iteration when the result contains only one digit. Finally before the program closes, it shows the steps taken.

# Example program runs

print("Program starting.")
print("\nCheck multiplicative persistence.")
n = int(input("Insert an integer: "))

steps = 0

while True:
    digits = [int(d) for d in str(n)]
    if len(digits) == 1:
        break

    print(" * ".join(str(d) for d in digits), end=" = ")
    product = 1
    for d in digits:
        product *= d
    print(product)
    n = product
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")