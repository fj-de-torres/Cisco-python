from os import system

def get_life_digit(string):
    # Clean the input string
    string = string.strip().strip("-").strip("/")
    
    # Validate input
    if not string.isdigit():
        print("Only numbers, please")
        return None
    
    # Base case: if single digit, return it
    if len(string) == 1:
        return int(string)
    
    # Calculate sum of digits
    suma = sum(int(digit) for digit in string)
    
    # Recursive call with the new sum
    return get_life_digit(str(suma))

if __name__ == "__main__":
    system("cls || clear")
    result = get_life_digit(input("Please enter a date to calculate the life digit: "))
    if result is not None:
        print("Life number is:", result)
