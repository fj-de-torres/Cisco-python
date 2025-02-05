from sys import path
#path.append('../Python_2/modules')
path.insert(0,'../Python_2/modules')
from module import suml, prodl
from os import system

if __name__ == "__main__":
    system("cls || clear")
    #print(module.__counter)
    zeroes = [0 for i in range(5)]
    ones = [1 for i in range(5)]

    print(suml(zeroes))
    print(prodl(ones))

    for p in path:
        print(p)