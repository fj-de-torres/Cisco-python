from os import system
def check_anagrama(input_string_1, input_string_2):
    working_string_1 = input_string_1.lower().replace(' ','')
    working_string_2 = input_string_2.lower().replace(' ','')
    if len(working_string_1.strip(working_string_2)) == 0:
        print("Son anagramas")
    else:
        print("NO son anagramas")
if __name__ == "__main__":
    system("cls || clear")
    check_anagrama("Listen","Silent")
    check_anagrama("Idiot","Toyota")