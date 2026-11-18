"""
Exercício 16.11:
Criar uma classe Lista que realize as seguintes tarefas:
- Uma lista simples que contenha zero ou mais elementos de algum tipo específico.
- Criar uma lista vazia.
- Somar (adicionar) elementos à lista.
- Determinar se a lista está vazia.
- Determinar se a lista está cheia.
- Acessar cada elemento da lista e efetuar alguma ação sobre ela.
"""

from typing import Any, Callable, Generic, Iterator, Optional, TypeVar

# Parâmetro de tipo genérico
T = TypeVar("T")


class Lista(Generic[T]):
    """
    Implementação de uma Lista Simples Homogênea (TAD Lista) de tipo específico
    com capacidade configurável.
    """

    CAPACIDADE_PADRAO: int = 100

    # 1. & 2. Construtor que cria uma lista vazia de um tipo específico
    def __init__(
        self,
        tipo_esperado: Optional[type] = None,
        capacidade: int = CAPACIDADE_PADRAO,
    ) -> None:
        """
        Inicializa uma lista vazia.
        - tipo_esperado: especifica o tipo dos elementos (ex: int, str, float). Se None, infere no 1º item.
        - capacidade: define a capacidade máxima da tabela de armazenamento.
        """
        self.tipo_esperado: Optional[type] = tipo_esperado
        self.capacidade: int = capacidade
        self._itens: list[Optional[T]] = [None] * self.capacidade
        self._tamanho: int = 0

    # 4. Determinar se a lista está vazia
    def esta_vazia(self) -> bool:
        """Retorna True se a lista não contiver nenhum elemento; caso contrário, False."""
        return self._tamanho == 0

    # 5. Determinar se a lista está cheia
    def esta_cheia(self) -> bool:
        """Retorna True se a lista atingiu sua capacidade máxima; caso contrário, False."""
        return self._tamanho == self.capacidade

    # 3. Somar (adicionar) elementos à lista
    def somar_elemento(self, elemento: T) -> None:
        """
        Adiciona (soma) um novo elemento ao final da lista.
        Garante a homogeneidade do tipo e impede estouro de capacidade.
        """
        if self.esta_cheia():
            raise OverflowError(
                f"A lista está cheia! Capacidade máxima ({self.capacidade}) atingida."
            )

        # Se o tipo específico ainda não foi definido, fixa no tipo do primeiro elemento
        if self.tipo_esperado is None:
            self.tipo_esperado = type(elemento)

        # Validação do tipo específico dos elementos
        if not isinstance(elemento, self.tipo_esperado):
            raise TypeError(
                f"Elemento inválido: esperado tipo '{self.tipo_esperado.__name__}', "
                f"mas recebeu '{type(elemento).__name__}'."
            )

        self._itens[self._tamanho] = elemento
        self._tamanho += 1

    # Alias convencionais
    adicionar = somar_elemento
    anexar = somar_elemento

    # 6. Acessar cada elemento da lista e efetuar alguma ação sobre ela
    def percorrer(self, acao: Callable[[T], Any]) -> None:
        """
        Acessa cada elemento da lista sequencialmente e executa uma função de ação
        (callback/função de alta ordem) sobre ele.
        """
        for i in range(self._tamanho):
            item = self._itens[i]
            assert item is not None
            acao(item)

    def transformar(self, acao: Callable[[T], T]) -> None:
        """
        Acessa cada elemento e substitui pelo resultado da ação executada sobre ele.
        """
        for i in range(self._tamanho):
            item = self._itens[i]
            assert item is not None
            self._itens[i] = acao(item)

    def obter(self, indice: int) -> T:
        """Acessa um elemento individual por seu índice (0 até tamanho - 1)."""
        if indice < 0 or indice >= self._tamanho:
            raise IndexError(f"Índice fora dos limites da lista: {indice}.")
        item = self._itens[indice]
        assert item is not None
        return item

    # --- Métodos Mágicos e Idiomáticos de Python ---

    def __len__(self) -> int:
        return self._tamanho

    def __getitem__(self, indice: int) -> T:
        return self.obter(indice)

    def __iter__(self) -> Iterator[T]:
        for i in range(self._tamanho):
            item = self._itens[i]
            assert item is not None
            yield item

    def __add__(self, elemento: T) -> "Lista[T]":
        """Permite a sintaxe lista + elemento."""
        self.somar_elemento(elemento)
        return self

    def __str__(self) -> str:
        elementos = [repr(self._itens[i]) for i in range(self._tamanho)]
        tipo = self.tipo_esperado.__name__ if self.tipo_esperado else "Indefinido"
        return f"Lista[{tipo}]({', '.join(elementos)})"

    def __repr__(self) -> str:
        return (
            f"Lista(tipo={self.tipo_esperado.__name__ if self.tipo_esperado else None}, "
            f"tamanho={self._tamanho}/{self.capacidade})"
        )


