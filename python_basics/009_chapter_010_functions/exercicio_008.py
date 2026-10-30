'''
Usando a função mdc definida no exercício anterior, defina uma
função para calcular o menor múltiplo comum (M.M.C.) entre dois números.
mmc(a, b) =  |a × b|
mdc(a, b)
Onde |a × b| pode ser escrito em Python como: abs(a*b).

'''


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

print(mdc(4, 2))
print(mmc(4, 2))
