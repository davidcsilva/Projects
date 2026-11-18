'''
17.7 Implemente uma hierarquia de tipos dados numéricos que estenda os tipos de dados fundamentais, como
int e float, disponíveis em C++. As classes a serem projetadas podem ser Complexo, Fração, Vetor,
Matriz etc.
'''

import math
from abc import ABC, abstractmethod


# ==============================================================================
# NÍVEL 1: CLASSE BASE ABSTRATA
# ==============================================================================

class TipoNumerico(ABC):
    """Classe base abstrata para todos os tipos numéricos estendidos."""

    @abstractmethod
    def norma(self) -> float:
        """Retorna o valor absoluto, módulo ou norma da estrutura."""

    @abstractmethod
    def multiplicar_por_escalar(self, k: int | float) -> "TipoNumerico":
        """Multiplica o objeto numérico por um escalar primitivo (int ou float)."""

    @abstractmethod
    def __str__(self) -> str:
        """Representação textual legível."""


# ==============================================================================
# NÍVEL 2: ESCALAR E COLEÇÃO NUMÉRICA
# ==============================================================================

class Escalar(TipoNumerico, ABC):
    """Subclasse abstrata para grandezas escalares unidimensionais."""

    @abstractmethod
    def __float__(self) -> float:
        """Permite conversão direta via float(obj)."""


class ColecaoNumerica(TipoNumerico, ABC):
    """Subclasse abstrata para estruturas multidimensionais."""

    @abstractmethod
    def __len__(self) -> int:
        """Retorna a quantidade total de elementos."""


# ==============================================================================
# NÍVEL 3 (RAMO ESCALAR): FRAÇÃO E COMPLEXO
# ==============================================================================

class Fracao(Escalar):
    """Representa um número racional a/b simplificado automaticamente."""

    def __init__(self, numerador: int, denominador: int = 1):
        if denominador == 0:
            raise ValueError("O denominador não pode ser zero.")
        if denominador < 0:
            numerador = -numerador
            denominador = -denominador

        mdc = math.gcd(abs(numerador), denominador)
        self.numerador = numerador // mdc
        self.denominador = denominador // mdc

    @classmethod
    def _converter(cls, valor: "Fracao | int") -> "Fracao":
        if isinstance(valor, Fracao):
            return valor
        if isinstance(valor, int):
            return cls(valor, 1)
        raise TypeError(
            f"Operação não suportada entre Fracao e {type(valor).__name__}.")

    def __float__(self) -> float:
        return self.numerador / self.denominador

    def norma(self) -> float:
        return abs(float(self))

    def multiplicar_por_escalar(self, k: int | float) -> "Fracao":
        return Fracao(self.numerador * int(round(k)), self.denominador)

    def __add__(self, outro: "Fracao | int") -> "Fracao":
        o = self._converter(outro)
        return Fracao(
            self.numerador * o.denominador + o.numerador * self.denominador,
            self.denominador * o.denominador,
        )

    def __radd__(self, outro: int) -> "Fracao":
        return self.__add__(outro)

    def __sub__(self, outro: "Fracao | int") -> "Fracao":
        o = self._converter(outro)
        return Fracao(
            self.numerador * o.denominador - o.numerador * self.denominador,
            self.denominador * o.denominador,
        )

    def __mul__(self, outro: "Fracao | int") -> "Fracao":
        o = self._converter(outro)
        return Fracao(self.numerador * o.numerador, self.denominador * o.denominador)

    def __rmul__(self, outro: int) -> "Fracao":
        return self.__mul__(outro)

    def __str__(self) -> str:
        return f"{self.numerador}" if self.denominador == 1 else f"{self.numerador}/{self.denominador}"


class Complexo(Escalar):
    """Representa um número complexo na forma a + bi."""

    def __init__(self, real: float = 0.0, imag: float = 0.0):
        self.real = float(real)
        self.imag = float(imag)

    @classmethod
    def _converter(cls, valor: "Complexo | int | float") -> "Complexo":
        if isinstance(valor, Complexo):
            return valor
        if isinstance(valor, (int, float)):
            return cls(valor, 0.0)
        raise TypeError(
            f"Operação não suportada entre Complexo e {type(valor).__name__}.")

    def __float__(self) -> float:
        return self.real

    def norma(self) -> float:
        return math.hypot(self.real, self.imag)

    def conjugado(self) -> "Complexo":
        return Complexo(self.real, -self.imag)

    def multiplicar_por_escalar(self, k: int | float) -> "Complexo":
        return Complexo(self.real * k, self.imag * k)

    def __add__(self, outro: "Complexo | int | float") -> "Complexo":
        o = self._converter(outro)
        return Complexo(self.real + o.real, self.imag + o.imag)

    def __radd__(self, outro: int | float) -> "Complexo":
        return self.__add__(outro)

    def __sub__(self, outro: "Complexo | int | float") -> "Complexo":
        o = self._converter(outro)
        return Complexo(self.real - o.real, self.imag - o.imag)

    def __mul__(self, outro: "Complexo | int | float") -> "Complexo":
        o = self._converter(outro)
        return Complexo(
            self.real * o.real - self.imag * o.imag,
            self.real * o.imag + self.imag * o.real,
        )

    def __rmul__(self, outro: int | float) -> "Complexo":
        return self.__mul__(outro)

    def __str__(self) -> str:
        sinal = "+" if self.imag >= 0 else "-"
        return f"{self.real:g} {sinal} {abs(self.imag):g}i"


# ==============================================================================
# NÍVEL 3 (RAMO MULTIDIMENSIONAL): VETOR E MATRIZ
# ==============================================================================

