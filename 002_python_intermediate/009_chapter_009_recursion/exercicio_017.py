'''
Desenvolva uma função recursiva que conte o número de números binários de n-dígitos que não
tenham dois 1 em uma fila. (Sugestão: O número começa com um 0 ou um 1. Começando com 0, o
número de possibilidades é determinado pelos restantes n – 1 dígitos. Começando com 1, qual
deve ser o seguinte?)

ANÁLISE E DEDUÇÃO RECURSIVA:
Para construir uma sequência binária válida de tamanho n:
1. Se o primeiro dígito for '0':
   O próximo dígito pode ser qualquer um (0 ou 1). Logo, restam (n - 1) posições a preencher,
   o que dá f(n - 1) possibilidades.

2. Se o primeiro dígito for '1':
   O segundo dígito OBRIGATORIAMENTE deve ser '0' (para não haver dois 1 consecutivos: "11").
   Portanto, os dois primeiros dígitos são fixos ("10"), restando (n - 2) posições a preencher,
   o que dá f(n - 2) possibilidades.

Relação de Recorrência:
    f(n) = f(n - 1) + f(n - 2)

Casos Base:
    - Para n = 0: 1 possibilidade (cadeia vazia "")
    - Para n = 1: 2 possibilidades ("0" e "1")
'''


def contar_binarios(n: int) -> int:
    """Calcula recursivamente a quantidade de números binários de n dígitos sem '11' consecutivos."""
    if n < 0:
        raise ValueError(
            "O número de dígitos n deve ser maior ou igual a zero.")

    # Casos base:
    if n == 0:
        return 1
    if n == 1:
        return 2

    # Relação recursiva:
    # f(n - 1): começa com 0
    # f(n - 2): começa com 10
    return contar_binarios(n - 1) + contar_binarios(n - 2)


def gerar_binarios(n: int) -> list[str]:
    """Gera recursivamente a lista de todas as cadeias binárias válidas de tamanho n."""
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1"]

    resultado: list[str] = []
    # Começando com '0':
    for sub in gerar_binarios(n - 1):
        resultado.append("0" + sub)
    # Começando com '1' (seguido obrigatoriamente de '0'):
    for sub in gerar_binarios(n - 2):
        resultado.append("10" + sub)

    return resultado


if __name__ == "__main__":
    print("=== NÚMEROS BINÁRIOS DE N DÍGITOS SEM '1' CONSECUTIVOS ===")
    print(f"{'n':>2} | {'Quantidade':>10} | {'Sequências geradas'}")
    print("-" * 65)

    for n in range(1, 6):
        qtd = contar_binarios(n)
        lista = gerar_binarios(n)
        print(f"{n:>2} | {qtd:>10} | {lista}")

    print("\nPara valores maiores de n:")
    for n in [6, 7, 8, 10]:
        print(f"n = {n:>2} dígitos -> {contar_binarios(n)} combinações válidas")
