from os import system
from sys import path
path.append('../Python_2/packages')
path.append('../Python_2/packages/extrapack.zip')

import extra.iota
system("cls || clear")
print(extra.iota.funI())

import extra.good.best.sigma as sig
import extra.good.alpha as alp
print(sig.funS())
print(alp.funA())

from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())