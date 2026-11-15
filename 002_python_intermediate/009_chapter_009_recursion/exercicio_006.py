'''
14.6 Forneça funções recursivas que representem os seguintes conceitos:
a) O produto de dois números naturais.
b) O conjunto de permutações de uma lista de números.
'''


# ----------------------------------------------------------------------
# a) O produto de dois números naturais
# ----------------------------------------------------------------------
def produto(a: int, b: int) -> int:
    """Calcula o produto de dois números naturais (a * b) através de somas recursivas.

    Definição:
      produto(a, 0) = 0
      produto(a, b) = a + produto(a, b - 1)
    """
    if a < 0 or b < 0:
        raise ValueError("Os números devem ser naturais (inteiros >= 0).")
    if b == 0:
        return 0
    return a + produto(a, b - 1)


# ----------------------------------------------------------------------
# b) O conjunto de permutações de uma lista de números
# ----------------------------------------------------------------------
def permutacoes(lista: list[int]) -> list[list[int]]:
    """Gera recursivamente todas as permutações de uma lista de números.

    Caso base:
      Uma lista com 0 ou 1 elemento possui apenas uma permutação: ela mesma.
    Passo recursivo:
      Para cada elemento da lista, fixa-se o elemento e concatena-se com
      todas as permutações dos elementos restantes.
    """
    if len(lista) <= 1:
        return [list(lista)]

    resultado: list[list[int]] = []
    for i, elemento in enumerate(lista):
        # Elementos restantes excluindo o elemento atual
        resto = lista[:i] + lista[i + 1:]
        # Gera permutações do resto e adiciona o elemento atual à frente
        for perm in permutacoes(resto):
            resultado.append([elemento] + perm)

    return resultado


if __name__ == "__main__":
    # Teste do item a: Produto de naturais
    num1, num2 = 4, 3
    print(f"a) Produto de {num1} x {num2} = {produto(num1, num2)}")

    # Teste do item b: Permutações
    numeros = [1, 2, 3]
    resultado_perms = permutacoes(numeros)
    print(f"\nb) Permutações de {numeros} (total: {len(resultado_perms)}):")
    for p in resultado_perms:
        print("  ", p)
