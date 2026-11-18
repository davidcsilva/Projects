'''
Reescreva o programa da listagem 8.8 de forma a utilizar for em vez
de while.
'''




def fatorial(n):
    fat = 1
    for x in range(1, n + 1):
        fat *= x
    return fat

print(fatorial(3))