# Alias conforme enunciado
lista = Lista


def main() -> None:
    print("=== Exercício 16.11: Classe Lista de Tipo Específico ===")

    # 1. & 2. Criar uma lista vazia com tipo específico (ex: int) e capacidade 5
    print("\n--- 1 & 2. Criando lista vazia de inteiros (capacidade=5) ---")
    lista_int: Lista[int] = Lista(tipo_esperado=int, capacidade=5)
    print(f"Lista criada: {lista_int}")
    print(f"Está vazia? {lista_int.esta_vazia()} (esperado: True)")
    print(f"Está cheia? {lista_int.esta_cheia()} (esperado: False)")

    # 3. Somar elementos à lista
    print("\n--- 3. Somando (adicionando) elementos ---")
    valores = [10, 25, 42, 77]
    for val in valores:
        lista_int.somar_elemento(val)
        print(f"  somar_elemento({val}) -> Tamanho atual: {len(lista_int)}")

    print(f"Estado da lista: {lista_int}")
    print(f"Está vazia agora? {lista_int.esta_vazia()} (esperado: False)")
    print(f"Está cheia agora? {lista_int.esta_cheia()} (esperado: False)")

    # Testando validação de tipo homogêneo
    print("\nTentando adicionar um elemento de tipo diferente (string 'Python'):")
    try:
        lista_int.somar_elemento("Python")  # type: ignore[arg-type]
    except TypeError as erro:
        print(f"  Exceção esperada capturada: {erro}")

    # Adicionando o 5º elemento para encher a lista
    lista_int.somar_elemento(99)
    print(f"\nApós adicionar o 5º elemento: {lista_int}")
    print(f"Está cheia agora? {lista_int.esta_cheia()} (esperado: True)")

    try:
        lista_int.somar_elemento(100)
    except OverflowError as erro:
        print(f"  Tentativa de ultrapassar capacidade capturada: {erro}")

    # 6. Acessar cada elemento da lista e efetuar alguma ação sobre ela
    print("\n--- 6. Acessando cada elemento e efetuando ações ---")

    print("\nAção 1: Exibir cada elemento formatado com seu quadrado:")

    def exibir_quadrado(x: int) -> None:
        print(f"  Elemento: {x:2d} -> Quadrado: {x**2}")

    lista_int.percorrer(exibir_quadrado)

    print("\nAção 2: Somar todos os elementos em um acumulador:")
    total = 0

    def acumular(x: int) -> None:
        nonlocal total
        total += x

    lista_int.percorrer(acumular)
    print(f"  Soma total acumulada dos elementos: {total}")

    print("\nAção 3: Modificar os elementos in-place (dobrar cada elemento com transformar):")
    lista_int.transformar(lambda x: x * 2)
    print(f"  Lista após dobrar cada elemento: {lista_int}")

    # Demonstração adicional com lista de strings
    print("\n--- Demonstração com Lista de Strings ---")
    lista_str: Lista[str] = Lista(tipo_esperado=str, capacidade=3)
    lista_str.somar_elemento("Algoritmos")
    lista_str.somar_elemento("Estruturas de Dados")
    lista_str.somar_elemento("Python Avançado")

    print("Imprimindo cada elemento em letras maiúsculas:")
    lista_str.percorrer(lambda s: print(f"  -> {s.upper()}"))


if __name__ == "__main__":
    main()
