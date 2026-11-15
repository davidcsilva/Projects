'''
14.19 Escreva um programa em que o usuário introduza 10 inteiros positivos e calcule e imprima seu fatorial.
'''


def fatorial(n: int) -> int:
    """Calcula o fatorial de um número inteiro positivo de forma recursiva.

    Definição:
        fatorial(1) = 1
        fatorial(n) = n * fatorial(n - 1)
    """
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    if n in (0, 1):
        return 1
    return n * fatorial(n - 1)


def obter_10_inteiros_positivos() -> list[int]:
    """Lê 10 números inteiros positivos do usuário, validando cada entrada."""
    numeros: list[int] = []
    total = 10
    print(f"Por favor, introduza {total} números inteiros positivos:\n")

    for i in range(1, total + 1):
        while True:
            try:
                entrada = input(
                    f"Digite o {i:>2}º número inteiro positivo: ").strip()
                if not entrada:
                    raise EOFError
                valor = int(entrada)
                if valor <= 0:
                    print(
                        "  -> O número deve ser estritamente positivo (> 0). Tente novamente.")
                    continue
                numeros.append(valor)
                break
            except ValueError:
                print(
                    "  -> Entrada inválida. Por favor, digite um número inteiro válido.")
            except EOFError:
                # Fallback automático caso executado sem terminal interativo
                faltantes = total - len(numeros)
                valores_padrao = list(range(len(numeros) + 1, total + 1))
                print(
                    f"\n[Execução automática]: Preenchendo {faltantes} valores restantes com: {valores_padrao}")
                numeros.extend(valores_padrao)
                return numeros

    return numeros


def main() -> None:
    print("=== PROGRAMA: CÁLCULO DE FATORIAL DE 10 NÚMEROS ===")
    numeros = obter_10_inteiros_positivos()

    print("\n" + "=" * 45)
    print(f"{'Número (n)':^15} | {'Fatorial (n!)':^25}")
    print("=" * 45)

    for num in numeros:
        resultado = fatorial(num)
        print(f"{num:^15} | {resultado:>25,}".replace(",", "."))

    print("=" * 45)


if __name__ == "__main__":
    main()
