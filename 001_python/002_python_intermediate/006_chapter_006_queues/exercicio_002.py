'''
Priority Queue
'''

import heapq


class PriorityQueue:
    def __init__(self):
        self._fila = []
        # Usado como critério de desempate (ordem de chegada)
        self._contador = 0

    def is_empty(self):
        return len(self._fila) == 0

    def enqueue(self, item, prioridade):
        # Armazena uma tupla: (prioridade, ordem_chegada, item)
        # O contador evita erro caso dois itens tenham a mesma prioridade e não sejam comparáveis
        heapq.heappush(self._fila, (prioridade, self._contador, item))
        self._contador += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila de prioridade está vazia.")
        # Remove e retorna o item com o menor número de prioridade
        return heapq.heappop(self._fila)[2]

    def peek(self):
        if self.is_empty():
            raise IndexError("A fila de prioridade está vazia.")
        return self._fila[0][2]

    def __len__(self):
        return len(self._fila)


# --- Exemplo de uso: Triagem Hospitalar ---
triagem = PriorityQueue()

triagem.enqueue("Paciente A (Dor de cabeça)", prioridade=3)
triagem.enqueue("Paciente B (Fratura exposta)", prioridade=1)
triagem.enqueue("Paciente C (Febre alta)", prioridade=2)
triagem.enqueue("Paciente D (Gripe leve)", prioridade=3)

print("Próximo a ser atendido:", triagem.peek())  # Paciente B

while not triagem.is_empty():
    print("Atendendo:", triagem.dequeue())
