from os import system
from time import sleep
def find_word(objective_str,main_str):
    index_list = []
    objective_str = objective_str.lower()
    main_str = main_str.lower()

    fnd_first = main_str.find(objective_str[0])
    if fnd_first != -1:
        index_list.append(fnd_first)
        for j in range(1,len(objective_str)):
            letter_position = main_str.find(objective_str[j],fnd_first)
            if letter_position != -1:
                fnd_first = letter_position
                index_list.append(letter_position)
        if len(index_list) == len(objective_str):
            print("Sí")
            #print(index_list)
        else:
            print("No")
            #print(index_list)
    else:
        print("No")
        #print(index_list)
if __name__ == "__main__":
    system("cls || clear")
    # find_word("dog","vcxzxduybfdsobywuefgas")
    # find_word("dog","vcxzxdcybfdstbywuefsas")
    try:
        while True:
            find_word(input("Input string to search for (and press Ctrl + C to stop): "),input("Input strig where to search: "))
            sleep(3)
            system("cls || clear")
    except KeyboardInterrupt:

        print("\n\nFinished by user\n")

        #find_word("donor","Nabucodonosor")