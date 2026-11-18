'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.6

Enunciado:
Determinar atributos e operações que possam ser de interesse para os seguintes
objetos, partindo do princípio que vão ser os elementos de uma loja de presentes:
1. Um livro
2. Um disco
3. Um gravador de vídeo
4. Uma fita de vídeo
5. Uma televisão
6. Um rádio
7. Uma torradeira
8. Uma cadeia de música
9. Uma calculadora
10. Um telefone celular (móvel)
'''

from abc import ABC
from dataclasses import dataclass, field


# ==============================================================================
# CLASSE BASE COMUM A TODOS OS ITENS DA LOJA DE PRESENTES
# ==============================================================================

@dataclass
class ProdutoLojaPresentes(ABC):
    """
    Classe base que encapsula os atributos e comportamentos comuns
    de qualquer item comercializado em uma loja de presentes.
    """
    codigo_sku: str
    nome: str
    preco: float
    estoque: int
    marca: str
    embalado_para_presente: bool = False
    mensagem_cartao: str = ""

    def aplicar_desconto(self, percentual: float) -> None:
        """Aplica desconto promocional sobre o preço."""
        if 0 < percentual < 100:
            self.preco *= (1 - percentual / 100)

    def embalar_presente(self, mensagem: str = "") -> None:
        """Serviço típico de loja de presentes: embrulho e cartão cortesia."""
        self.embalado_para_presente = True
        self.mensagem_cartao = mensagem
        print(f"Produto '{self.nome}' embalado para presente com cartão: '{mensagem}'")

    def dar_baixa_estoque(self, quantidade: int = 1) -> bool:
        """Reduz a quantidade de itens no inventário da loja."""
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        return False

    def exibir_ficha_comercial(self) -> None:
        embrulho = "Sim" if self.embalado_para_presente else "Não"
        print(f"[{self.codigo_sku}] {self.nome} ({self.marca}) | Preço: R$ {self.preco:.2f} | Estoque: {self.estoque} | Embalagem de Presente: {embrulho}")


# ==============================================================================
# 1. LIVRO
# ==============================================================================
@dataclass
class Livro(ProdutoLojaPresentes):
    autor: str = ""
    editora: str = ""
    isbn: str = ""
    numero_paginas: int = 0
    genero: str = ""

    def obter_sinopse(self) -> str:
        return f"Livro '{self.nome}' de {self.autor}, gênero {self.genero}."


# ==============================================================================
# 2. DISCO (CD / Vinil)
# ==============================================================================
@dataclass
class Disco(ProdutoLojaPresentes):
    artista: str = ""
    formato: str = "Vinil"  # Vinil ou CD
    numero_faixas: int = 0
    genero_musical: str = ""

    def tocar_amostra(self) -> None:
        print(f"Tocando prévia do disco '{self.nome}' do artista {self.artista}...")


# ==============================================================================
# 3. GRAVADOR DE VÍDEO
# ==============================================================================
@dataclass
class GravadorVideo(ProdutoLojaPresentes):
    tipo_midia: str = "VHS"
    voltagem: str = "Bivolt"
    tem_controle_remoto: bool = True

    def testar_gravacao(self) -> None:
        print(f"Testando gravação do aparelho {self.nome}...")


# ==============================================================================
# 4. FITA DE VÍDEO
# ==============================================================================
@dataclass
class FitaVideo(ProdutoLojaPresentes):
    duracao_minutos: int = 120
    formato: str = "VHS"
    virgem: bool = False

    def rebobinar(self) -> None:
        print(f"Rebobinando a fita de vídeo '{self.nome}' ({self.duracao_minutos} min)...")


# ==============================================================================
# 5. TELEVISÃO
# ==============================================================================
@dataclass
class Televisao(ProdutoLojaPresentes):
    polegadas: int = 50
    resolucao: str = "4K Ultra HD"
    smart_tv: bool = True
    voltagem: str = "Bivolt"

    def demonstrar_imagem(self) -> None:
        print(f"Exibindo demonstração de cores na TV {self.nome} ({self.polegadas}\" {self.resolucao}).")


# ==============================================================================
# 6. RÁDIO
# ==============================================================================
@dataclass
class Radio(ProdutoLojaPresentes):
    faixas: str = "AM/FM"
    alimentacao: str = "Pilha/Bateria"
    tem_bluetooth: bool = True

    def sintonizar_estacao(self, estacao: str) -> None:
        print(f"Sintonizando rádio na frequência {estacao}.")


# ==============================================================================
# 7. TORRADEIRA
# ==============================================================================
@dataclass
class Torradeira(ProdutoLojaPresentes):
    fatias: int = 2
    niveis_tostagem: int = 7
    potencia_watts: int = 800
    material: str = "Aço Inox"

    def demonstrar_tostagem(self, nivel: int) -> None:
        print(f"Demonstrando ciclo da torradeira no nível {nivel} ({self.fatias} fatias).")


# ==============================================================================
# 8. CADEIA DE MÚSICA (Aparelho de Som / Mini System)
# ==============================================================================
@dataclass
class CadeiaDeMusica(ProdutoLojaPresentes):
    potencia_rms_watts: int = 300
    entradas: list[str] = field(default_factory=lambda: ["Bluetooth", "USB", "CD", "Auxiliar"])
    numero_caixas: int = 2

    def parear_bluetooth(self, dispositivo: str) -> None:
        print(f"Pareando som '{self.nome}' com o dispositivo {dispositivo}.")


# ==============================================================================
# 9. CALCULADORA
# ==============================================================================
@dataclass
class Calculadora(ProdutoLojaPresentes):
    tipo: str = "Científica"  # Básica, Científica ou Financeira
    alimentacao: str = "Solar/Bateria"
    digitos_display: int = 12

    def calcular(self, expressao: str) -> str:
        return f"Calculando {expressao} no display de {self.digitos_display} dígitos."


# ==============================================================================
# 10. TELEFONE CELULAR (MÓVEL)
# ==============================================================================
@dataclass
class TelefoneCelular(ProdutoLojaPresentes):
    modelo: str = ""
    armazenamento_gb: int = 256
    memoria_ram_gb: int = 8
    camera_megapixels: int = 50
    suporte_5g: bool = True

    def realizar_chamada_teste(self, destino: str) -> None:
        print(f"Disparando chamada de teste de {self.modelo} para {destino}.")


# ==============================================================================
# Demonstração Prática na Loja de Presentes
# ==============================================================================
if __name__ == "__main__":
    print("=== Vitrine da Loja de Presentes ===\n")

    livro = Livro(
        codigo_sku="LIV-001",
        nome="O Senhor dos Anéis",
        preco=89.90,
        estoque=15,
        marca="HarperCollins",
        autor="J.R.R. Tolkien",
        editora="HarperCollins",
        isbn="978-8595084759",
        numero_paginas=1200,
        genero="Fantasia"
    )

    celular = TelefoneCelular(
        codigo_sku="CEL-999",
        nome="Galaxy S25 Ultra",
        preco=6999.00,
        estoque=5,
        marca="Samsung",
        modelo="SM-S928B",
        armazenamento_gb=512,
        memoria_ram_gb=12
    )

    torradeira = Torradeira(
        codigo_sku="ELET-01",
        nome="Torradeira Vintage Retrô",
        preco=249.90,
        estoque=8,
        marca="Oster",
        fatias=2,
        material="Aço Escovado Vermelho"
    )

    # Aplicação de operações comuns de Loja de Presentes
    livro.embalar_presente(mensagem="Feliz Aniversário, meu amigo!")
    livro.exibir_ficha_comercial()

    print()
    celular.aplicar_desconto(10)  # Desconto de 10%
    celular.embalar_presente(mensagem="Com carinho para você!")
    celular.exibir_ficha_comercial()

    print()
    torradeira.exibir_ficha_comercial()