class Vetor(ColecaoNumerica):
    """Representa um vetor n-dimensional de números reais."""

    def __init__(self, elementos: list[int | float]):
        self.dados = [float(x) for x in elementos]

    def __len__(self) -> int:
        return len(self.dados)

    def __getitem__(self, indice: int) -> float:
        return self.dados[indice]

    def norma(self) -> float:
        return math.sqrt(sum(x * x for x in self.dados))

    def multiplicar_por_escalar(self, k: int | float) -> "Vetor":
        return Vetor([x * k for x in self.dados])

    def produto_escalar(self, outro: "Vetor") -> float:
        if len(self) != len(outro):
            raise ValueError("Os vetores devem ter a mesma dimensão.")
        return sum(a * b for a, b in zip(self.dados, outro.dados))

    def __add__(self, outro: "Vetor") -> "Vetor":
        if not isinstance(outro, Vetor) or len(self) != len(outro):
            raise ValueError("Soma requer dois vetores de mesma dimensão.")
        return Vetor([a + b for a, b in zip(self.dados, outro.dados)])

    def __mul__(self, k: int | float) -> "Vetor":
        if isinstance(k, (int, float)):
            return self.multiplicar_por_escalar(k)
        raise TypeError("Use produto_escalar() para multiplicar dois vetores.")

    def __rmul__(self, k: int | float) -> "Vetor":
        return self.__mul__(k)

    def __str__(self) -> str:
        return f"[{', '.join(f'{x:g}' for x in self.dados)}]"


class Matriz(ColecaoNumerica):
    """Representa uma matriz m x n de números reais."""

    def __init__(self, linhas: list[list[int | float]]):
        if not linhas or not linhas[0]:
            raise ValueError("A matriz não pode ser vazia.")
        cols = len(linhas[0])
        if any(len(linha) != cols for linha in linhas):
            raise ValueError(
                "Todas as linhas da matriz devem ter o mesmo comprimento.")

        self.dados = [[float(val) for val in linha] for linha in linhas]
        self.num_linhas = len(linhas)
        self.num_colunas = cols

    def __len__(self) -> int:
        return self.num_linhas * self.num_colunas

    def norma(self) -> float:
        """Norma de Frobenius."""
        return math.sqrt(sum(val * val for linha in self.dados for val in linha))

    def multiplicar_por_escalar(self, k: int | float) -> "Matriz":
        return Matriz([[val * k for val in linha] for linha in self.dados])

    def __add__(self, outra: "Matriz") -> "Matriz":
        if (self.num_linhas, self.num_colunas) != (outra.num_linhas, outra.num_colunas):
            raise ValueError("Dimensões incompatíveis para soma de matrizes.")
        return Matriz([
            [self.dados[i][j] + outra.dados[i][j]
                for j in range(self.num_colunas)]
            for i in range(self.num_linhas)
        ])

    def __mul__(self, outro: "Matriz | int | float") -> "Matriz":
        if isinstance(outro, (int, float)):
            return self.multiplicar_por_escalar(outro)
        if isinstance(outro, Matriz):
            if self.num_colunas != outro.num_linhas:
                raise ValueError(
                    "Dimensões incompatíveis para multiplicação matricial.")
            resultado = [
                [
                    sum(self.dados[i][k] * outro.dados[k][j]
                        for k in range(self.num_colunas))
                    for j in range(outro.num_colunas)
                ]
                for i in range(self.num_linhas)
            ]
            return Matriz(resultado)
        raise TypeError("Operando inválido para multiplicação com Matriz.")

    def __rmul__(self, k: int | float) -> "Matriz":
        if isinstance(k, (int, float)):
            return self.multiplicar_por_escalar(k)
        raise TypeError("Operando inválido.")

    def __str__(self) -> str:
        linhas_fmt = [
            "  | " + " ".join(f"{val:6g}" for val in linha) + " |" for linha in self.dados]
        return "\n" + "\n".join(linhas_fmt)


# ==============================================================================
# EXEMPLO DE EXECUÇÃO E DEMONSTRAÇÃO POLIMÓRFICA
# ==============================================================================

if __name__ == "__main__":
    # 1. Interoperabilidade natural com int e float via sobrecarga de operadores
    f1, f2 = Fracao(2, 4), Fracao(1, 3)  # f1 simplifica para 1/2
    soma_f = 2 + f1 + f2
    print(f"Fração: 2 + {f1} + {f2} = {soma_f} (decimal: {float(soma_f):.4f})")

    c1, c2 = Complexo(3, 4), Complexo(1, -2)
    print(f"Complexo: ({c1}) * ({c2}) = {c1 * c2}")

    v1, v2 = Vetor([1, 2, 3]), Vetor([4, 5, 6])
    print(
        f"Vetor: {v1} + {v2} = {v1 + v2} | Produto Escalar = {v1.produto_escalar(v2)}")

    m1 = Matriz([[1, 2], [3, 4]])
    m2 = Matriz([[2, 0], [1, 2]])
    print(f"Matriz M1 * M2 ={m1 * m2}")

    # 2. Polimorfismo sobre a classe base TipoNumerico
    colecao: list[TipoNumerico] = [
        Fracao(3, 4),
        Complexo(3, 4),
        Vetor([3, 4]),
        m1,
    ]

    print("\n=== DEMONSTRAÇÃO POLIMÓRFICA (Norma e Escala x2) ===")
    for item in colecao:
        escalado = item.multiplicar_por_escalar(2)
        print(
            f"Tipo: {type(item).__name__:8s} | Original: {item} | Norma: {item.norma():.2f} | x2: {escalado}")
