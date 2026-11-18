"""
Capítulo 04 - Associação, Generalização e Herança
Exercício 17.3

Enunciado:
17.3 Projete uma hierarquia de classe que utilize como classe base ou raiz uma classe LAN (rede de área local).
As subclasses derivadas devem representar diferentes topologias como estrela, anel, barramento e hub.
Os membros dados devem representar propriedades, tais como suporte de transmissão, controle de acesso,
formato do referencial de dados, padrões, velocidade de transmissão etc. Desejamos simular a atividade
dos nós da LAN.
A rede consta de nós, que podem ser dispositivos, tais como computadores pessoais, estações de trabalho,
máquinas de Fax etc. Uma tarefa principal da LAN é suportar comunicações de dados entre seus nós. O usuário
do processo de simulação deve, no mínimo, poder:
• Enumerar os nós atuais da rede LAN.
• Somar um novo nó na rede LAN.
• Retirar um nó da rede LAN.
• Configurar a rede, proporcionando uma topologia de estrela ou barramento.
• Especificar o tamanho do pacote, que é o tamanho em bytes da mensagem que vai de um nó a outro.
• Enviar um pacote de um nó específico a outro.
• Difundir um pacote do nó a todos os demais da rede.
• Efetuar estatísticas da LAN, tais como tempo médio que emprega um pacote.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import random
import time
from typing import Any, Iterator


# ==============================================================================
# ESTRUTURA DO PACOTE DE DADOS / QUADRO
# ==============================================================================

@dataclass
class Pacote:
    """
    Representa a unidade de dados (PDU / Quadro / Pacote) transmitida pela LAN.

    Atributos:
        id_pacote: Identificador único da mensagem.
        origem_id: ID do nó remetente.
        destino_id: ID do nó destinatário (ou 'BROADCAST').
        tamanho_bytes: Tamanho do pacote em bytes (payload + cabeçalho).
        conteudo: Carga útil (dados transmitidos).
        tempo_transito_ms: Tempo decorrido de trânsito em milissegundos.
        rota: Lista de nós e dispositivos intermediários percorridos.
        sucesso: Indica se a entrega foi concluída.
    """
    id_pacote: str
    origem_id: str
    destino_id: str
    tamanho_bytes: int
    conteudo: str = ""
    tempo_transito_ms: float = 0.0
    rota: list[str] = field(default_factory=list)
    sucesso: bool = False

    @property
    def is_broadcast(self) -> bool:
        return self.destino_id.upper() == "BROADCAST"

    def __str__(self) -> str:
        dest = "TODOS (Broadcast)" if self.is_broadcast else self.destino_id
        return (
            f"Pacote [{self.id_pacote}] {self.origem_id} -> {dest} "
            f"({self.tamanho_bytes} B, {self.tempo_transito_ms:.4f} ms)"
        )


# ==============================================================================
# HIERARQUIA 1: NÓS E DISPOSITIVOS DA REDE (GENERALIZAÇÃO)
# ==============================================================================

class No(ABC):
    """
    Classe base abstrata para todos os dispositivos conectados à rede LAN.
    """

    def __init__(self, id_no: str, nome: str, mac: str, ip: str) -> None:
        self.id_no = id_no.strip().upper()
        self.nome = nome.strip()
        self.mac = mac.strip().upper()
        self.ip = ip.strip()
        self.ativo: bool = True
        self.buffer_recebimento: list[Pacote] = []

    def receber_pacote(self, pacote: Pacote) -> None:
        """Processa a chegada de um pacote direcionado a este nó ou broadcast."""
        if not self.ativo:
            return
        self.buffer_recebimento.append(pacote)

    @property
    @abstractmethod
    def tipo_dispositivo(self) -> str:
        """Identifica a categoria do nó na rede."""

    @property
    @abstractmethod
    def taxa_processamento_ms(self) -> float:
        """Tempo em ms que a placa de rede do dispositivo consome para processar um frame."""

    def limpar_buffer(self) -> None:
        self.buffer_recebimento.clear()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id_no!r}, nome={self.nome!r}, ip={self.ip!r})"

    def __str__(self) -> str:
        status = "Online" if self.ativo else "Offline"
        return f"[{self.id_no}] {self.nome} ({self.tipo_dispositivo}) - IP: {self.ip} | MAC: {self.mac} [{status}]"


class ComputadorPessoal(No):
    """Representa um computador de mesa ou notebook comum de usuário."""

    @property
    def tipo_dispositivo(self) -> str:
        return "Computador Pessoal (PC)"

    @property
    def taxa_processamento_ms(self) -> float:
        return 0.05


class EstacaoTrabalho(No):
    """Representa uma workstation de alta capacidade (desenvolvimento / CAD)."""

    @property
    def tipo_dispositivo(self) -> str:
        return "Estação de Trabalho (Workstation)"

    @property
    def taxa_processamento_ms(self) -> float:
        return 0.02


class Servidor(No):
    """Representa um servidor corporativo de dados / aplicação."""

    @property
    def tipo_dispositivo(self) -> str:
        return "Servidor Corporativo"

    @property
    def taxa_processamento_ms(self) -> float:
        return 0.01


class MaquinaFax(No):
    """Representa um aparelho de Fax conectado à rede LAN por adaptador."""

    @property
    def tipo_dispositivo(self) -> str:
        return "Máquina de Fax"

    @property
    def taxa_processamento_ms(self) -> float:
        return 0.20


class ImpressoraRede(No):
    """Representa uma impressora de rede departamental."""

    @property
    def tipo_dispositivo(self) -> str:
        return "Impressora de Rede"

    @property
    def taxa_processamento_ms(self) -> float:
        return 0.10


# ==============================================================================
# HIERARQUIA 2: CLASSE BASE LAN E SUBCLASSES DE TOPOLOGIAS
# ==============================================================================

class LAN(ABC):
    """
    Classe base / raiz para Redes de Área Local (LAN).
    Define propriedades físicas e lógicas de comunicação, coleção de nós
    e métodos de envio, broadcast e estatísticas.
    """

    def __init__(
        self,
        nome: str,
        suporte_transmissao: str,
        controle_acesso: str,
        formato_quadro: str,
        padrao: str,
        velocidade_mbps: float,
        tamanho_pacote_padrao: int = 1500,
    ) -> None:
        self.nome = nome.strip()
        self.suporte_transmissao = suporte_transmissao.strip()
        self.controle_acesso = controle_acesso.strip()
        self.formato_quadro = formato_quadro.strip()
        self.padrao = padrao.strip()
        self.velocidade_mbps = float(velocidade_mbps)
        self.tamanho_pacote_padrao = int(tamanho_pacote_padrao)

        self.nos: dict[str, No] = {}
        self.historico_pacotes: list[Pacote] = []
        self._contador_pacotes: int = 0

    @property
    @abstractmethod
    def topologia(self) -> str:
        """Nome textual da topologia implementada."""

    @abstractmethod
    def simular_envio_unicast(self, pacote: Pacote) -> Pacote:
        """Encaminha o pacote da origem ao destino de acordo com as regras da topologia."""

    @abstractmethod
    def simular_envio_broadcast(self, pacote_base: Pacote) -> list[Pacote]:
        """Difunde o pacote para todos os outros nós ativos da LAN."""

    # --------------------------------------------------------------------------
    # REQUISITOS OPERACIONAIS MÍNIMOS
    # --------------------------------------------------------------------------

    def enumerar_nos(self) -> list[No]:
        """
        [Requisito 1] Enumera todos os nós atualmente presentes na LAN.
        """
        return list(self.nos.values())

    def adicionar_no(self, no: No) -> None:
        """
        [Requisito 2] Soma um novo nó à rede LAN.
        """
        if no.id_no in self.nos:
            raise ValueError(
                f"O nó com ID '{no.id_no}' já existe na rede LAN.")
        self.nos[no.id_no] = no

    def retirar_no(self, id_no: str) -> No:
        """
        [Requisito 3] Retira um nó da rede LAN.
        """
        id_norm = id_no.strip().upper()
        if id_norm not in self.nos:
            raise KeyError(
                f"O nó com ID '{id_no}' não foi encontrado na rede LAN.")
        return self.nos.pop(id_norm)

    def especificar_tamanho_pacote(self, tamanho_bytes: int) -> None:
        """
        [Requisito 5] Especifica o tamanho padrão do pacote em bytes.
        """
        if tamanho_bytes <= 0:
            raise ValueError(
                "O tamanho do pacote deve ser estritamente positivo.")
        self.tamanho_pacote_padrao = int(tamanho_bytes)

    def enviar_pacote(
        self,
        origem_id: str,
        destino_id: str,
        mensagem: str = "",
        tamanho_bytes: int | None = None,
    ) -> Pacote:
        """
        [Requisito 6] Envia um pacote de um nó específico a outro (Unicast).
        """
        origem_norm = origem_id.strip().upper()
        destino_norm = destino_id.strip().upper()

        if origem_norm not in self.nos:
            raise KeyError(
                f"Nó de origem '{origem_id}' não cadastrado na LAN.")
        if destino_norm not in self.nos:
            raise KeyError(
                f"Nó de destino '{destino_id}' não cadastrado na LAN.")
        if origem_norm == destino_norm:
            raise ValueError(
                "O nó de origem não pode ser idêntico ao nó de destino.")

        tam = tamanho_bytes if tamanho_bytes is not None else self.tamanho_pacote_padrao

        self._contador_pacotes += 1
        id_pkt = f"PKT-{self._contador_pacotes:05d}"

        pacote = Pacote(
            id_pacote=id_pkt,
            origem_id=origem_norm,
            destino_id=destino_norm,
            tamanho_bytes=tam,
            conteudo=mensagem or f"Payload de dados ({tam} bytes)",
        )

        resultado = self.simular_envio_unicast(pacote)
        self.historico_pacotes.append(resultado)
        return resultado

    def difundir_pacote(
        self,
        origem_id: str,
        mensagem: str = "",
        tamanho_bytes: int | None = None,
    ) -> list[Pacote]:
        """
        [Requisito 7] Difunde um pacote do nó a todos os demais da rede (Broadcast).
        """
        origem_norm = origem_id.strip().upper()
        if origem_norm not in self.nos:
            raise KeyError(
                f"Nó de origem '{origem_id}' não cadastrado na LAN.")

        if len(self.nos) <= 1:
            return []

        tam = tamanho_bytes if tamanho_bytes is not None else self.tamanho_pacote_padrao

        self._contador_pacotes += 1
        id_pkt = f"BCAST-{self._contador_pacotes:05d}"

        pacote_base = Pacote(
            id_pacote=id_pkt,
            origem_id=origem_norm,
            destino_id="BROADCAST",
            tamanho_bytes=tam,
            conteudo=mensagem or f"Broadcast ({tam} bytes)",
        )

        pacotes_entregues = self.simular_envio_broadcast(pacote_base)
        self.historico_pacotes.extend(pacotes_entregues)
        return pacotes_entregues

    def obter_estatisticas(self) -> dict[str, Any]:
        """
        [Requisito 8] Efetua estatísticas da LAN, tais como tempo médio de pacote.
        """
        total_pacotes = len(self.historico_pacotes)
        if total_pacotes == 0:
            return {
                "total_pacotes": 0,
                "pacotes_sucesso": 0,
                "taxa_sucesso_pct": 0.0,
                "total_bytes": 0,
                "tempo_medio_ms": 0.0,
                "tempo_minimo_ms": 0.0,
                "tempo_maximo_ms": 0.0,
                "velocidade_mbps": self.velocidade_mbps,
                "topologia": self.topologia,
            }

        sucessos = [p for p in self.historico_pacotes if p.sucesso]
        tempos = [p.tempo_transito_ms for p in sucessos]
        total_bytes = sum(p.tamanho_bytes for p in self.historico_pacotes)

        tempo_medio = sum(tempos) / len(tempos) if tempos else 0.0
        tempo_min = min(tempos) if tempos else 0.0
        tempo_max = max(tempos) if tempos else 0.0

        return {
            "total_pacotes": total_pacotes,
            "pacotes_sucesso": len(sucessos),
            "taxa_sucesso_pct": (len(sucessos) / total_pacotes) * 100.0,
            "total_bytes": total_bytes,
            "tempo_medio_ms": tempo_medio,
            "tempo_minimo_ms": tempo_min,
            "tempo_maximo_ms": tempo_max,
            "velocidade_mbps": self.velocidade_mbps,
            "topologia": self.topologia,
        }

    # --------------------------------------------------------------------------
    # MODELO DE LATÊNCIA FÍSICA
    # --------------------------------------------------------------------------

    def calcular_tempo_transmissao_ms(self, tamanho_bytes: int) -> float:
        """
        Calcula o atraso de transmissão (Tx Delay) puro:
        T_tx = (tamanho_bytes * 8) / (velocidade_mbps * 1_000_000) * 1000 ms
        """
        bits = tamanho_bytes * 8
        velocidade_bps = self.velocidade_mbps * 1_000_000.0
        return (bits / velocidade_bps) * 1000.0

    def __len__(self) -> int:
        return len(self.nos)

    def __iter__(self) -> Iterator[No]:
        return iter(self.nos.values())

    def __str__(self) -> str:
        return (
            f"LAN '{self.nome}' | Topologia: {self.topologia} | Velocidade: {self.velocidade_mbps} Mbps | "
            f"Padrão: {self.padrao} | Meio: {self.suporte_transmissao} | Nós: {len(self.nos)}"
        )


# ==============================================================================
# SUBCLASSES DE TOPOLOGIA
# ==============================================================================

class LANEstrela(LAN):
    """
    Topologia em Estrela (Star Topology).
    Todos os nós conectam-se a um switch central de comutação ativa.
    """

    def __init__(
        self,
        nome: str = "LAN Estrela Ethernet",
        velocidade_mbps: float = 1000.0,
        latencia_switch_ms: float = 0.005,
        tamanho_pacote_padrao: int = 1500,
    ) -> None:
        super().__init__(
            nome=nome,
            suporte_transmissao="Par Trançado UTP Cat6 / Fibra Óptica",
            controle_acesso="Comutação Full-Duplex sem Colisão",
            formato_quadro="Quadro Ethernet IEEE 802.3",
            padrao="Gigabit Ethernet (1000BASE-T)",
            velocidade_mbps=velocidade_mbps,
            tamanho_pacote_padrao=tamanho_pacote_padrao,
        )
        self.latencia_switch_ms = latencia_switch_ms

    @property
    def topologia(self) -> str:
        return "Estrela (Switch Central)"

    def simular_envio_unicast(self, pacote: Pacote) -> Pacote:
        no_origem = self.nos[pacote.origem_id]
        no_destino = self.nos[pacote.destino_id]

        # Trajeto: Origem -> Switch -> Destino
        tx_origem = self.calcular_tempo_transmissao_ms(pacote.tamanho_bytes)
        tx_destino = self.calcular_tempo_transmissao_ms(pacote.tamanho_bytes)
        proc = no_origem.taxa_processamento_ms + no_destino.taxa_processamento_ms

        tempo_total = tx_origem + self.latencia_switch_ms + tx_destino + proc
        pacote.tempo_transito_ms = tempo_total
        pacote.rota = [pacote.origem_id, "SWITCH-CENTRAL", pacote.destino_id]
        pacote.sucesso = no_destino.ativo

        if pacote.sucesso:
            no_destino.receber_pacote(pacote)

        return pacote

    def simular_envio_broadcast(self, pacote_base: Pacote) -> list[Pacote]:
        entregas: list[Pacote] = []
        no_origem = self.nos[pacote_base.origem_id]

        tx_origem = self.calcular_tempo_transmissao_ms(
            pacote_base.tamanho_bytes)
        tx_ramal = self.calcular_tempo_transmissao_ms(
            pacote_base.tamanho_bytes)

        for dest_id, no_dest in self.nos.items():
            if dest_id == pacote_base.origem_id:
                continue

            tempo = tx_origem + self.latencia_switch_ms + tx_ramal + \
                no_origem.taxa_processamento_ms + no_dest.taxa_processamento_ms

            p_copia = Pacote(
                id_pacote=f"{pacote_base.id_pacote}->{dest_id}",
                origem_id=pacote_base.origem_id,
                destino_id=dest_id,
                tamanho_bytes=pacote_base.tamanho_bytes,
                conteudo=pacote_base.conteudo,
                tempo_transito_ms=tempo,
                rota=[pacote_base.origem_id, "SWITCH-CENTRAL", dest_id],
                sucesso=no_dest.ativo,
            )
            if p_copia.sucesso:
                no_dest.receber_pacote(p_copia)
            entregas.append(p_copia)

        return entregas


class LANBarramento(LAN):
    """
    Topologia em Barramento (Bus Topology).
    Todos os nós compartilham um cabo coaxial comum com terminadores de carga.
    Utiliza CSMA/CD para acesso concorrente ao meio.
    """

    def __init__(
        self,
        nome: str = "LAN Barramento Coaxial",
        velocidade_mbps: float = 10.0,
        comprimento_cabo_metros: float = 185.0,
        tamanho_pacote_padrao: int = 1500,
    ) -> None:
        super().__init__(
            nome=nome,
            suporte_transmissao="Cabo Coaxial Fino (RG-58, 50 Ohms)",
            controle_acesso="CSMA/CD (Detecção de Portadora com Detecção de Colisão)",
            formato_quadro="Quadro IEEE 802.3 Ethernet",
            padrao="10BASE2 (Thinnet Ethernet)",
            velocidade_mbps=velocidade_mbps,
            tamanho_pacote_padrao=tamanho_pacote_padrao,
        )
        self.comprimento_cabo_metros = comprimento_cabo_metros
        self.velocidade_propagacao_m_s = 2.0e8  # 200.000 km/s no coaxial

    @property
    def topologia(self) -> str:
        return "Barramento (Bus)"

    def _tempo_propagacao_cabo_ms(self) -> float:
        segundos = self.comprimento_cabo_metros / self.velocidade_propagacao_m_s
        return segundos * 1000.0

    def simular_envio_unicast(self, pacote: Pacote) -> Pacote:
        no_origem = self.nos[pacote.origem_id]
        no_destino = self.nos[pacote.destino_id]

        tx = self.calcular_tempo_transmissao_ms(pacote.tamanho_bytes)
        prop = self._tempo_propagacao_cabo_ms()
        proc = no_origem.taxa_processamento_ms + no_destino.taxa_processamento_ms

        tempo_total = tx + prop + proc
        pacote.tempo_transito_ms = tempo_total
        pacote.rota = [pacote.origem_id,
                       "BARRAMENTO-COMPARTILHADO", pacote.destino_id]
        pacote.sucesso = no_destino.ativo

        if pacote.sucesso:
            no_destino.receber_pacote(pacote)

        return pacote

    def simular_envio_broadcast(self, pacote_base: Pacote) -> list[Pacote]:
        entregas: list[Pacote] = []
        no_origem = self.nos[pacote_base.origem_id]
        tx = self.calcular_tempo_transmissao_ms(pacote_base.tamanho_bytes)
        prop = self._tempo_propagacao_cabo_ms()

        for dest_id, no_dest in self.nos.items():
            if dest_id == pacote_base.origem_id:
                continue

            tempo = tx + prop + no_origem.taxa_processamento_ms + no_dest.taxa_processamento_ms
            p_copia = Pacote(
                id_pacote=f"{pacote_base.id_pacote}->{dest_id}",
                origem_id=pacote_base.origem_id,
                destino_id=dest_id,
                tamanho_bytes=pacote_base.tamanho_bytes,
                conteudo=pacote_base.conteudo,
                tempo_transito_ms=tempo,
                rota=[pacote_base.origem_id,
                      "BARRAMENTO-COMPARTILHADO", dest_id],
                sucesso=no_dest.ativo,
            )
            if p_copia.sucesso:
                no_dest.receber_pacote(p_copia)
            entregas.append(p_copia)

        return entregas


class LANAnel(LAN):
    """
    Topologia em Anel (Ring Topology).
    Os nós são conectados em um circuito fechado unidirecional com passagem de Token.
    """

    def __init__(
        self,
        nome: str = "LAN Anel Token Ring",
        velocidade_mbps: float = 16.0,
        tamanho_pacote_padrao: int = 1500,
    ) -> None:
        super().__init__(
            nome=nome,
            suporte_transmissao="Cabo STP (Par Trançado Blindado) / Fibra",
            controle_acesso="Token Passing (Passagem de Ficha)",
            formato_quadro="Quadro Token Ring IEEE 802.5",
            padrao="IEEE 802.5 Token Ring",
            velocidade_mbps=velocidade_mbps,
            tamanho_pacote_padrao=tamanho_pacote_padrao,
        )

    @property
    def topologia(self) -> str:
        return "Anel (Token Ring)"

    def _calcular_saltos(self, origem_id: str, destino_id: str) -> list[str]:
        lista_ids = list(self.nos.keys())
        idx_origem = lista_ids.index(origem_id)
        idx_destino = lista_ids.index(destino_id)

        n = len(lista_ids)
        saltos: list[str] = [origem_id]

        curr = (idx_origem + 1) % n
        while True:
            id_no_curr = lista_ids[curr]
            saltos.append(id_no_curr)
            if id_no_curr == destino_id:
                break
            curr = (curr + 1) % n

        return saltos

    def simular_envio_unicast(self, pacote: Pacote) -> Pacote:
        rota = self._calcular_saltos(pacote.origem_id, pacote.destino_id)
        total_hops = len(rota) - 1

        tx_base = self.calcular_tempo_transmissao_ms(pacote.tamanho_bytes)
        # Cada nó no anel introduz um pequeno atraso de repetição do token (0.01 ms)
        tempo_total = (tx_base * total_hops) + (total_hops * 0.015)

        no_destino = self.nos[pacote.destino_id]
        pacote.tempo_transito_ms = tempo_total
        pacote.rota = rota
        pacote.sucesso = no_destino.ativo

        if pacote.sucesso:
            no_destino.receber_pacote(pacote)

        return pacote

    def simular_envio_broadcast(self, pacote_base: Pacote) -> list[Pacote]:
        # No anel, o frame dá a volta completa no circuito para que todos recebam
        entregas: list[Pacote] = []
        for dest_id, no_dest in self.nos.items():
            if dest_id == pacote_base.origem_id:
                continue

            rota = self._calcular_saltos(pacote_base.origem_id, dest_id)
            total_hops = len(rota) - 1
            tx_base = self.calcular_tempo_transmissao_ms(
                pacote_base.tamanho_bytes)
            tempo = (tx_base * total_hops) + (total_hops * 0.015)

            p_copia = Pacote(
                id_pacote=f"{pacote_base.id_pacote}->{dest_id}",
                origem_id=pacote_base.origem_id,
                destino_id=dest_id,
                tamanho_bytes=pacote_base.tamanho_bytes,
                conteudo=pacote_base.conteudo,
                tempo_transito_ms=tempo,
                rota=rota,
                sucesso=no_dest.ativo,
            )
            if p_copia.sucesso:
                no_dest.receber_pacote(p_copia)
            entregas.append(p_copia)

        return entregas


class LANHub(LAN):
    """
    Topologia Estrela Física com Hub Repetidor (Camada 1).
    Qualquer pacote recebido em uma porta é repetido cegamente para todas as outras portas.
    Compartilha o domínio de colisão entre todos os nós.
    """

    def __init__(
        self,
        nome: str = "LAN Hub 100BASE-TX",
        velocidade_mbps: float = 100.0,
        tamanho_pacote_padrao: int = 1500,
    ) -> None:
        super().__init__(
            nome=nome,
            suporte_transmissao="Cabo UTP Cat5e",
            controle_acesso="CSMA/CD com Repetidor Multiportas (Half-Duplex)",
            formato_quadro="Quadro Ethernet IEEE 802.3",
            padrao="Fast Ethernet (100BASE-TX Hub)",
            velocidade_mbps=velocidade_mbps,
            tamanho_pacote_padrao=tamanho_pacote_padrao,
        )
        self.atraso_repetidor_ms = 0.008

    @property
    def topologia(self) -> str:
        return "Hub (Repetidor Multiportas)"

    def simular_envio_unicast(self, pacote: Pacote) -> Pacote:
        no_origem = self.nos[pacote.origem_id]
        no_destino = self.nos[pacote.destino_id]

        tx = self.calcular_tempo_transmissao_ms(pacote.tamanho_bytes)
        proc = no_origem.taxa_processamento_ms + no_destino.taxa_processamento_ms
        tempo_total = (tx * 2) + self.atraso_repetidor_ms + proc

        pacote.tempo_transito_ms = tempo_total
        pacote.rota = [pacote.origem_id,
                       "HUB-BROADCAST-PHY", pacote.destino_id]
        pacote.sucesso = no_destino.ativo

        if pacote.sucesso:
            no_destino.receber_pacote(pacote)

        return pacote

    def simular_envio_broadcast(self, pacote_base: Pacote) -> list[Pacote]:
        entregas: list[Pacote] = []
        no_origem = self.nos[pacote_base.origem_id]
        tx = self.calcular_tempo_transmissao_ms(pacote_base.tamanho_bytes)

        for dest_id, no_dest in self.nos.items():
            if dest_id == pacote_base.origem_id:
                continue

            tempo = (tx * 2) + self.atraso_repetidor_ms + \
                no_origem.taxa_processamento_ms + no_dest.taxa_processamento_ms
            p_copia = Pacote(
                id_pacote=f"{pacote_base.id_pacote}->{dest_id}",
                origem_id=pacote_base.origem_id,
                destino_id=dest_id,
                tamanho_bytes=pacote_base.tamanho_bytes,
                conteudo=pacote_base.conteudo,
                tempo_transito_ms=tempo,
                rota=[pacote_base.origem_id, "HUB-BROADCAST-PHY", dest_id],
                sucesso=no_dest.ativo,
            )
            if p_copia.sucesso:
                no_dest.receber_pacote(p_copia)
            entregas.append(p_copia)

        return entregas


# ==============================================================================
# HIERARQUIA 3: GERENCIADOR / SIMULADOR DINÂMICO DA LAN
# ==============================================================================

class SimuladorLAN:
    """
    Controlador de Simulação que encapsula a LAN ativa, permitindo alternar
    dinamicamente a topologia (estrela, barramento, anel, hub) preservando os nós,
    além de oferecer todos os 8 comandos e relatórios exigidos pelo exercício.
    """

    def __init__(self, topologia_inicial: str = "estrela") -> None:
        self.lan_ativa: LAN = self._instanciar_topologia(topologia_inicial)

    def _instanciar_topologia(self, tipo: str) -> LAN:
        tipo_normalizado = tipo.strip().lower()
        if tipo_normalizado in ("estrela", "star"):
            return LANEstrela()
        elif tipo_normalizado in ("barramento", "bus"):
            return LANBarramento()
        elif tipo_normalizado in ("anel", "ring"):
            return LANAnel()
        elif tipo_normalizado in ("hub",):
            return LANHub()
        else:
            raise ValueError(
                f"Topologia desconhecida: '{tipo}'. Escolha entre 'estrela', 'barramento', 'anel' ou 'hub'."
            )

    def configurar_topologia(self, nova_topologia: str) -> None:
        """
        [Requisito 4] Configura a rede proporcionando uma topologia (ex: estrela ou barramento).
        Preserva os nós já cadastrados na rede durante a transição.
        """
        nos_preservados = dict(self.lan_ativa.nos)
        tamanho_pacote = self.lan_ativa.tamanho_pacote_padrao

        self.lan_ativa = self._instanciar_topologia(nova_topologia)
        self.lan_ativa.nos = nos_preservados
        self.lan_ativa.especificar_tamanho_pacote(tamanho_pacote)

    # Delegações diretas para cumprir as 8 operações:

    def enumerar_nos(self) -> list[No]:
        """[Requisito 1]"""
        return self.lan_ativa.enumerar_nos()

    def somar_no(self, no: No) -> None:
        """[Requisito 2]"""
        self.lan_ativa.adicionar_no(no)

    def retirar_no(self, id_no: str) -> No:
        """[Requisito 3]"""
        return self.lan_ativa.retirar_no(id_no)

    def especificar_tamanho_pacote(self, tamanho_bytes: int) -> None:
        """[Requisito 5]"""
        self.lan_ativa.especificar_tamanho_pacote(tamanho_bytes)

    def enviar_pacote(self, origem_id: str, destino_id: str, mensagem: str = "") -> Pacote:
        """[Requisito 6]"""
        return self.lan_ativa.enviar_pacote(origem_id, destino_id, mensagem)

    def difundir_pacote(self, origem_id: str, mensagem: str = "") -> list[Pacote]:
        """[Requisito 7]"""
        return self.lan_ativa.difundir_pacote(origem_id, mensagem)

    def obter_estatisticas(self) -> dict[str, Any]:
        """[Requisito 8]"""
        return self.lan_ativa.obter_estatisticas()


# ==============================================================================
# DEMONSTRAÇÃO PRÁTICA E RELATÓRIOS
# ==============================================================================

def imprimir_tabela_nos(nos: list[No]) -> None:
    print("\n" + "-" * 85)
    print(f"{'ID':<8} | {'NOME DO DISPOSITIVO':<25} | {'TIPO':<30} | {'IP':<15}")
    print("-" * 85)
    if not nos:
        print("  (Nenhum nó conectado à rede)")
    for n in nos:
        print(f"{n.id_no:<8} | {n.nome:<25} | {n.tipo_dispositivo:<30} | {n.ip:<15}")
    print("-" * 85)


def imprimir_relatorio_estatisticas(stats: dict[str, Any]) -> None:
    print("\n" + "=" * 60)
    print(f" ESTATÍSTICAS DA REDE ({stats['topologia'].upper()})")
    print("=" * 60)
    print(f"  • Total de Pacotes Transmitidos : {stats['total_pacotes']}")
    print(
        f"  • Entregas com Sucesso         : {stats['pacotes_sucesso']} ({stats['taxa_sucesso_pct']:.1f}%)")
    print(f"  • Volume Total de Dados        : {stats['total_bytes']} bytes")
    print(
        f"  • Tempo Médio por Pacote       : {stats['tempo_medio_ms']:.4f} ms")
    print(
        f"  • Tempo Mínimo de Trânsito     : {stats['tempo_minimo_ms']:.4f} ms")
    print(
        f"  • Tempo Máximo de Trânsito     : {stats['tempo_maximo_ms']:.4f} ms")
    print(
        f"  • Velocidade Nominal           : {stats['velocidade_mbps']} Mbps")
    print("=" * 60)


def main() -> None:
    """Execução demonstrativa completa de todas as funcionalidades exigidas."""
    print("=" * 90)
    print(" EXERCÍCIO 17.3 - SIMULADOR DE REDE LOCAL (LAN) E TOPOLOGIAS")
    print("=" * 90)

    # Instancia o simulador com topologia Estrela por padrão
    sim = SimuladorLAN(topologia_inicial="estrela")
    print(f">> Rede Inicial Criada: {sim.lan_ativa}")

    # 1. Somar nós na rede LAN (Requisito 2)
    print("\n[Operação 2] Cadastrando dispositivos heterogêneos na LAN...")
    pc1 = ComputadorPessoal("PC-01", "Desktop Financeiro",
                            "00:1A:2B:3C:4D:01", "192.168.1.10")
    pc2 = ComputadorPessoal("PC-02", "Desktop RH",
                            "00:1A:2B:3C:4D:02", "192.168.1.11")
    ws1 = EstacaoTrabalho("WS-01", "Workstation Engenharia",
                          "00:1A:2B:3C:4D:03", "192.168.1.20")
    srv1 = Servidor("SRV-01", "Servidor de Arquivos",
                    "00:1A:2B:3C:4D:04", "192.168.1.100")
    fax1 = MaquinaFax("FAX-01", "Máquina de Fax Recepção",
                      "00:1A:2B:3C:4D:05", "192.168.1.50")
    imp1 = ImpressoraRede("IMP-01", "Impressora Laser",
                          "00:1A:2B:3C:4D:06", "192.168.1.60")

    for no in [pc1, pc2, ws1, srv1, fax1, imp1]:
        sim.somar_no(no)
        print(f"  + Nó adicionado: {no.nome} ({no.tipo_dispositivo})")

    # 2. Enumerar os nós atuais da rede LAN (Requisito 1)
    print("\n[Operação 1] Enumerando nós conectados na LAN:")
    imprimir_tabela_nos(sim.enumerar_nos())

    # 3. Especificar tamanho do pacote (Requisito 5)
    print("\n[Operação 5] Especificando tamanho do pacote para 1024 bytes...")
    sim.especificar_tamanho_pacote(1024)
    print(
        f"  Tamanho configurado: {sim.lan_ativa.tamanho_pacote_padrao} bytes")

    # 4. Enviar pacote de um nó específico a outro (Requisito 6)
    print("\n[Operação 6] Enviando pacote Unicast de 'PC-01' para 'SRV-01'...")
    pkt1 = sim.enviar_pacote(
        "PC-01", "SRV-01", "Consulta SQL ao Banco de Dados")
    print(f"  Resultado: {pkt1}")
    print(f"  Rota percorrida: {' -> '.join(pkt1.rota)}")

    # 5. Difundir pacote a todos os nós (Requisito 7)
    print("\n[Operação 7] Difundindo pacote Broadcast a partir de 'SRV-01'...")
    broadcast_pkts = sim.difundir_pacote(
        "SRV-01", "Aviso: Manutenção do Servidor às 22h")
    print(f"  Total de nós que receberam o broadcast: {len(broadcast_pkts)}")
    for p in broadcast_pkts:
        print(f"  -> {p.destino_id}: {p.tempo_transito_ms:.4f} ms")

    # 6. Estatísticas da LAN (Requisito 8)
    print("\n[Operação 8] Estatísticas da LAN na Topologia Estrela:")
    imprimir_relatorio_estatisticas(sim.obter_estatisticas())

    # 7. Retirar um nó da rede LAN (Requisito 3)
    print("\n[Operação 3] Retirando nó 'FAX-01' da rede LAN...")
    removido = sim.retirar_no("FAX-01")
    print(f"  Nó desativado/removido: {removido.nome} (ID: {removido.id_no})")
    print("  Nós restantes após remoção:")
    imprimir_tabela_nos(sim.enumerar_nos())

    # 8. Configurar a rede proporcionando topologia de Barramento (Requisito 4)
    print("\n[Operação 4] Reconfigurando topologia para BARRAMENTO...")
    sim.configurar_topologia("barramento")
    print(f"  Nova Topologia Ativa: {sim.lan_ativa.topologia}")
    print(f"  Meio de Transmissão: {sim.lan_ativa.suporte_transmissao}")
    print(f"  Velocidade: {sim.lan_ativa.velocidade_mbps} Mbps")

    print("\n  Enviando pacote Unicast na nova topologia em barramento (PC-02 -> IMP-01)...")
    pkt_bus = sim.enviar_pacote("PC-02", "IMP-01", "Documento para Impressão")
    print(f"  Resultado: {pkt_bus}")
    print(f"  Rota: {' -> '.join(pkt_bus.rota)}")

    print("\n  Estatísticas da LAN após transição para Barramento:")
    imprimir_relatorio_estatisticas(sim.obter_estatisticas())

    print("\n>> Demonstração do Exercício 17.3 concluída com êxito!")


if __name__ == "__main__":
    main()
