'''
14.9 O elemento maior de um array inteiro de n elementos pode ser calculado recursivamente. Defina a função:
inteiro função Máx (E inteiro: x, y)
que devolva o maior de dois inteiros x e y. Definir a função
inteiro função máxarray (E arr: a, E inteiro: n)
que utiliza recursão para devolver o elemento maior de a

Condição de parada:
n == 1

incremento recursivo:
máxarray = Máx(máx (a[0] ... a [n–2]), a[n–1])
'''


def maximo(x: int, y: int) -> int:
    """Devolve o maior entre dois números inteiros x e y."""
    return x if x > y else y


def maxarray(a: list[int], n: int | None = None) -> int:
    """Utiliza recursão para devolver o maior elemento de uma lista/array 'a' de tamanho 'n'.

    Condição de parada:
        n == 1 -> retorna a[0]
    Passo recursivo:
        maxarray = maximo(maxarray(a, n - 1), a[n - 1])
    """
    if n is None:
        n = len(a)

    if n <= 0:
        raise ValueError("O tamanho do array deve ser maior ou igual a 1.")

    # Condição de parada (caso base):
    if n == 1:
        return a[0]

    # Passo recursivo:
    return maximo(maxarray(a, n - 1), a[n - 1])


if __name__ == "__main__":
    lista = [12, 45, 7, 89, 23, 56, 3]
    maior_elemento = maxarray(lista)

    print(f"Array: {lista}")
    print(f"Maior elemento encontrado: {maior_elemento}")

    # Teste com elementos negativos
    lista_negativos = [-15, -3, -42, -8, -1]
    print(f"\nArray negativo: {lista_negativos}")
    print(f"Maior elemento encontrado: {maxarray(lista_negativos)}")
