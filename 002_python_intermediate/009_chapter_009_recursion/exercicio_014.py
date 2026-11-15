'''
14.14 Escreva uma função recursiva que liste todos os subconjuntos de duas letras para um conjunto
dado de letras:
[A, C, E, K] → [A, C], [A, E], [A, K], [C, E], [C, K], [E, K]
'''


def subconjuntos_de_dois(letras: list[str]) -> list[list[str]]:
    """Gera recursivamente todos os subconjuntos de 2 elementos de uma lista de letras.

    Lógica recursiva:
    1. Caso base: se a lista tiver menos de 2 elementos, não é possível formar pares (retorna []).
    2. Passo recursivo:
       - Fixa o primeiro elemento e combina-o com cada um dos elementos restantes.
       - Chama a função recursivamente para encontrar todos os pares no restante da lista (sem o primeiro).
       - Concatena as duas partes.
    """
    if len(letras) < 2:
        return []

    primeiro = letras[0]
    restante = letras[1:]

    # Pares contendo o primeiro elemento com os demais
    pares_com_primeiro = [[primeiro, outro] for outro in restante]

    # Chamada recursiva para os pares que não contêm o primeiro elemento
    pares_sem_primeiro = subconjuntos_de_dois(restante)

    return pares_com_primeiro + pares_sem_primeiro


def subconjuntos_k(conjunto: list[str], k: int = 2) -> list[list[str]]:
    """Versão generalizada para subconjuntos de qualquer tamanho k."""
    if k == 0:
        return [[]]
    if len(conjunto) < k:
        return []

    primeiro = conjunto[0]
    restante = conjunto[1:]

    # Subconjuntos que incluem o primeiro elemento (buscam k - 1 elementos no restante)
    com_primeiro = [[primeiro] +
                    sub for sub in subconjuntos_k(restante, k - 1)]

    # Subconjuntos que não incluem o primeiro elemento (buscam k elementos no restante)
    sem_primeiro = subconjuntos_k(restante, k)

    return com_primeiro + sem_primeiro


if __name__ == "__main__":
    letras = ["A", "C", "E", "K"]
    resultado = subconjuntos_de_dois(letras)

    print(f"Conjunto original: {letras}")
    print(f"Subconjuntos de 2 letras (total: {len(resultado)}):")
    for sub in resultado:
        print(f"  {sub}")

    # Exibição no formato da questão:
    formatado = ", ".join(str(sub) for sub in resultado)
    print(f"\nFormato da questão:\n{letras} → {formatado}")
