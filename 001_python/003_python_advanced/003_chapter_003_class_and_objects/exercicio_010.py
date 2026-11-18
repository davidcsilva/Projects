"""
Exercício 16.10:
Classe Conjunto que gerencie um conjunto de inteiros (int) com ajuda de uma tabela de tamanho fixo.
Características:
- Cada elemento é único (não há repetições).
- Elementos não possuem ordem obrigatória.

Operações implementadas:
- vazia(): esvazia o conjunto.
- agregar(item): adiciona um inteiro ao conjunto (se ainda não existir).
- eliminar(item): retira um inteiro do conjunto.
- copiar(outro): copia um conjunto em outro.
- é_membro(item): retorna booleano indicando se o elemento pertence ao conjunto.
- é_igual(outro): retorna booleano indicando se o conjunto é igual a outro.
- imprimir(): efetua a visualização formatada do conjunto.
"""

from typing import Optional


class Conjunto:
    """
    Implementação de um Tipo Abstrato de Dados (TAD) Conjunto de inteiros
    armazenado em uma tabela (array) de tamanho fixo.
    """

    CAPACIDADE_PADRAO: int = 100

    def __init__(self, capacidade: int = CAPACIDADE_PADRAO) -> None:
        """
        Inicializa o conjunto com uma tabela de tamanho fixo.
        """
        self._capacidade: int = capacidade
        # Tabela de tamanho fixo pré-alocada
        self._tabela: list[Optional[int]] = [None] * self._capacidade
        # Quantidade atual de elementos válidos no conjunto
        self._tamanho: int = 0

    def vazia(self) -> None:
        """
        Função membro 'vazia':
        Esvazia o conjunto, reiniciando o tamanho e liberando os elementos da tabela.
        """
        for i in range(self._tamanho):
            self._tabela[i] = None
        self._tamanho = 0

    # Alias semântico
    esvaziar = vazia

    def esta_vazio(self) -> bool:
        """Retorna True se o conjunto estiver vazio; caso contrário, False."""
        return self._tamanho == 0

    def é_membro(self, item: int) -> bool:
        """
        Função membro 'é_membro':
        Retorna True se o inteiro 'item' pertencer ao conjunto; caso contrário, False.
        """
        if not isinstance(item, int):
            return False

        for i in range(self._tamanho):
            if self._tabela[i] == item:
                return True
        return False

    # Alias sem acento para facilitar chamadas
    e_membro = é_membro

    def agregar(self, item: int) -> bool:
        """
        Função membro 'agregar':
        Soma (insere) um número inteiro ao conjunto.
        - Se o elemento já for membro, não faz nada e retorna False (garante unicidade).
        - Se a tabela estiver cheia, lança OverflowError.
        - Retorna True se o elemento foi inserido com sucesso.
        """
        if not isinstance(item, int):
            raise TypeError(
                f"O conjunto armazena apenas inteiros, recebido: {type(item).__name__}.")

        # Regra de conjunto: não pode conter duplicatas
        if self.é_membro(item):
            return False

        # Verifica capacidade da tabela de tamanho fixo
        if self._tamanho >= self._capacidade:
            raise OverflowError(
                f"Capacidade máxima atingida ({self._capacidade} elementos). Tabela cheia."
            )

        # Insere no fim da lista válida
        self._tabela[self._tamanho] = item
        self._tamanho += 1
        return True

    def eliminar(self, item: int) -> bool:
        """
        Função membro 'eliminar':
        Retira um inteiro do conjunto.
        Como conjuntos não são ordenados, remove substituindo o elemento encontrado
        pelo último elemento da tabela em tempo O(1) após a busca.
        Retorna True se o elemento foi encontrado e removido; caso contrário, False.
        """
        if not isinstance(item, int):
            return False

        for i in range(self._tamanho):
            if self._tabela[i] == item:
                # Move o último elemento para a posição atual
                ultimo = self._tabela[self._tamanho - 1]
                self._tabela[i] = ultimo
                self._tabela[self._tamanho - 1] = None
                self._tamanho -= 1
                return True

        return False

    def copiar(self, outro: "Conjunto") -> None:
        """
        Função membro 'copiar':
        Copia o conteúdo de 'outro' conjunto para este conjunto (self).
        """
        if not isinstance(outro, Conjunto):
            raise TypeError(
                "O objeto a ser copiado deve ser uma instância de Conjunto.")

        if self is outro:
            return  # Auto-atribuição, nada a fazer

        # Ajusta capacidade se necessário
        if self._capacidade < outro._tamanho:
            self._capacidade = outro._capacidade
            self._tabela = [None] * self._capacidade

        # Esvazia o conjunto atual e copia os elementos
        self.vazia()
        for i in range(outro._tamanho):
            self._tabela[i] = outro._tabela[i]
        self._tamanho = outro._tamanho

    def clone(self) -> "Conjunto":
        """Retorna uma nova instância independente de Conjunto idêntica a esta."""
        novo = Conjunto(capacidade=self._capacidade)
        novo.copiar(self)
        return novo

    def é_igual(self, outro: "Conjunto") -> bool:
        """
        Função membro 'é_igual':
        Retorna True se ambos os conjuntos tiverem a mesma cardinalidade e
        todos os elementos deste conjunto pertencerem a 'outro'.
        """
        if not isinstance(outro, Conjunto):
            return False

        if self._tamanho != outro._tamanho:
            return False

        # Cada elemento de self deve estar em outro
        for i in range(self._tamanho):
            elem = self._tabela[i]
            assert elem is not None
            if not outro.é_membro(elem):
                return False

        return True

    # Alias sem acento
    e_igual = é_igual

    def imprimir(self) -> None:
        """
        Função membro 'imprimir':
        Efetua a visualização formatada do conjunto no padrão matemático:
        Exemplo: {10, 20, 30} ou {} se estiver vazio.
        """
        elementos = [str(self._tabela[i]) for i in range(self._tamanho)]
        print("{" + ", ".join(elementos) + "}")

    # --- Métodos Mágicos do Python ---

    def __contains__(self, item: int) -> bool:
        """Permite o uso do operador 'in' (ex: item in conjunto)."""
        return self.é_membro(item)

    def __eq__(self, outro: object) -> bool:
        """Permite o uso do operador '==' (ex: c1 == c2)."""
        if not isinstance(outro, Conjunto):
            return False
        return self.é_igual(outro)

    def __len__(self) -> int:
        """Permite o uso de len(conjunto)."""
        return self._tamanho

    def __str__(self) -> str:
        elementos = [str(self._tabela[i]) for i in range(self._tamanho)]
        return "{" + ", ".join(elementos) + "}"

    def __repr__(self) -> str:
        return f"Conjunto(elementos={self!s}, tamanho={self._tamanho}/{self._capacidade})"


