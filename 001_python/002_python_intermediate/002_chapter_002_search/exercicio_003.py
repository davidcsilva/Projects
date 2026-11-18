'''
hashing search
'''


class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        # Cria uma lista de "baldes" (buckets) vazios para lidar com colisões (encadeamento)
        self.tabela = [[] for _ in range(self.tamanho)]

    def _funcao_hash(self, chave):
        # Converte a chave em um índice válido dentro do tamanho da tabela
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._funcao_hash(chave)
        balde = self.tabela[indice]

        # Atualiza o valor caso a chave já exista no balde
        for i, (k, v) in enumerate(balde):
            if k == chave:
                balde[i] = (chave, valor)
                return

        # Caso contrário, adiciona o novo par (chave, valor)
        balde.append((chave, valor))

    def buscar(self, chave):
        indice = self._funcao_hash(chave)
        balde = self.tabela[indice]

        # Percorre apenas o balde correspondente ao índice calculado
        for k, v in balde:
            if k == chave:
                return v

        return None  # Retorna None se a chave não for encontrada


# Exemplo de uso
tabela = TabelaHash(tamanho=7)

# Inserindo elementos
tabela.inserir("Ana", 28)
tabela.inserir("Bruno", 34)
tabela.inserir("Carla", 22)
tabela.inserir("Daniel", 41)

# Realizando buscas
print("Idade de Bruno:", tabela.buscar("Bruno"))   # Saída: 34
print("Idade de Carla:", tabela.buscar("Carla"))   # Saída: 22
print("Idade de Lucas:", tabela.buscar("Lucas"))   # Saída: None
