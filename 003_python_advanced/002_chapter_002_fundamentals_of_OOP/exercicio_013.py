'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.13

Enunciado:
Construir uma classe chamada Luz que simule um semáforo de tráfego.
O atributo cor da classe deve mudar de Verde a Amarelo e Vermelho e de novo voltar
para Verde mediante a função mudança. Quando um objeto Luz é criado sua cor
inicial será o Vermelho.
'''

from enum import Enum


class CorSemaforo(Enum):
    VERMELHO = "Vermelho"
    VERDE = "Verde"
    AMARELO = "Amarelo"


# Cores ANSI para visualização estilizada no terminal
CORES_ANSI = {
    "Vermelho": "\033[1;31m",
    "Amarelo": "\033[1;33m",
    "Verde": "\033[1;32m",
    "Cinza": "\033[1;30m",
    "Reset": "\033[0m"
}


class Luz:
    """
    Simula um semáforo de tráfego.

    Regras de negócio:
    - Ao ser instanciado, a cor inicial é sempre 'Vermelho'.
    - A função 'mudanca()' transita ciclicamente:
        Vermelho -> Verde -> Amarelo -> Vermelho -> Verde...
    """

    # Mapeamento do ciclo de transição de trânsito
    PROXIMA_COR: dict[CorSemaforo, CorSemaforo] = {
        CorSemaforo.VERMELHO: CorSemaforo.VERDE,
        CorSemaforo.VERDE: CorSemaforo.AMARELO,
        CorSemaforo.AMARELO: CorSemaforo.VERMELHO
    }

    def __init__(self) -> None:
        """
        Construtor da classe Luz.
        Garante que toda nova instância inicie estritamente na cor Vermelho.
        """
        self._cor: CorSemaforo = CorSemaforo.VERMELHO

    @property
    def cor(self) -> str:
        """Retorna o nome da cor atual do semáforo."""
        return self._cor.value

    def mudanca(self) -> str:
        """
        Executa a transição da cor do semáforo para o próximo estado:
        Verde -> Amarelo -> Vermelho -> Verde...
        Retorna a nova cor atingida.
        """
        cor_anterior = self._cor
        self._cor = self.PROXIMA_COR[self._cor]
        print(
            f"[Transição] Cor mudou de {cor_anterior.value} para {self._cor.value}.")
        return self.cor

    # Sinônimo com acentuação para compatibilidade
    def mudança(self) -> str:
        return self.mudanca()

    def visualizar(self) -> None:
        """
        Renderiza graficamente o semáforo no terminal destacando a luz acesa.
        """
        reset = CORES_ANSI["Reset"]
        cinza = CORES_ANSI["Cinza"]

        # Define quais lâmpadas estão acesas ou apagadas (cinza)
        luz_vermelha = f"{CORES_ANSI['Vermelho']}● Vermelho (PARE){reset}" if self._cor == CorSemaforo.VERMELHO else f"{cinza}○ Vermelho{reset}"
        luz_amarela = f"{CORES_ANSI['Amarelo']}● Amarelo (ATENÇÃO){reset}" if self._cor == CorSemaforo.AMARELO else f"{cinza}○ Amarelo{reset}"
        luz_verde = f"{CORES_ANSI['Verde']}● Verde (SIGA){reset}" if self._cor == CorSemaforo.VERDE else f"{cinza}○ Verde{reset}"

        print("+-----------------------+")
        print(f"|  {luz_vermelha:<28} |")
        print(f"|  {luz_amarela:<28} |")
        print(f"|  {luz_verde:<28} |")
        print("+-----------------------+")

    def __str__(self) -> str:
        return f"Semáforo (Cor: {self.cor})"

    def __repr__(self) -> str:
        return f"Luz(cor='{self.cor}')"


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    print("=== 1. Criação do Objeto Luz ===")
    semaforo = Luz()
    print(f"Cor inicial do semáforo recém-criado: {semaforo.cor}")
    semaforo.visualizar()

    print("\n=== 2. Ciclo de Transições via função mudança() ===")

    # 1ª mudança: Vermelho -> Verde
    print("\n--- 1ª Mudança ---")
    semaforo.mudanca()
    semaforo.visualizar()

    # 2ª mudança: Verde -> Amarelo
    print("\n--- 2ª Mudança ---")
    semaforo.mudanca()
    semaforo.visualizar()

    # 3ª mudança: Amarelo -> Vermelho
    print("\n--- 3ª Mudança ---")
    semaforo.mudanca()
    semaforo.visualizar()

    # 4ª mudança: Retorno ao Verde (completando o ciclo contínuo)
    print("\n--- 4ª Mudança (Ciclo reiniciado) ---")
    semaforo.mudanca()
    semaforo.visualizar()
