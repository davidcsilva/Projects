'''
14.13 Um palíndromo é uma palavra que é lida exatamente igual da esquerda para a direita e vice-
versa. Tais palavras como ovo, ala etc. são exemplos de palíndromos. Escreva uma função
recursiva que devolva um valor de 1 (verdadeiro) se uma palavra passada como argumento é
um palíndromo e devolve 0 (falso) caso contrário.
'''


def eh_palindromo(palavra: str) -> int:
    """Verifica recursivamente se uma palavra é um palíndromo.

    Retorna:
        1: se for palíndromo (verdadeiro)
        0: caso contrário (falso)
    """
    # Caso base: palavras vazias ou com apenas 1 caractere são palíndromos
    if len(palavra) <= 1:
        return 1

    # Compara o primeiro e o último caractere (desconsiderando maiúsculas/minúsculas)
    if palavra[0].lower() != palavra[-1].lower():
        return 0

    # Chamada recursiva: analisa a substring sem o primeiro e o último caractere
    return eh_palindromo(palavra[1:-1])


if __name__ == "__main__":
    exemplos = [
        "ovo",
        "ala",
        "radar",
        "arara",
        "osso",
        "reviver",
        "python",
        "recursao",
        "computador",
        "A",
        "",
    ]

    print("=== Teste de Palíndromos Recursivo ===")
    for termo in exemplos:
        resultado = eh_palindromo(termo)
        status = "Palíndromo (1)" if resultado == 1 else "Não é palíndromo (0)"
        print(f"'{termo}': {resultado} -> {status}")
