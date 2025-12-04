from A8_T1Lib import activationPause

def askUser() -> str:
    return input("Your choice: ")

def showOptions() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activation pause")
    print("0 - Exit")
    
    return None

def chooseActivity() -> None:
    duration = 0
    while True:
        showOptions()
        choice = int(askUser())
        match choice:
            case 1:
                duration = int(input("Insert pause duration (s): "))
            case 2:
                activationPause(duration)
            case 0:
                print("Exiting program.")
                break    
    return None

def main() -> None:
    print("Program starting.")
    chooseActivity()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()