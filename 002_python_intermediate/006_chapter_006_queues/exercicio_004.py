'''
Dequeu
'''


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Fila:
    def __init__(self):
        self.frente = None
        self.fim = None

    def enqueue(self, dado):
        novo = No(dado)
        if not self.fim:
            self.frente = self.fim = novo
            return
        self.fim.proximo = novo
        self.fim = novo

    def dequeue(self):
        if self.frente is None:
            raise IndexError(
                "Erro: Não é possível fazer dequeue em uma fila vazia.")

        valor_removido = self.frente.dado
        self.frente = self.frente.proximo

        # Se a fila ficou vazia após a remoção, zera também o ponteiro 'fim'
        if self.frente is None:
            self.fim = None

        return valor_removido


# Exemplo de uso
f = Fila()
f.enqueue("A")
f.enqueue("B")

print(f.dequeue())  # Saída: A
print(f.dequeue())  # Saída: B
