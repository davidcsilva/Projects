"""
Exercícios de Estruturas de Dados e Orientação a Objetos em Python:
16.1 Pilha baseada em Array (Vetor de tamanho fixo: 100 caracteres)
16.2 Pilha baseada em Lista Ligada (Estrutura dinâmica)
"""

from typing import Optional


# ============================================================================
# 16.1 - Pilha com Array (Tamanho fixo de 100 caracteres)
# ============================================================================
class PilhaArray:
    """
    Implementação de uma pilha com capacidade fixa para 100 caracteres
    utilizando um array (vetor simulado via lista de tamanho fixo).
    """

    CAPACIDADE: int = 100

    def __init__(self, capacidade: int = CAPACIDADE) -> None:
        self.capacidade: int = capacidade
        # Aloca o array com posições vazias (None)
        self._elementos: list[Optional[str]] = [None] * self.capacidade
        # Apontador para o topo (-1 indica pilha vazia)
        self._topo: int = -1

    def pilhavazia(self) -> bool:
        """Retorna True se a pilha estiver vazia; caso contrário, False."""
        return self._topo == -1

    def pilhacheia(self) -> bool:
        """Retorna True se a pilha atingir a capacidade máxima; caso contrário, False."""
        return self._topo == self.capacidade - 1

    def colocar(self, caractere: str) -> None:
        """
        Insere um caractere no topo da pilha.
        Lança OverflowError se a pilha já estiver cheia.
        """
        if not isinstance(caractere, str) or len(caractere) != 1:
            raise ValueError(
                "O elemento inserido deve ser um único caractere (string de tamanho 1).")

        if self.pilhacheia():
            raise OverflowError(
                "Estouro de pilha (Stack Overflow): a pilha está cheia.")

        self._topo += 1
        self._elementos[self._topo] = caractere

    def retirar(self) -> str:
        """
        Remove e retorna o caractere do topo da pilha.
        Lança IndexError se a pilha estiver vazia.
        """
        if self.pilhavazia():
            raise IndexError(
                "Subfluxo de pilha (Stack Underflow): a pilha está vazia.")

        caractere = self._elementos[self._topo]
        self._elementos[self._topo] = None  # Libera a referência
        self._topo -= 1
        return caractere  # type: ignore[return-value]

    def topo(self) -> Optional[str]:
        """Consulta o caractere do topo sem removê-lo."""
        if self.pilhavazia():
            return None
        return self._elementos[self._topo]

    def __len__(self) -> int:
        """Retorna o número de elementos na pilha."""
        return self._topo + 1

    def __repr__(self) -> str:
        itens = [repr(self._elementos[i]) for i in range(self._topo, -1, -1)]
        return f"PilhaArray(topo -> [{', '.join(itens)}], total={len(self)}/{self.capacidade})"


# ============================================================================
# 16.2 - Pilha com Lista Ligada (Alocação Dinâmica)
# ============================================================================
class No:
    """Nó individual para a lista ligada."""

    def __init__(self, dado: str, proximo: Optional["No"] = None) -> None:
        self.dado: str = dado
        self.proximo: Optional["No"] = proximo


class PilhaListaLigada:
    """
    Implementação de uma pilha utilizando uma lista ligada (encadeada).
    Nesta abordagem, a memória é alocada dinamicamente para cada novo nó.
    """

    def __init__(self) -> None:
        self._topo: Optional[No] = None
        self._tamanho: int = 0

    def pilhavazia(self) -> bool:
        """Retorna True se a pilha estiver vazia; caso contrário, False."""
        return self._topo is None

    def pilhacheia(self) -> bool:
        """
        Em uma lista ligada pura, a capacidade é dinâmica e limitada apenas
        pela memória do sistema. Portanto, a pilha nunca fica cheia.
        """
        return False

    def colocar(self, caractere: str) -> None:
        """
        Insere um caractere no topo da pilha criando um novo nó encadeado.
        """
        if not isinstance(caractere, str) or len(caractere) != 1:
            raise ValueError(
                "O elemento inserido deve ser um único caractere (string de tamanho 1).")

        novo_no = No(caractere, proximo=self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def retirar(self) -> str:
        """
        Remove e retorna o caractere do topo da pilha.
        Lança IndexError se a pilha estiver vazia.
        """
        if self.pilhavazia():
            raise IndexError(
                "Subfluxo de pilha (Stack Underflow): a pilha está vazia.")

        assert self._topo is not None
        caractere_removido = self._topo.dado
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return caractere_removido

    def topo(self) -> Optional[str]:
        """Consulta o caractere do topo sem removê-lo."""
        if self.pilhavazia():
            return None
        assert self._topo is not None
        return self._topo.dado

    def __len__(self) -> int:
        """Retorna a quantidade de elementos armazenados."""
        return self._tamanho

    def __repr__(self) -> str:
        elementos = []
        atual = self._topo
        while atual is not None:
            elementos.append(repr(atual.dado))
            atual = atual.proximo
        return f"PilhaListaLigada(topo -> [{', '.join(elementos)}], total={self._tamanho})"


# ============================================================================
# Testes e Demonstração de Uso
# ============================================================================
if __name__ == "__main__":
    print("--- Testando 16.1: PilhaArray ---")
    pilha_arr = PilhaArray()
    print(f"Pilha recém-criada está vazia? {pilha_arr.pilhavazia()}")  # True
    print(f"Está cheia? {pilha_arr.pilhacheia()}")                   # False

    # Inserindo alguns caracteres
    palavra = "ESTRUTURA"
    for letra in palavra:
        pilha_arr.colocar(letra)
    print(f"Após inserir '{palavra}': {pilha_arr}")

    # Retirando elementos (deve desempilhar na ordem inversa: LIFO)
    desempilhado = []
    while not pilha_arr.pilhavazia():
        desempilhado.append(pilha_arr.retirar())
    print(f"Caracteres desempilhados: {''.join(desempilhado)}")

    # Testando limite da pilha de 100 caracteres
    print("\nPreenchendo até a capacidade máxima de 100...")
    for i in range(100):
        pilha_arr.colocar(chr(65 + (i % 26)))
    print(f"Pilha está cheia agora? {pilha_arr.pilhacheia()}")  # True

    try:
        pilha_arr.colocar("X")
    except OverflowError as e:
        print(f"Exceção capturada com sucesso ao exceder capacidade: {e}")

    print("\n--- Testando 16.2: PilhaListaLigada ---")
    pilha_lista = PilhaListaLigada()
    print(f"Pilha recém-criada está vazia? {pilha_lista.pilhavazia()}")  # True
    # False
    print(f"Está cheia? {pilha_lista.pilhacheia()}")

    for letra in "PYTHON":
        pilha_lista.colocar(letra)
    print(f"Após inserir 'PYTHON': {pilha_lista}")

    desempilhado_lista = []
    while not pilha_lista.pilhavazia():
        desempilhado_lista.append(pilha_lista.retirar())
    print(f"Caracteres desempilhados: {''.join(desempilhado_lista)}")

    try:
        pilha_lista.retirar()
    except IndexError as e:
        print(f"Exceção capturada com sucesso ao desempilhar pilha vazia: {e}")
