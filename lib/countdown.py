# your code goes here!
import time


def countdown(number: int):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")


def countdown_with_sleep(number: int):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
