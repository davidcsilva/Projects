'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.3

Enunciado:
Definir os seguintes termos:
a) classe
b) objeto
c) sessão de declaração
d) sessão de implementação
e) variável de instância
f) função membro
g) membro dado
h) construtor
i) instância de uma classe
j) métodos ou serviços
k) sobrecarga
l) interface
'''

from abc import ABC, abstractmethod
from typing import overload


# ==============================================================================
# l) Interface
# ==============================================================================
# Contrato que especifica QUAIS operações uma classe deve disponibilizar,
# sem definir COMO essas operações são implementadas.

class DispositivoEletronico(ABC):
    """Interface abstrata para dispositivos eletrônicos."""

    @abstractmethod
    def ligar(self) -> None:
        """Contrato: deve implementar a inicialização do dispositivo."""
        pass

    @abstractmethod
    def desligar(self) -> None:
        """Contrato: deve implementar o desligamento do dispositivo."""
        pass


# ==============================================================================
# a) Classe | c) Seção de Declaração | d) Seção de Implementação
# ==============================================================================
# Classe: Modelo/molde conceitual para criar objetos com estado e comportamento.
# Seção de Declaração: Especifica os atributos e assinaturas dos métodos.
# Seção de Implementação: O código executável que dá corpo aos métodos.

class Televisao(DispositivoEletronico):
    """
    Representa uma Televisão que implementa a interface DispositivoEletronico.
    """

    # --------------------------------------------------------------------------
    # h) Construtor
    # --------------------------------------------------------------------------
    # Operação especial invocada na criação do objeto para inicializar o estado.
    def __init__(self, marca: str, tamanho_polegadas: int) -> None:
        # ----------------------------------------------------------------------
        # g) Membro Dado / e) Variável de Instância
        # ----------------------------------------------------------------------
        # Atributos pertencentes a cada instância específica na memória.
        self.marca: str = marca                          # Membro dado
        self.tamanho_polegadas: int = tamanho_polegadas  # Membro dado
        self.ligada: bool = False                        # Variável de instância
        self.canal_atual: int = 1                        # Variável de instância
        self.volume: int = 15                            # Variável de instância

    # --------------------------------------------------------------------------
    # f) Função Membro / j) Métodos ou Serviços
    # --------------------------------------------------------------------------
    # Comportamentos e operações que o objeto oferece ao mundo externo.

    def ligar(self) -> None:
        """Serviço: liga a televisão."""
        self.ligada = True
        print(f"[{self.marca}] TV ligada no canal {self.canal_atual}.")

    def desligar(self) -> None:
        """Serviço: desliga a televisão."""
        self.ligada = False
        print(f"[{self.marca}] TV desligada.")

    def alterar_volume(self, delta: int) -> None:
        """Função membro que manipula o membro dado 'volume'."""
        if not self.ligada:
            print(
                f"[{self.marca}] Não é possível alterar volume com a TV desligada.")
            return
        self.volume = max(0, min(100, self.volume + delta))
        print(f"[{self.marca}] Volume atual: {self.volume}")

    # --------------------------------------------------------------------------
    # k) Sobrecarga (Overloading)
    # --------------------------------------------------------------------------
    # Em linguagens estáticas (ex.: C++, Java), define métodos com mesmo nome e
    # assinaturas de tipos diferentes.
    # Em Python, demonstra-se via @overload para verificação de tipos e tratamento
    # flexível de argumentos:

    @overload
    def mudar_canal(self, novo_canal: int) -> None: ...

    @overload
    def mudar_canal(self, novo_canal: str) -> None: ...

    def mudar_canal(self, novo_canal: int | str) -> None:
        """Sobrecarga: aceita número inteiro do canal ou nome textual."""
        if not self.ligada:
            print(f"[{self.marca}] Ligue a TV primeiro.")
            return

        if isinstance(novo_canal, int):
            self.canal_atual = novo_canal
            print(
                f"[{self.marca}] Canal sintonizado pelo número: {self.canal_atual}")
        elif isinstance(novo_canal, str):
            canais_famosos = {"noticias": 24, "esportes": 30, "filmes": 45}
            self.canal_atual = canais_famosos.get(novo_canal.lower(), 1)
            print(
                f"[{self.marca}] Canal '{novo_canal}' mapeado para o número: {self.canal_atual}")


# ==============================================================================
# b) Objeto | i) Instância de uma Classe
# ==============================================================================
if __name__ == "__main__":
    print("=== Criação de Instâncias / Objetos Concretos ===")

    # Instanciação: tv_sala e tv_quarto são objetos distintos da classe Televisao
    tv_sala: Televisao = Televisao(marca="Sony", tamanho_polegadas=55)
    tv_quarto: Televisao = Televisao(marca="Samsung", tamanho_polegadas=32)

    # Cada instância possui seu próprio estado independente
    print(
        f"Objeto 1 (Sala): {tv_sala.marca} {tv_sala.tamanho_polegadas}\" - ID Memória: {hex(id(tv_sala))}")
    print(
        f"Objeto 2 (Quarto): {tv_quarto.marca} {tv_quarto.tamanho_polegadas}\" - ID Memória: {hex(id(tv_quarto))}")

    print("\n=== Executando Métodos / Serviços ===")
    tv_sala.ligar()
    tv_sala.alterar_volume(5)

    print("\n=== Demonstração de Sobrecarga de Métodos ===")
    tv_sala.mudar_canal(12)              # Chamada com int
    # Chamada com str (sobrecarga simulada)
    tv_sala.mudar_canal("esportes")

    print("\n=== Verificação de Independência de Estado ===")
    print(f"TV da Sala está ligada? {tv_sala.ligada}")
    print(f"TV do Quarto está ligada? {tv_quarto.ligada} (não foi alterada)")
