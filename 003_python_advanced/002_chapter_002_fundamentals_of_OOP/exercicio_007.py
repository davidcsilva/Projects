'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.7

Enunciado:
Criar uma classe que descreva um retângulo que possa ser visualizado em uma tela
do computador, mudar de tamanho, modificar sua cor de fundo e as cores laterais.
'''

from dataclasses import dataclass, field


# Dicionário de cores ANSI para renderização visual colorida no terminal
CORES_ANSI: dict[str, str] = {
    "preto": "\033[30m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "magenta": "\033[35m",
    "ciano": "\033[36m",
    "branco": "\033[37m",
    "reset": "\033[0m"
}

CORES_FUNDO_ANSI: dict[str, str] = {
    "preto": "\033[40m",
    "vermelho": "\033[41m",
    "verde": "\033[42m",
    "amarelo": "\033[43m",
    "azul": "\033[44m",
    "magenta": "\033[45m",
    "ciano": "\033[46m",
    "branco": "\033[47m",
    "padrao": "\033[49m"
}


@dataclass
class CoresLaterais:
    """Encapsula as cores individuais das 4 bordas laterais do retângulo."""
    superior: str = "azul"
    inferior: str = "azul"
    esquerda: str = "azul"
    direita: str = "azul"

    def definir_todas(self, cor: str) -> None:
        """Modifica todas as cores laterais simultaneamente."""
        self.superior = cor
        self.inferior = cor
        self.esquerda = cor
        self.direita = cor

    def definir_individual(
        self,
        superior: str | None = None,
        inferior: str | None = None,
        esquerda: str | None = None,
        direita: str | None = None
    ) -> None:
        """Modifica as cores laterais individualmente."""
        if superior is not None:
            self.superior = superior
        if inferior is not None:
            self.inferior = inferior
        if esquerda is not None:
            self.esquerda = esquerda
        if direita is not None:
            self.direita = direita


class Retangulo:
    """
    Classe que descreve um retângulo gráfico na tela do computador.
    Permite:
      - Ser visualizado graficamente e textualmente;
      - Mudar de tamanho (largura e altura);
      - Modificar sua cor de fundo;
      - Modificar suas cores laterais (bordas).
    """

    def __init__(
        self,
        largura: int = 10,
        altura: int = 5,
        pos_x: int = 0,
        pos_y: int = 0,
        cor_fundo: str = "preto",
        cor_lateral_padrao: str = "azul"
    ) -> None:
        self.pos_x: int = max(0, pos_x)
        self.pos_y: int = max(0, pos_y)
        self._largura: int = max(2, largura)
        self._altura: int = max(2, altura)
        self.cor_fundo: str = cor_fundo.lower()
        self.cores_laterais: CoresLaterais = CoresLaterais()
        self.cores_laterais.definir_todas(cor_lateral_padrao.lower())

    # --------------------------------------------------------------------------
    # Propriedades de Dimensões
    # --------------------------------------------------------------------------
    @property
    def largura(self) -> int:
        return self._largura

    @property
    def altura(self) -> int:
        return self._altura

    @property
    def area(self) -> int:
        """Calcula a área do retângulo."""
        return self._largura * self._altura

    @property
    def perimetro(self) -> int:
        """Calcula o perímetro do retângulo."""
        return 2 * (self._largura + self._altura)

    # --------------------------------------------------------------------------
    # Operação 1: Mudar de tamanho
    # --------------------------------------------------------------------------
    def mudar_tamanho(self, nova_largura: int, nova_altura: int) -> None:
        """
        Altera as dimensões de largura e altura do retângulo.
        Exige valores mínimos de 2 para permitir bordas.
        """
        if nova_largura < 2 or nova_altura < 2:
            raise ValueError(
                "A largura e a altura devem ser no mínimo 2 unidades.")
        self._largura = nova_largura
        self._altura = nova_altura
        print(f"[Ação] Tamanho alterado para {self._largura}x{self._altura}.")

    def redimensionar(self, fator: float) -> None:
        """Redimensiona proporcionalmente por um fator de escala (ex.: 1.5, 2.0)."""
        if fator <= 0:
            raise ValueError("O fator de redimensionamento deve ser positivo.")
        self.mudar_tamanho(int(self._largura * fator),
                           int(self._altura * fator))

    # --------------------------------------------------------------------------
    # Operação 2: Modificar cor de fundo
    # --------------------------------------------------------------------------
    def modificar_cor_fundo(self, nova_cor: str) -> None:
        """Altera a cor de preenchimento de fundo do retângulo."""
        self.cor_fundo = nova_cor.lower()
        print(f"[Ação] Cor de fundo alterada para '{self.cor_fundo}'.")

    # --------------------------------------------------------------------------
    # Operação 3: Modificar cores laterais
    # --------------------------------------------------------------------------
    def modificar_todas_cores_laterais(self, nova_cor: str) -> None:
        """Altera a cor de todas as quatro bordas laterais para a mesma cor."""
        self.cores_laterais.definir_todas(nova_cor.lower())
        print(f"[Ação] Todas as cores laterais alteradas para '{nova_cor}'.")

    def modificar_cores_laterais(
        self,
        superior: str | None = None,
        inferior: str | None = None,
        esquerda: str | None = None,
        direita: str | None = None
    ) -> None:
        """Permite alterar as cores das bordas superior, inferior, esquerda e direita individualmente."""
        self.cores_laterais.definir_individual(
            superior, inferior, esquerda, direita)
        print("[Ação] Cores laterais atualizadas:")
        print(
            f"       Superior: {self.cores_laterais.superior} | Inferior: {self.cores_laterais.inferior}")
        print(
            f"       Esquerda: {self.cores_laterais.esquerda} | Direita:  {self.cores_laterais.direita}")

    # --------------------------------------------------------------------------
    # Operação 4: Visualizar na tela do computador
    # --------------------------------------------------------------------------
    def visualizar(self) -> None:
        """
        Renderiza graficamente o retângulo na tela/terminal com caracteres
        ASCII e cores ANSI correspondentes às cores configuradas.
        """
        reset = CORES_ANSI["reset"]
        bg = CORES_FUNDO_ANSI.get(self.cor_fundo, CORES_FUNDO_ANSI["padrao"])

        cor_sup = CORES_ANSI.get(self.cores_laterais.superior, "")
        cor_inf = CORES_ANSI.get(self.cores_laterais.inferior, "")
        cor_esq = CORES_ANSI.get(self.cores_laterais.esquerda, "")
        cor_dir = CORES_ANSI.get(self.cores_laterais.direita, "")

        print("\n" + "=" * 50)
        print(
            f"Ficha do Retângulo: {self._largura}x{self._altura} em ({self.pos_x}, {self.pos_y})")
        print(f"Área: {self.area} | Perímetro: {self.perimetro}")
        print(
            f"Fundo: {self.cor_fundo.upper()} | Bordas: [Sup: {self.cores_laterais.superior}, Inf: {self.cores_laterais.inferior}, Esq: {self.cores_laterais.esquerda}, Dir: {self.cores_laterais.direita}]")
        print("-" * 50)

        # 1. Borda Superior
        linha_topo = cor_sup + "+" + ("-" * (self._largura - 2)) + "+" + reset
        print(linha_topo)

        # 2. Linhas Intermediárias (Borda Esquerda + Preenchimento Fundo + Borda Direita)
        espaco_interno = " " * (self._largura - 2)
        for _ in range(self._altura - 2):
            linha_meio = (
                cor_esq + "|" + reset +
                bg + espaco_interno + reset +
                cor_dir + "|" + reset
            )
            print(linha_meio)

        # 3. Borda Inferior
        linha_base = cor_inf + "+" + ("-" * (self._largura - 2)) + "+" + reset
        print(linha_base)
        print("=" * 50 + "\n")


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    print("--- 1. Criando retângulo inicial de 16x6 ---")
    r = Retangulo(
        largura=16,
        altura=6,
        pos_x=5,
        pos_y=2,
        cor_fundo="azul",
        cor_lateral_padrao="amarelo"
    )
    r.visualizar()

    print("--- 2. Mudando de tamanho para 24x8 ---")
    r.mudar_tamanho(nova_largura=24, nova_altura=8)
    r.visualizar()

    print("--- 3. Modificando cor de fundo para verde ---")
    r.modificar_cor_fundo("verde")
    r.visualizar()

    print("--- 4. Modificando cores laterais de forma individualizada ---")
    r.modificar_cores_laterais(
        superior="vermelho",
        inferior="ciano",
        esquerda="magenta",
        direita="amarelo"
    )
    r.visualizar()
