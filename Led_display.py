
digits= {1 : ["  #","  #","  #","  #","  #"],
2 : ["###","  #","###","#  ","###"],
3 : ["###","  #","###","  #","###"],
4 : ["# #","# #","###","  #","  #"],
5 : ["###","#  ","###","  #","###"],
6 : ["###","#  ","###","# #","###"],
7 : ["###","  #","  #","  #","  #"],
8 : ["###","# #","###","# #","###"],
9 : ["###","# #","###","  #","###"],
0 : ["###","# #","# #","# #","###"]}

def print_number(string_number):
    if string_number.isdigit() == False:
        print("Ingresa un número válido")
        return
    else:
        for i in range(5):
            for j in string_number:
                print(digits[int(j)][i],end=" ")
            print()
print_number(input("Ingresa el número que deseas mostrar: "))


