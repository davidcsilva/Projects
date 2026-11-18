'''
Circular Queue
'''


class CircularQueue:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.frente = 0
        self.fim = -1
        self.tamanho = 0

    def is_empty(self):
        return self.tamanho == 0

    def is_full(self):
        return self.tamanho == self.capacidade

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("A fila circular está cheia.")

        # Avança o ponteiro 'fim' circularmente
        self.fim = (self.fim + 1) % self.capacidade
        self.fila[self.fim] = item
        self.tamanho += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila circular está vazia.")

        item = self.fila[self.frente]
        self.fila[self.frente] = None  # Limpa a referência (opcional)

        # Avança o ponteiro 'frente' circularmente
        self.frente = (self.frente + 1) % self.capacidade
        self.tamanho -= 1
        return item

    def front(self):
        if self.is_empty():
            raise IndexError("A fila circular está vazia.")
        return self.fila[self.frente]

    def __str__(self):
        if self.is_empty():
            return "Fila vazia"

        elementos = []
        for i in range(self.tamanho):
            indice = (self.frente + i) % self.capacidade
            elementos.append(str(self.fila[indice]))
        return f"Frente <- [{' -> '.join(elementos)}] <- Fim (Array interno: {self.fila})"


# --- Exemplo de execução ---
cq = CircularQueue(capacidade=4)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
print(cq)

print("Removido:", cq.dequeue())  # Remove 10 (libera índice 0)
print("Removido:", cq.dequeue())  # Remove 20 (libera índice 1)

# Os novos itens dão a volta e ocupam os índices 0 e 1 liberados
cq.enqueue(50)
cq.enqueue(60)
print(cq)
