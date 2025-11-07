# Create a program that can read a text file and then print the file content. User must be able to specify the file name. Decorate the beginning and the end of the file with a decorative line.
import os

# Määritellään polku tiedostoille
current_dir = os.path.dirname(os.path.abspath(__file__))
sallitut_tiedostot = [
    os.path.join(current_dir, "A6_T1_D1.txt"),
    os.path.join(current_dir, "A6_T1_D2.txt"),
    os.path.join(current_dir, "A6_T1_D3.txt")
]

def read_file(filename):
    # Muokataan käyttäjän antama tiedostonimi sisältämään polku
    full_path = os.path.join(current_dir, filename)
    if filename in [os.path.basename(f) for f in sallitut_tiedostot]:
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                data = f.read()
                return data
        except FileNotFoundError:
            print(f"Tiedostoa ei löytynyt: {full_path}")
        except PermissionError:
            print("Ei oikeuksia tiedoston avaamiseen.")
    else:
        print("Virhe: Tiedoston nimi ei ole sallittu.")

def decorative_lineStart(filename):
    print("#### START " + filename + " ####")

def decorative_lineEnd(filename):
    print("#### END " + filename + " ####")

def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    decorative_lineStart(filename)
    content = read_file(filename)
    print(content)
    decorative_lineEnd(filename)
    print("Program ending.")

if __name__ == "__main__":
    main()