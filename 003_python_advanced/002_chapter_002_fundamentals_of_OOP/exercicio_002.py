'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.2

Enunciado:
Quais seriam os objetos que devem ser considerados nos seguintes sistemas?
a) Um programa para editar uma revista.
b) Um atendente de telefone.
c) Um sistema de controle de elevadores.
d) Um sistema de assinaturas de uma revista.
'''

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum, auto


# ==============================================================================
# a) Um programa para editar uma revista
# ==============================================================================
# Objetos a considerar:
# - Revista / Edição (contêiner geral das publicações)
# - Pagina (unidade de diagramação, margens, dimensões)
# - Artigo / Matéria (título, autor, conteúdo editorial)
# - Elementos visuais/layout: CaixaDeTexto, Imagem, Anuncio
# - Autor / Jornalista (dados do criador do conteúdo)
# - EstiloTipografico (fontes, tamanhos, cores)

@dataclass
class CaixaDeTexto:
    pos_x: float
    pos_y: float
    largura: float
    altura: float
    conteudo: str
    fonte: str = "Arial"
    tamanho_fonte: int = 12


@dataclass
class Imagem:
    arquivo_origem: str
    largura: float
    altura: float
    legenda: str
    credito_fotografo: str


@dataclass
class Pagina:
    numero: int
    elementos: list[object] = field(default_factory=list)

    def adicionar_elemento(self, elemento: object) -> None:
        self.elementos.append(elemento)


@dataclass
class EdicaoRevista:
    numero_edicao: int
    titulo: str
    data_publicacao: date
    paginas: list[Pagina] = field(default_factory=list)


# ==============================================================================
# b) Um atendente de telefone (URA / Central Telefônica / Secretária Eletrônica)
# ==============================================================================
# Objetos a considerar:
# - Chamada (origem, destino, timestamp, status)
# - LinhaTelefonica (canal físico/virtual, status: ocupado/livre)
# - MenuAtendimento / URA (áudio explicativo, opções de navegação)
# - OpcaoMenu (dígito discado, ação/redirecionamento)
# - MensagemVoz (áudio gravado caso não haja atendimento humano)
# - Ramal / Operador (atendente humano e canal de transferência)
# - FilaDeEspera (chamadas aguardando atendimento)

class StatusChamada(Enum):
    CHAMANDO = auto()
    EM_ANDAMENTO = auto()
    EM_ESPERA = auto()
    ENCERRADA = auto()


@dataclass
class Chamada:
    id_chamada: str
    numero_origem: str
    numero_destino: str
    inicio: datetime = field(default_factory=datetime.now)
    status: StatusChamada = StatusChamada.CHAMANDO


@dataclass
class OpcaoMenu:
    digito: str
    descricao: str
    ramal_destino: str


@dataclass
class MenuAtendimento:
    mensagem_saudacao: str
    opcoes: dict[str, OpcaoMenu] = field(default_factory=dict)


@dataclass
class MensagemVoz:
    chamada_id: str
    audio_url: str
    duracao_segundos: int
    gravado_em: datetime = field(default_factory=datetime.now)
    ouvida: bool = False


# ==============================================================================
# c) Um sistema de controle de elevadores
# ==============================================================================
# Objetos a considerar:
# - Elevador / Cabine (andar atual, direção, capacidade, peso atual)
# - Porta (status: aberta, fechando, fechada; sensor anti-esmagamento)
# - Motor / SistemaTracao (velocidade, aceleração, frenagem)
# - Andar (identificador/número do pavimento)
# - Botoeira / Botao (botões internos de destino e botões de chamada no andar)
# - Requisicao / Chamado (andar de origem, direção solicitada, prioridade)
# - DespachanteElevador / ControladorCentral (algoritmo de alocação de tráfego)

class DirecaoElevador(Enum):
    SUBINDO = auto()
    DESCENDO = auto()
    PARADO = auto()


class EstadoPorta(Enum):
    ABERTA = auto()
    FECHADA = auto()
    ABRINDO = auto()
    FECHANDO = auto()


@dataclass
class Porta:
    estado: EstadoPorta = EstadoPorta.FECHADA
    obstruida: bool = False


@dataclass
class Requisicao:
    andar: int
    direcao: DirecaoElevador
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class Elevador:
    id_elevador: int
    andar_atual: int = 0
    direcao: DirecaoElevador = DirecaoElevador.PARADO
    capacidade_kg: float = 600.0
    peso_atual_kg: float = 0.0
    porta: Porta = field(default_factory=Porta)
    chamadas_internas: set[int] = field(default_factory=set)


@dataclass
class ControladorElevadores:
    elevadores: list[Elevador]
    requisicoes_pendentes: list[Requisicao] = field(default_factory=list)

    def despachar_chamada(self, requisicao: Requisicao) -> Elevador:
        """Seleciona o elevador mais adequado para atender a solicitação."""
        # Heurística simplificada de proximidade:
        melhor_elevador = min(
            self.elevadores,
            key=lambda e: abs(e.andar_atual - requisicao.andar)
        )
        melhor_elevador.chamadas_internas.add(requisicao.andar)
        return melhor_elevador


# ==============================================================================
# d) Um sistema de assinaturas de uma revista
# ==============================================================================
# Objetos a considerar:
# - Assinante / Cliente (dados pessoais, endereço de entrega, contato)
# - PlanoAssinatura (nome, preço, periodicidade, tipo: impresso, digital)
# - Assinatura (contrato ativo, data_inicio, data_termino, status)
# - Fatura / Pagamento (valor, vencimento, método de pagamento, status)
# - MetodoPagamento (cartão, boleto, pix)
# - OrdemEntrega / Remessa (gerada para cada nova edição impressa enviada)
# - EdicaoRevista (o item físico/digital a ser entregue ou disponibilizado)

class StatusAssinatura(Enum):
    ATIVA = auto()
    PENDENTE = auto()
    SUSPENSA = auto()
    CANCELADA = auto()


@dataclass
class Assinante:
    id_cliente: str
    nome: str
    email: str
    endereco_entrega: str


@dataclass
class PlanoAssinatura:
    id_plano: str
    nome: str
    preco_mensal: float
    inclui_impresso: bool = True
    inclui_digital: bool = True


@dataclass
class Pagamento:
    id_pagamento: str
    valor: float
    data_vencimento: date
    pago: bool = False


@dataclass
class Assinatura:
    id_assinatura: str
    assinante: Assinante
    plano: PlanoAssinatura
    data_inicio: date
    data_renovacao: date
    status: StatusAssinatura = StatusAssinatura.ATIVA
    faturas: list[Pagamento] = field(default_factory=list)


@dataclass
class OrdemEntrega:
    id_remessa: str
    assinante: Assinante
    edicao_id: int
    codigo_rastreio: str
    enviado_em: date
    entregue: bool = False


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    print("=== a) Edição de Revista ===")
    edicao = EdicaoRevista(42, "Tech Insights", date.today())
    p1 = Pagina(1)
    p1.adicionar_elemento(CaixaDeTexto(
        10, 20, 200, 50, "Inteligência Artificial em 2026"))
    p1.adicionar_elemento(
        Imagem("capa.jpg", 400, 300, "Robô futurista", "João Fotógrafo"))
    edicao.paginas.append(p1)
    print(
        f"Revista '{edicao.titulo}' - Edição #{edicao.numero_edicao} com {len(edicao.paginas)} página(s).")

    print("\n=== b) Atendente de Telefone ===")
    menu = MenuAtendimento(
        mensagem_saudacao="Olá! Pressione 1 para Suporte ou 2 para Vendas.",
        opcoes={
            "1": OpcaoMenu("1", "Suporte Técnico", "RAMAL-101"),
            "2": OpcaoMenu("2", "Equipe de Vendas", "RAMAL-102")
        }
    )
    chamada = Chamada("CH-001", "11988887777", "0800-123456")
    print(
        f"Chamada {chamada.id_chamada} de {chamada.numero_origem} recebida no menu com {len(menu.opcoes)} opções.")

    print("\n=== c) Controle de Elevadores ===")
    e1 = Elevador(id_elevador=1, andar_atual=0)
    e2 = Elevador(id_elevador=2, andar_atual=8)
    controlador = ControladorElevadores(elevadores=[e1, e2])
    chamado_andar_3 = Requisicao(andar=3, direcao=DirecaoElevador.SUBINDO)
    atendido_por = controlador.despachar_chamada(chamado_andar_3)
    print(
        f"Chamada no 3º andar despachada para o Elevador #{atendido_por.id_elevador} (estava no andar {atendido_por.andar_atual}).")

    print("\n=== d) Sistema de Assinaturas ===")
    cliente = Assinante("CLI-1", "Carlos Silva",
                        "carlos@email.com", "Rua das Flores, 123")
    plano_anual = PlanoAssinatura(
        "PLN-01", "Plano Anual Premium", 29.90, True, True)
    assinatura = Assinatura("ASS-99", cliente, plano_anual,
                            date(2026, 1, 1), date(2027, 1, 1))
    print(
        f"Assinatura {assinatura.id_assinatura} ativada para {cliente.nome} ({plano_anual.nome}).")
