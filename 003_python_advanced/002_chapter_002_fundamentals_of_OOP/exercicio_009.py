'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.9

Enunciado:
Representar uma classe elevador que tenha as funções usuais de subir, baixar,
parar entre níveis (andares), alarme, sobrecarga e, em cada andar, botões de
chamada para subir ou descer.
'''

from dataclasses import dataclass
from enum import Enum


class Direcao(Enum):
    PARADO = "Parado"
    SUBINDO = "Subindo"
    DESCENDO = "Descendo"


@dataclass
class BotaoChamadaAndar:
    """
    Representa o painel de botões externo presente no hall de cada andar.
    Permite solicitar subida ou descida.
    """
    andar: int
    chamada_subir: bool = False
    chamada_descer: bool = False

    def pressionar_subir(self) -> None:
        self.chamada_subir = True
        print(f"[Painel Hall {self.andar}º Andar] Botão ▲ SUBIR pressionado.")

    def pressionar_descer(self) -> None:
        self.chamada_descer = True
        print(f"[Painel Hall {self.andar}º Andar] Botão ▼ DESCER pressionado.")

    def atender_chamada(self, direcao: Direcao) -> None:
        if direcao == Direcao.SUBINDO:
            self.chamada_subir = False
        elif direcao == Direcao.DESCENDO:
            self.chamada_descer = False
        else:
            self.chamada_subir = False
            self.chamada_descer = False


class Elevador:
    """
    Representa um elevador com controle de andares, portas, segurança,
    detecção de sobrecarga, acionamento de alarme e integração com botões de chamada.
    """

    def __init__(
        self,
        total_andares: int = 10,
        andar_minimo: int = 0,
        capacidade_maxima_kg: float = 600.0
    ) -> None:
        self.total_andares: int = total_andares
        self.andar_minimo: int = andar_minimo
        self.capacidade_maxima_kg: float = capacidade_maxima_kg

        # Estado da cabine
        self.andar_atual: int = andar_minimo
        self.direcao: Direcao = Direcao.PARADO
        self.porta_aberta: bool = False
        self.peso_atual_kg: float = 0.0

        # Mecanismos de segurança
        self.alarme_ativo: bool = False
        self.em_sobrecarga: bool = False

        # Destinos internos solicitados dentro da cabine
        self.destinos_cabine: set[int] = set()

        # Painel de botões externos em cada andar
        self.botoes_andares: dict[int, BotaoChamadaAndar] = {
            andar: BotaoChamadaAndar(andar)
            for andar in range(andar_minimo, total_andares + 1)
        }

    # --------------------------------------------------------------------------
    # 1. Controle de Carga e Sobrecarga
    # --------------------------------------------------------------------------
    def atualizar_peso(self, peso_kg: float) -> None:
        """Atualiza a pesagem da cabine e verifica sobrecarga."""
        self.peso_atual_kg = max(0.0, peso_kg)
        self.verificar_sobrecarga()

    def verificar_sobrecarga(self) -> bool:
        """
        Detecta se a carga atual excede a capacidade máxima permitida.
        Se exceder, bloqueia o fechamento das portas e o movimento.
        """
        if self.peso_atual_kg > self.capacidade_maxima_kg:
            self.em_sobrecarga = True
            print(
                f"\n[ALERTA DE SOBRECARGA!] Peso: {self.peso_atual_kg:.1f} kg "
                f"(Capacidade máxima: {self.capacidade_maxima_kg:.1f} kg). "
                f"O elevador não se moverá até que passageiros desembarquem!"
            )
            self.abrir_porta()
        else:
            if self.em_sobrecarga:
                print("[Sobrecarga normalizada] Peso dentro dos limites permitidos.")
            self.em_sobrecarga = False
        return self.em_sobrecarga

    # --------------------------------------------------------------------------
    # 2. Mecanismo de Alarme
    # --------------------------------------------------------------------------
    def acionar_alarme(self) -> None:
        """Dispara o alarme de emergência e trava o elevador imediatamente."""
        self.alarme_ativo = True
        self.direcao = Direcao.PARADO
        print("\n[EMERGÊNCIA!] Alarme acionado! Elevador paralisado por segurança.")

    def desativar_alarme(self) -> None:
        """Desativa o alarme após resolução da emergência pela equipe técnica."""
        self.alarme_ativo = False
        print("[Alarme desativado] Sistema operacional liberado.")

    # --------------------------------------------------------------------------
    # 3. Portas
    # --------------------------------------------------------------------------
    def abrir_porta(self) -> None:
        """Abre a porta da cabine."""
        self.porta_aberta = True
        print(f"[Porta] Porta ABERTA no {self.andar_atual}º andar.")

    def fechar_porta(self) -> bool:
        """Fecha a porta se não houver sobrecarga nem alarme ativo."""
        if self.em_sobrecarga:
            print("[Bloqueio] Porta NÃO pode fechar devido à sobrecarga de peso!")
            return False
        if self.alarme_ativo:
            print("[Bloqueio] Porta travada enquanto alarme estiver acionado.")
            return False
        self.porta_aberta = False
        print(f"[Porta] Porta FECHADA no {self.andar_atual}º andar.")
        return True

    # --------------------------------------------------------------------------
    # 4. Movimentação: Subir, Baixar e Parar entre Níveis
    # --------------------------------------------------------------------------
    def subir(self) -> bool:
        """Move o elevador um nível para cima."""
        if not self._pode_se_mover():
            return False

        if self.andar_atual >= self.total_andares:
            print(
                f"[Limite] Elevador já está no último andar ({self.total_andares}º).")
            self.parar()
            return False

        if not self.fechar_porta():
            return False

        self.direcao = Direcao.SUBINDO
        self.andar_atual += 1
        print(
            f"[Movimento ▲] Elevador subindo... Chegou ao {self.andar_atual}º andar.")
        self._verificar_parada()
        return True

    def baixar(self) -> bool:
        """Move o elevador um nível para baixo."""
        if not self._pode_se_mover():
            return False

        if self.andar_atual <= self.andar_minimo:
            print(
                f"[Limite] Elevador já está no andar térreo/mínimo ({self.andar_minimo}º).")
            self.parar()
            return False

        if not self.fechar_porta():
            return False

        self.direcao = Direcao.DESCENDO
        self.andar_atual -= 1
        print(
            f"[Movimento ▼] Elevador descendo... Chegou ao {self.andar_atual}º andar.")
        self._verificar_parada()
        return True

    def parar(self) -> None:
        """Interrompe o movimento entre níveis ou no andar atual e abre a porta."""
        self.direcao = Direcao.PARADO
        print(f"[Parada] Elevador PAROU no {self.andar_atual}º andar.")
        self.abrir_porta()

        # Atende solicitações no andar atual
        self.destinos_cabine.discard(self.andar_atual)
        if self.andar_atual in self.botoes_andares:
            self.botoes_andares[self.andar_atual].atender_chamada(self.direcao)

    def _pode_se_mover(self) -> bool:
        """Verifica todas as travas de segurança antes de mover."""
        if self.alarme_ativo:
            print("[Segurança] Movimento bloqueado: alarme de emergência ativo.")
            return False
        if self.em_sobrecarga:
            print("[Segurança] Movimento bloqueado: peso acima da capacidade máxima.")
            return False
        return True

    def _verificar_parada(self) -> None:
        """Verifica se há solicitação para parar no andar recém-atingido."""
        painel = self.botoes_andares.get(self.andar_atual)
        deve_parar = (
            self.andar_atual in self.destinos_cabine or
            (painel and (painel.chamada_subir or painel.chamada_descer))
        )
        if deve_parar:
            self.parar()

    # --------------------------------------------------------------------------
    # 5. Interface com Botões dos Andares e Seleção Interna
    # --------------------------------------------------------------------------
    def chamar_no_andar(self, andar: int, direcao_desejada: str) -> None:
        """
        Simula um usuário no hall de um andar pressionando o botão de subir ou descer.
        """
        if not (self.andar_minimo <= andar <= self.total_andares):
            print(f"[Erro] Andar {andar} inexistente no edifício.")
            return

        botao = self.botoes_andares[andar]
        if direcao_desejada.lower() in ("subir", "sobe", "up"):
            botao.pressionar_subir()
        elif direcao_desejada.lower() in ("descer", "desce", "down"):
            botao.pressionar_descer()

    def selecionar_destino_cabine(self, andar: int) -> None:
        """Simula um passageiro dentro do elevador pressionando o botão do andar."""
        if not (self.andar_minimo <= andar <= self.total_andares):
            print(f"[Erro] Andar {andar} inválido.")
            return
        self.destinos_cabine.add(andar)
        print(f"[Painel Cabine] Andar {andar} selecionado internamente.")

    def exibir_status(self) -> None:
        """Imprime o painel geral do elevador."""
        porta = "Aberta" if self.porta_aberta else "Fechada"
        alarme = "ATIVO!" if self.alarme_ativo else "Normal"
        sobrecarga = "SIM!" if self.em_sobrecarga else "Não"
        print("\n" + "=" * 55)
        print(
            f"PAINEL DO ELEVADOR: {self.andar_atual}º Andar | Direção: {self.direcao.value}")
        print(
            f"Porta: {porta} | Carga: {self.peso_atual_kg:.1f}/{self.capacidade_maxima_kg:.1f} kg")
        print(f"Status Alarme: {alarme} | Sobrecarga: {sobrecarga}")
        print("=" * 55)


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    elevador = Elevador(total_andares=5, capacidade_maxima_kg=450.0)
    elevador.exibir_status()

    print("\n--- 1. Chamada Externa e Embarque ---")
    # Alguém no 2º andar aperta botão para subir
    elevador.chamar_no_andar(andar=2, direcao_desejada="subir")

    # Elevador sobe até o 2º andar
    elevador.subir()
    elevador.subir()  # Chega ao 2º e para automaticamente

    print("\n--- 2. Embarque de Passageiros e Destino Interno ---")
    elevador.atualizar_peso(160.0)  # Dois passageiros entram
    elevador.selecionar_destino_cabine(4)

    elevador.subir()  # vai para 3º andar
    elevador.subir()  # chega ao 4º andar e para

    print("\n--- 3. Teste de Sobrecarga ---")
    elevador.atualizar_peso(550.0)  # Excede limite de 450 kg
    elevador.subir()  # Deve ser bloqueado!
    elevador.atualizar_peso(380.0)  # Passageiro desce, peso normaliza

    print("\n--- 4. Teste de Descida e Alarme de Emergência ---")
    elevador.baixar()
    elevador.acionar_alarme()
    elevador.baixar()  # Bloqueado pelo alarme!
    elevador.desativar_alarme()
    elevador.baixar()  # Agora desce normalmente

    elevador.exibir_status()
