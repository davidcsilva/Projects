'''
Doubly Linked List
'''


class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class DoublyLinkedList:
    def __init__(self):
        self.cabeca = None  # Primeiro nó (head)
        self.cauda = None   # Último nó (tail)

    def adicionar_inicio(self, valor):
        novo_no = NoDuplo(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo_no
            return

        novo_no.proximo = self.cabeca
        self.cabeca.anterior = novo_no
        self.cabeca = novo_no

    def adicionar_fim(self, valor):
        novo_no = NoDuplo(valor)
        if self.cauda is None:
            self.cabeca = self.cauda = novo_no
            return

        novo_no.anterior = self.cauda
        self.cauda.proximo = novo_no
        self.cauda = novo_no

    def remover_valor(self, alvo):
        atual = self.cabeca

        while atual is not None and atual.valor != alvo:
            atual = atual.proximo

        if atual is None:
            return False  # Elemento não encontrado

        # Ajusta o ponteiro do nó anterior (ou da cabeça, se for o primeiro)
        if atual.anterior is not None:
            atual.anterior.proximo = atual.proximo
        else:
            self.cabeca = atual.proximo

        # Ajusta o ponteiro do próximo nó (ou da cauda, se for o último)
        if atual.proximo is not None:
            atual.proximo.anterior = atual.anterior
        else:
            self.cauda = atual.anterior

        return True

    def exibir_frente(self):
        valores = []
        atual = self.cabeca
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo
        print("Frente: None <- " + " <-> ".join(valores) + " -> None")

    def exibir_tras(self):
        valores = []
        atual = self.cauda
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.anterior
        print("Trás:   None <- " + " <-> ".join(valores) + " -> None")


# --- Exemplo de execução ---
lista = DoublyLinkedList()

lista.adicionar_fim(10)
lista.adicionar_fim(20)
lista.adicionar_fim(30)
lista.adicionar_inicio(5)

lista.exibir_frente()
lista.exibir_tras()

lista.remover_valor(20)
print("\nApós remover o 20:")
lista.exibir_frente()
lista.exibir_tras()
