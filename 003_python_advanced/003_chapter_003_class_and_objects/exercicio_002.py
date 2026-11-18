"""
Exercício 16.2:
Reescreva a classe pilha que utilize uma lista ligada em lugar de um array
(sugestão: utilizar outra classe para representar os nós/nodos da lista).

Funções membro da classe:
- colocar(caractere)
- retirar()
- pilhavazia()
- pilhacheia()
"""

from typing import Optional


class Nodo:
    """
    Classe que representa um nó (ou nodo) da lista ligada.
    Cada nó armazena o caractere e uma referência para o próximo nó da pilha.
    """

    def __init__(self, caractere: str, proximo: Optional["Nodo"] = None) -> None:
        self.caractere: str = caractere
        self.proximo: Optional["Nodo"] = proximo

    def __repr__(self) -> str:
        return f"Nodo({self.caractere!r})"


class PilhaListaLigada:
    """
    Implementação da Pilha (TAD) utilizando uma lista ligada encadeada.
    """

    def __init__(self) -> None:
        # O ponteiro para o elemento no topo da pilha
        self._topo: Optional[Nodo] = None
        self._total_elementos: int = 0

    def pilhavazia(self) -> bool:
        """
        Retorna True se a pilha não contiver nenhum elemento;
        caso contrário, retorna False.
        """
        return self._topo is None

    def pilhacheia(self) -> bool:
        """
        Diferente de um array com capacidade pré-determinada, uma lista ligada
        possui alocação dinâmica de memória, permitindo crescer conforme a
        necessidade. Portanto, nunca atinge um limite estático (retorna False).
        """
        return False

    def colocar(self, caractere: str) -> None:
        """
        Insere um caractere no topo da pilha.
        Cria um novo nó cujo ponteiro aponta para o nó do topo atual e
        atualiza o topo para este novo nó.
        """
        if not isinstance(caractere, str) or len(caractere) != 1:
            raise ValueError(
                f"Elemento inválido: {caractere!r}. A pilha armazena caracteres individuais (tamanho 1)."
            )

        # O novo nó aponta para o topo anterior
        novo_nodo = Nodo(caractere=caractere, proximo=self._topo)
        # O topo da pilha passa a ser o novo nó
        self._topo = novo_nodo
        self._total_elementos += 1

    def retirar(self) -> str:
        """
        Remove e retorna o caractere situado no topo da pilha (LIFO - Last In, First Out).
        Lança IndexError se a pilha estiver vazia.
        """
        if self.pilhavazia():
            raise IndexError(
                "Erro de Subfluxo (Stack Underflow): a pilha está vazia.")

        assert self._topo is not None
        nodo_removido = self._topo
        self._topo = self._topo.proximo
        self._total_elementos -= 1

        return nodo_removido.caractere

    def ver_topo(self) -> Optional[str]:
        """
        Permite espiar o caractere do topo da pilha sem removê-lo.
        """
        if self.pilhavazia():
            return None
        assert self._topo is not None
        return self._topo.caractere

    def __len__(self) -> int:
        """Retorna o número total de elementos atualmente empilhados."""
        return self._total_elementos

    def __repr__(self) -> str:
        elementos = []
        atual = self._topo
        while atual is not None:
            elementos.append(repr(atual.caractere))
            atual = atual.proximo
        conteudo = " -> ".join(elementos) if elementos else "vazia"
        return f"PilhaListaLigada(topo -> {conteudo}, total={self._total_elementos})"


# ============================================================================
# Demonstração e Testes
# ============================================================================
if __name__ == "__main__":
    print("=== Demonstração do Exercício 16.2 (Pilha com Lista Ligada) ===")

    pilha = PilhaListaLigada()

    # 1. Verificando estado inicial
    print(f"Pilha criada. pilhavazia() -> {pilha.pilhavazia()}")
    print(f"pilhacheia() -> {pilha.pilhacheia()}")
    print(f"Estado: {pilha}\n")

    # 2. Empilhando caracteres usando colocar()
    palavra = "ESTRUTURA"
    print(f"Empilhando caracteres da palavra: {palavra}")
    for ch in palavra:
        pilha.colocar(ch)
        print(
            f"  colocar('{ch}') -> Topo atual: '{pilha.ver_topo()}' | Total: {len(pilha)}")

    print(f"\nEstado da pilha após inserções:\n  {pilha}\n")

    # 3. Desempilhando usando retirar()
    print("Desempilhando elementos (ordem LIFO):")
    resultado = []
    while not pilha.pilhavazia():
        removido = pilha.retirar()
        resultado.append(removido)
        print(
            f"  retirar() retornou: '{removido}' | Elementos restantes: {len(pilha)}")

    print(f"\nPalavra desempilhada (invertida): {''.join(resultado)}")
    print(f"pilhavazia() após desempilhar tudo -> {pilha.pilhavazia()}\n")

    # 4. Teste de tentativa de retirar de pilha vazia
    print("Tentando retirar de uma pilha vazia...")
    try:
        pilha.retirar()
    except IndexError as erro:
        print(f"Exceção capturada com sucesso: {erro}")
