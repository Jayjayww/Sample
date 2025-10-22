def askName() -> str:
    Name = input("Insert name: ")
    return Name

def greetUser(PName)-> None:
    print(f"Hello {PName} !")
    return None

def main() -> None:
    print("Program starting.")
    Name = askName()
    greetUser(Name)
    print("Program ending.")
    return None

main()