'''
Circular Linked List

'''


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class CircularLinkedList:
    def __init__(self):
        self.cabeca = None

    def adicionar_fim(self, valor):
        novo_no = No(valor)

        # Se a lista estiver vazia, o nó aponta para si mesmo
        if self.cabeca is None:
            self.cabeca = novo_no
            novo_no.proximo = self.cabeca
            return

        # Percorre até o último nó (aquele que aponta de volta para a cabeça)
        atual = self.cabeca
        while atual.proximo != self.cabeca:
            atual = atual.proximo

        atual.proximo = novo_no
        novo_no.proximo = self.cabeca

    def adicionar_inicio(self, valor):
        novo_no = No(valor)

        if self.cabeca is None:
            self.cabeca = novo_no
            novo_no.proximo = self.cabeca
            return

        # Encontra o último nó para atualizar sua referência para a nova cabeça
        atual = self.cabeca
        while atual.proximo != self.cabeca:
            atual = atual.proximo

        novo_no.proximo = self.cabeca
        atual.proximo = novo_no
        self.cabeca = novo_no

    def remover_valor(self, alvo):
        if self.cabeca is None:
            return False

        atual = self.cabeca
        anterior = None

        while True:
            if atual.valor == alvo:
                # Caso 1: É o único nó da lista
                if atual == self.cabeca and atual.proximo == self.cabeca:
                    self.cabeca = None
                # Caso 2: O nó removido é a cabeça (com mais elementos na lista)
                elif atual == self.cabeca:
                    ultimo = self.cabeca
                    while ultimo.proximo != self.cabeca:
                        ultimo = ultimo.proximo
                    self.cabeca = atual.proximo
                    ultimo.proximo = self.cabeca
                # Caso 3: Nó intermediário ou último
                else:
                    anterior.proximo = atual.proximo
                return True

            anterior = atual
            atual = atual.proximo

            # Deu uma volta completa e não encontrou o alvo
            if atual == self.cabeca:
                break

        return False

    def exibir(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        valores = []
        atual = self.cabeca
        while True:
            valores.append(str(atual.valor))
            atual = atual.proximo
            if atual == self.cabeca:
                break

        print(" -> ".join(valores) + f" -> (volta para {self.cabeca.valor})")


# --- Exemplo de execução ---
lista = CircularLinkedList()

lista.adicionar_fim("Jogador 1")
lista.adicionar_fim("Jogador 2")
lista.adicionar_fim("Jogador 3")
lista.adicionar_inicio("Juiz")

lista.exibir()

lista.remover_valor("Jogador 2")
print("\nApós remover 'Jogador 2':")
lista.exibir()