# Alias conforme enunciado
conjunto = Conjunto


def main() -> None:
    print("=== Exercício 16.10: Classe Conjunto com Tabela de Tamanho Fixo ===")

    # 1. Criação do conjunto
    c1 = Conjunto(capacidade=10)
    print("Conjunto c1 recém-criado:")
    c1.imprimir()
    print(f"Está vazio? {c1.esta_vazio()}\n")

    # 2. Testando agregar() e garantia de unicidade
    print("--- Testando agregar() ---")
    itens = [10, 20, 30, 20, 40, 10, 50]
    print(f"Tentando inserir a sequência: {itens}")
    for item in itens:
        sucesso = c1.agregar(item)
        status = "inserido" if sucesso else "ignorado (duplicado)"
        print(f"  agregar({item:2d}) -> {status}")

    print("Estado de c1 após inserções: ", end="")
    c1.imprimir()
    print(f"Cardinalidade (tamanho): {len(c1)}\n")

    # 3. Testando é_membro()
    print("--- Testando é_membro() ---")
    print(f"c1.é_membro(20) -> {c1.é_membro(20)} (esperado: True)")
    print(f"c1.é_membro(99) -> {c1.é_membro(99)} (esperado: False)")
    print(f"Uso do operador 'in': 30 in c1 -> {30 in c1}\n")

    # 4. Testando eliminar()
    print("--- Testando eliminar() ---")
    print("Removendo o elemento 20...")
    c1.eliminar(20)
    print("c1 após eliminar(20): ", end="")
    c1.imprimir()
    print(f"20 ainda é membro? {c1.é_membro(20)}")
    print("Tentando eliminar elemento inexistente 99:", c1.eliminar(99), "\n")

    # 5. Testando copiar() e é_igual()
    print("--- Testando copiar() e é_igual() ---")
    c2 = Conjunto(capacidade=10)
    print("Copiando c1 para c2...")
    c2.copiar(c1)
    print("c2: ", end="")
    c2.imprimir()
    print(f"c1.é_igual(c2) -> {c1.é_igual(c2)} (esperado: True)")
    print(f"c1 == c2       -> {c1 == c2}")

    # Modificando c2 e retestando igualdade
    c2.agregar(99)
    print("\nApós adicionar 99 em c2:")
    print("c1: ", end="")
    c1.imprimir()
    print("c2: ", end="")
    c2.imprimir()
    print(f"c1.é_igual(c2) -> {c1.é_igual(c2)} (esperado: False)\n")

    # 6. Testando vazia()
    print("--- Testando vazia() (esvaziar) ---")
    print("Esvaziando c1...")
    c1.vazia()
    print("c1 após c1.vazia(): ", end="")
    c1.imprimir()
    print(f"c1 está vazio? {c1.esta_vazio()}")


if __name__ == "__main__":
    main()
