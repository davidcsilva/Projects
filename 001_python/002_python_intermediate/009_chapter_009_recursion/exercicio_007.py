'''
14.7 Suponha que a função G está definida recursivamente da seguinte maneira:

          1              se x <= y
G(x, y) = ------------------------
          G(x - y + 1)   se y < x

sendo x e y inteiros positivos. Encontre o valor de: a) G(8, 6); b) G(100, 10).

NOTA SOBRE A FORMATAÇÃO DO LIVRO:
1. O traço horizontal na expressão é uma falha de diagramação do livro que substituiu
   a chave clássica de definição por partes:
   G(x, y) = { 1             se x <= y
             { ...           se y < x

2. Na segunda linha, a chamada recursiva original de dois argumentos é:
   G(x - y, y) + 1   (onde ", y)" virou incorretamente "+ 1)" por erro tipográfico,
   ou G(x - y + 1, y) mantendo o segundo argumento 'y').
'''


def G_divisao(x: int, y: int) -> int:
    """Interpretação clássica (algoritmo de divisão/quociente recursivo):

    G(x, y) = 1                se x <= y
    G(x, y) = G(x - y, y) + 1  se y < x
    """
    if x <= y:
        return 1
    return G_divisao(x - y, y) + 1


def G_variacao(x: int, y: int) -> int:
    """Interpretação mantendo o termo '+ 1' no primeiro argumento e passando y:

    G(x, y) = 1                    se x <= y
    G(x, y) = G(x - y + 1, y) + 1  se y < x
    """
    if x <= y:
        return 1
    return G_variacao(x - y + 1, y) + 1


def G_sem_soma(x: int, y: int) -> int:
    """Interpretação literal passando y como segundo parâmetro sem somar 1:

    G(x, y) = 1                se x <= y
    G(x, y) = G(x - y + 1, y)  se y < x
    """
    if x <= y:
        return 1
    return G_sem_soma(x - y + 1, y)


def passo_a_passo_G_divisao(x: int, y: int) -> int:
    """Executa e imprime o passo a passo da recursão."""
    print(f"\n--- Traço de G({x}, {y}) [com G(x - y, y) + 1] ---")
    passo = 1
    total_somado = 0
    curr_x = x
    while curr_x > y:
        print(
            f"Passo {passo}: {curr_x} > {y} -> G({curr_x} - {y}, {y}) + 1 = G({curr_x - y}, {y}) + 1")
        curr_x -= y
        total_somado += 1
        passo += 1
    print(f"Passo {passo} (Caso Base): {curr_x} <= {y} -> retorna 1")
    resultado = 1 + total_somado
    print(f"Resultado final: 1 + {total_somado} = {resultado}")
    return resultado


if __name__ == "__main__":
    print("=== RESOLUÇÃO DO EXERCÍCIO 14.7 ===")

    # a) G(8, 6)
    passo_a_passo_G_divisao(8, 6)

    # b) G(100, 10)
    passo_a_passo_G_divisao(100, 10)
