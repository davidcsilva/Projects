"""
Exercício 16.9:
Efetue uma classe Complexo que permita o gerenciamento de números complexos
(um número complexo = dois números reais double: uma parte real + uma parte imaginária).
As operações a ser implementadas são as seguintes:
- Uma função estabelecer() permite inicializar um objeto de tipo Complexo de dois componentes double.
- Uma função imprimir() efetua a visualização formatada de um Complexo.
- Duas funções agregar() (sobrecarregadas) permitem acrescentar, respectivamente,
  um Complexo a outro e acrescentar dois componentes double a um Complexo.
"""

from typing import Optional, Union, overload


class Complexo:
    """
    Representa um número complexo: z = a + bi,
    onde 'a' é a parte real e 'b' é a parte imaginária.
    """

    def __init__(self, real: float = 0.0, imag: float = 0.0) -> None:
        """
        Construtor da classe. Inicializa o número complexo chamando estabelecer().
        """
        self.real: float = 0.0
        self.imag: float = 0.0
        self.estabelecer(real, imag)

    def estabelecer(self, real: float = 0.0, imag: float = 0.0) -> None:
        """
        Função membro 'estabelecer':
        Permite inicializar/redefinir os dois componentes double (real e imaginário)
        do objeto Complexo.
        """
        self.real = float(real)
        self.imag = float(imag)

    def imprimir(self) -> None:
        """
        Função membro 'imprimir':
        Efetua a visualização formatada do número complexo no padrão matematicamente usual:
        Exemplos: '3.0 + 4.0i', '5.0 - 2.0i', '7.0 + 0.0i'.
        """
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {abs(self.imag)}i")

    # --- Sobrecarga da função membro 'agregar' ---

    @overload
    def agregar(self, outro: "Complexo") -> None:
        """Assinatura 1: acrescenta outro objeto Complexo a este."""
        ...

    @overload
    def agregar(self, real: float, imag: float) -> None:
        """Assinatura 2: acrescenta dois componentes double a este Complexo."""
        ...

    def agregar(
        self,
        arg1: Union["Complexo", float, int],
        arg2: Optional[Union[float, int]] = None,
    ) -> None:
        """
        Função membro sobrecarregada 'agregar':
        Em Python, a sobrecarga de métodos é implementada verificando a quantidade
        e os tipos dos argumentos recebidos em tempo de execução:
        1. Se receber 1 argumento (Complexo): acrescenta o complexo a este.
        2. Se receber 2 argumentos (double real, double imag): acrescenta as componentes a este.
        """
        if isinstance(arg1, Complexo):
            # 1. Acrescentar um Complexo a outro
            self.real += arg1.real
            self.imag += arg1.imag
        elif isinstance(arg1, (int, float)) and arg2 is not None and isinstance(arg2, (int, float)):
            # 2. Acrescentar dois componentes double a um Complexo
            self.real += float(arg1)
            self.imag += float(arg2)
        else:
            raise TypeError(
                "Chamada inválida para agregar(). "
                "Utilize: agregar(outro_complexo) ou agregar(real, imag)."
            )

    # --- Métodos utilitários e mágicos adicionais em Python ---

    def __str__(self) -> str:
        """Representação em texto formatado."""
        sinal = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sinal} {abs(self.imag)}i"

    def __repr__(self) -> str:
        return f"Complexo(real={self.real}, imag={self.imag})"

    def __add__(self, outro: Union["Complexo", float, int]) -> "Complexo":
        """Sobrecarga do operador '+': retorna um novo Complexo com a soma."""
        if isinstance(outro, Complexo):
            return Complexo(self.real + outro.real, self.imag + outro.imag)
        elif isinstance(outro, (int, float)):
            return Complexo(self.real + float(outro), self.imag)
        return NotImplemented

    def __iadd__(self, outro: Union["Complexo", float, int]) -> "Complexo":
        """Sobrecarga do operador '+=': delega para agregar()."""
        if isinstance(outro, Complexo):
            self.agregar(outro)
            return self
        elif isinstance(outro, (int, float)):
            self.agregar(float(outro), 0.0)
            return self
        return NotImplemented


# Alias conforme convenção
complexo = Complexo


def main() -> None:
    print("=== Exercício 16.9: Classe Complexo com Métodos Sobrecarregados ===")

    # 1. Testando estabelecer() e imprimir()
    c1 = Complexo()
    print("Número c1 recém-criado:")
    c1.imprimir()

    print("\nExecutando c1.estabelecer(4.5, 2.5):")
    c1.estabelecer(4.5, 2.5)
    print("c1 após estabelecer: ", end="")
    c1.imprimir()

    # Criando um segundo número complexo
    c2 = Complexo(1.5, -6.0)
    print("\nNúmero c2 inicializado diretamente: ", end="")
    c2.imprimir()

    # 2. Testando a 1ª sobrecarga de agregar(Complexo)
    print("\n--- Teste 1: agregar(outro_complexo) ---")
    print(f"c1 antes: {c1}")
    print(f"c2 a ser agregado: {c2}")
    c1.agregar(c2)
    print(f"c1 após c1.agregar(c2):")
    print("  Visualização formatada: ", end="")
    c1.imprimir()

    # 3. Testando a 2ª sobrecarga de agregar(double, double)
    print("\n--- Teste 2: agregar(double real, double imag) ---")
    print(f"c1 antes: {c1}")
    delta_real = 2.0
    delta_imag = 5.5
    print(
        f"Componentes a serem agregados: real={delta_real}, imag={delta_imag}")
    c1.agregar(delta_real, delta_imag)
    print(f"c1 após c1.agregar({delta_real}, {delta_imag}):")
    print("  Visualização formatada: ", end="")
    c1.imprimir()

    # 4. Demonstração de uso do operador '+' e '+='
    print("\n--- Teste 3: Operadores '+' e '+=' ---")
    c3 = Complexo(1.0, 1.0)
    c4 = Complexo(2.0, 3.0)
    c5 = c3 + c4
    print(f"({c3}) + ({c4}) = {c5}")

    c5 += Complexo(10.0, 20.0)
    print(f"Após c5 += (10.0 + 20.0i): {c5}")


if __name__ == "__main__":
    main()
