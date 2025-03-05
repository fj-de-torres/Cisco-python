import sys
from os import system
from time import sleep
def secure_int():
    correct = True
    while correct:
        try:
            min = int(input("Enter minimum value: "))
            max = int(input("Enter máximum value: "))
            integer = int(input("Now enter value: "))
            if integer < min or integer > max:
                raise OverflowError
            print(f"Your number is :{integer}")
            correct = False
        except ValueError:
            print("Please ensure that you enter digits only. Please try again.")
        except OverflowError:
            print("Error: Your number is out of range. Please try again.")
        except KeyboardInterrupt:
            print("\nYou have chosen to terminate this program")
            
            for i in range(3,-1,-1):
                sleep(1)
                sys.stdout.write(f"\rExiting in... {i}")
                sys.stdout.flush
            print()
            break
if __name__ == "__main__":
    system("cls || clear")
    secure_int()