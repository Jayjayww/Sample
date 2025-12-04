from time import sleep

def activationPause(duration):
    print(f"Pausing for {duration} seconds")
    sleep(duration)
    print("Unpaused")