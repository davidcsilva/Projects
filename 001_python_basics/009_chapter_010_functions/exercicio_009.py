'''
Rastreie o programa da listagem 8.12 e compare o resultado com o
apresentado na listagem 8.13.

'''


def fatorial(n):
    print(f"Fatorial de {n}")
    if n == 1 or n == 0:
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f" de {n} = {fat}")
        return fat

fatorial(4)
