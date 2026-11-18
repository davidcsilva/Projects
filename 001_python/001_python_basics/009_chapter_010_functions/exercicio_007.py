'''
Defina uma função recursiva que calcule o maior divisor comum
(M.D.C.) entre dois números a e b, onde a > b.
mdc(a, b) = 

a b= 0
mdc(b, a − b a
b) a > b
Onde
a − b a
b pode ser escrito em Python como: a % b.

'''


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

print(mdc(4, 2))
