'''
single linked lists

'''


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class SinglyLinkedList:
    def __init__(self):
        self.cabeca = None

    def adicionar_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def adicionar_fim(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
            return

        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no

    def inserir_na_posicao(self, posicao, valor):
        if posicao == 0:
            self.adicionar_inicio(valor)
            return

        novo_no = No(valor)
        atual = self.cabeca

        # Avança até o nó imediatamente anterior à posição desejada
        for _ in range(posicao - 1):
            if atual is None:
                raise IndexError("Posição fora dos limites da lista.")
            atual = atual.proximo

        if atual is None:
            raise IndexError("Posição fora dos limites da lista.")

        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

    def remover_valor(self, alvo):
        atual = self.cabeca
        anterior = None

        while atual is not None and atual.valor != alvo:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            return False  # Valor não encontrado

        if anterior is None:
            self.cabeca = atual.proximo  # Remove o primeiro nó
        else:
            anterior.proximo = atual.proximo  # Pula o nó removido
        return True

    def __len__(self):
        contador = 0
        atual = self.cabeca
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador

    def __str__(self):
        valores = []
        atual = self.cabeca
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(valores) + " -> None"


# --- Exemplo de execução ---
lista = SinglyLinkedList()

lista.adicionar_fim("A")
lista.adicionar_fim("C")
lista.adicionar_inicio("Início")
lista.inserir_na_posicao(2, "B")

print("Lista atual:", lista)
print("Tamanho:", len(lista))

lista.remover_valor("C")
print("Após remover 'C':", lista)
