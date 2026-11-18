'''
Double-Ended Queue
'''


class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class Deque:
    def __init__(self):
        self.frente = None
        self.fim = None
        self._tamanho = 0

    def is_empty(self):
        return self._tamanho == 0

    def append_left(self, valor):
        novo_no = No(valor)
        if self.is_empty():
            self.frente = self.fim = novo_no
        else:
            novo_no.proximo = self.frente
            self.frente.anterior = novo_no
            self.frente = novo_no
        self._tamanho += 1

    def append_right(self, valor):
        novo_no = No(valor)
        if self.is_empty():
            self.frente = self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no
        self._tamanho += 1

    def pop_left(self):
        if self.is_empty():
            raise IndexError("Deque vazio.")
        valor = self.frente.valor
        self.frente = self.frente.proximo
        if self.frente is None:
            self.fim = None
        else:
            self.frente.anterior = None
        self._tamanho -= 1
        return valor

    def pop_right(self):
        if self.is_empty():
            raise IndexError("Deque vazio.")
        valor = self.fim.valor
        self.fim = self.fim.anterior
        if self.fim is None:
            self.frente = None
        else:
            self.fim.proximo = None
        self._tamanho -= 1
        return valor

    def __str__(self):
        elementos = []
        atual = self.frente
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        return f"Frente <-> [{' <-> '.join(elementos)}] <-> Fim"


# --- Exemplo de execução ---
dq = Deque()

dq.append_right(10)
dq.append_right(20)
dq.append_left(5)
dq.append_left(1)
print(dq)  # Frente <-> [1 <-> 5 <-> 10 <-> 20] <-> Fim

print("Removido da frente:", dq.pop_left())  # 1
print("Removido do fim:", dq.pop_right())    # 20
print(dq)  # Frente <-> [5 <-> 10] <-> Fim
