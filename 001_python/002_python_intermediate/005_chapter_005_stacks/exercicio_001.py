'''
Stacks (Pilhas)
O que é? É uma estrutura de dados que segue o princípio LIFO (Last In, First Out), ou seja, o último item a entrar é o primeiro a sair.
'''


class Stack:
    def __init__(self):
        self._itens = []

    def is_empty(self):
        return len(self._itens) == 0

    def push(self, item):
        self._itens.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia (Stack Underflow).")
        return self._itens.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia.")
        return self._itens[-1]

    def __len__(self):
        return len(self._itens)

    def __str__(self):
        return f"Base -> {self._itens} <- Topo"


# --- Exemplo de uso ---
pilha = Stack()

pilha.push("Página A")
pilha.push("Página B")
pilha.push("Página C")

# Base -> ['Página A', 'Página B', 'Página C'] <- Topo
print(pilha)
print("Topo atual:", pilha.peek())  # Página C

removido = pilha.pop()
print("Voltar de:", removido)  # Página C
print("Topo agora:", pilha.peek())  # Página B
