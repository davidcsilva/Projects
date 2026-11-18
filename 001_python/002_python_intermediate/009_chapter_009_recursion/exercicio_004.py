'''
14.4 Converta a seguinte função iterativa em uma recursiva. A função calcula um valor aproximado de e, a base dos
logaritmos naturais, somando as séries:

1 + 1/1! + 1/2! + ... + 1/n!

até que os termos adicionados não afetem a aproximação:

real função loge( )
  var
    // Dados locais
    real: enl, delta, fat
    inteiro: n
  início
    enl <- 1.0
    fat <- 1.0
    delta <- 1.0
    fazer
      enl <- enl + delta
      n <- n + 1
      fat <- fat * n
      delta <- 1.0 / fat
    enquanto (enl <> enl + delta)
    devolver (enl)
fim_função
'''
import math


def loge(enl: float = 1.0, delta: float = 1.0, fat: float = 1.0, n: int = 1) -> float:
    """Calcula um valor aproximado de e (base dos logaritmos naturais) de forma recursiva.

    A aproximação é feita pela série: e = 1 + 1/1! + 1/2! + ... + 1/n!
    até que o termo adicionado (delta) não altere a aproximação devido à precisão de ponto flutuante.
    """
    # Caso base: quando o termo delta é tão pequeno que não altera mais a soma
    if enl == enl + delta:
        return enl

    # Passo da iteração: acumula o termo atual
    enl = enl + delta

    # Prepara o próximo termo: (n + 1)! e delta = 1.0 / (n + 1)!
    n += 1
    fat *= n
    delta = 1.0 / fat

    # Chamada recursiva com o estado atualizado
    return loge(enl, delta, fat, n)


if __name__ == "__main__":
    valor_calculado = loge()
    valor_math = math.e

    print(f"Valor aproximado calculado: {valor_calculado:.16f}")
    print(f"Valor real (math.e):         {valor_math:.16f}")
    print(
        f"Diferença absoluta:         {abs(valor_calculado - valor_math):.2e}")
