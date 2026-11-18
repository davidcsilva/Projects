'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.4

Enunciado:
Escrever uma declaração de classes para cada uma das especificações seguintes.
Em cada caso, incluir um protótipo para um construtor e uma função membro
visualizar dados que possam ser utilizados para visualizar os valores dos membros.

a) Uma classe chamada Hora que tenha membros dados inteiros denominados
   segundos, minutos e horas.

b) Uma classe Complexo que tenha membros dados inteiros denominados xcentro e
   ycentro e um membro dado em ponto flutuante chamado raio.

c) Uma classe denominada Sistema que tenha membros dado de tipo caractere
   computador, impressora e tela, cada uma capaz de conter 30 caracteres
   e membros dados reais denominados PreçoComputador, PreçoImpressora e PreçoTela.
'''


# ==============================================================================
# a) Classe Hora
# ==============================================================================
class Hora:
    """
    Representa um horário com horas, minutos e segundos.

    Declaração C++ equivalente:
    ----------------------------
    class Hora {
    private:
        int horas;
        int minutos;
        int segundos;
    public:
        Hora(int h = 0, int m = 0, int s = 0); // Protótipo do construtor
        void visualizarDados() const;          // Função membro para visualizar dados
    };
    """

    def __init__(self, horas: int = 0, minutos: int = 0, segundos: int = 0) -> None:
        """
        Construtor da classe Hora.
        Inicializa horas, minutos e segundos com validação básica.
        """
        self.horas: int = horas
        self.minutos: int = minutos
        self.segundos: int = segundos

    def visualizar_dados(self) -> None:
        """Função membro para exibir os valores dos membros dados."""
        print(
            f"Horário: {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")


# ==============================================================================
# b) Classe Complexo
# ==============================================================================
class Complexo:
    """
    Representa uma entidade com centro (x, y) e raio.

    Declaração C++ equivalente:
    ----------------------------
    class Complexo {
    private:
        int xcentro;
        int ycentro;
        float raio;
    public:
        Complexo(int x = 0, int y = 0, float r = 0.0f); // Protótipo do construtor
        void visualizarDados() const;                    // Função membro para visualizar dados
    };
    """

    def __init__(self, xcentro: int = 0, ycentro: int = 0, raio: float = 0.0) -> None:
        """
        Construtor da classe Complexo.
        Inicializa as coordenadas do centro e o raio.
        """
        self.xcentro: int = xcentro
        self.ycentro: int = ycentro
        self.raio: float = float(raio)

    def visualizar_dados(self) -> None:
        """Função membro para exibir os valores dos membros dados."""
        print(
            f"Centro: ({self.xcentro}, {self.ycentro}) | Raio: {self.raio:.2f}")


# ==============================================================================
# c) Classe Sistema
# ==============================================================================
class Sistema:
    """
    Representa a configuração de um sistema computacional e seus preços.

    Declaração C++ equivalente:
    ----------------------------
    class Sistema {
    private:
        char computador[31];
        char impressora[31];
        char tela[31];
        double PrecoComputador;
        double PrecoImpressora;
        double PrecoTela;
    public:
        Sistema(const char* comp = "", const char* imp = "", const char* tel = "",
                double pComp = 0.0, double pImp = 0.0, double pTel = 0.0);
        void visualizarDados() const;
    };
    """

    TAMANHO_MAXIMO_CHAR: int = 30

    def __init__(
        self,
        computador: str = "",
        impressora: str = "",
        tela: str = "",
        preco_computador: float = 0.0,
        preco_impressora: float = 0.0,
        preco_tela: float = 0.0,
    ) -> None:
        """
        Construtor da classe Sistema.
        Garante que os membros texto respeitem o limite de até 30 caracteres.
        """
        self.computador: str = computador[: self.TAMANHO_MAXIMO_CHAR]
        self.impressora: str = impressora[: self.TAMANHO_MAXIMO_CHAR]
        self.tela: str = tela[: self.TAMANHO_MAXIMO_CHAR]
        self.PrecoComputador: float = float(preco_computador)
        self.PrecoImpressora: float = float(preco_impressora)
        self.PrecoTela: float = float(preco_tela)

    def visualizar_dados(self) -> None:
        """Função membro para exibir os componentes e seus respectivos preços."""
        preco_total = self.PrecoComputador + self.PrecoImpressora + self.PrecoTela
        print("=== Especificações do Sistema ===")
        print(
            f"Computador:  {self.computador:<30} | Preço: R$ {self.PrecoComputador:8.2f}")
        print(
            f"Impressora:  {self.impressora:<30} | Preço: R$ {self.PrecoImpressora:8.2f}")
        print(
            f"Tela:        {self.tela:<30} | Preço: R$ {self.PrecoTela:8.2f}")
        print(f"Preço Total: {'':<30} | Preço: R$ {preco_total:8.2f}")


# ==============================================================================
# Testes / Demonstração Prática
# ==============================================================================
if __name__ == "__main__":
    print("--- Teste a: Classe Hora ---")
    h1 = Hora(14, 30, 45)
    h1.visualizar_dados()

    print("\n--- Teste b: Classe Complexo ---")
    c1 = Complexo(xcentro=10, ycentro=-5, raio=7.5)
    c1.visualizar_dados()

    print("\n--- Teste c: Classe Sistema ---")
    sys1 = Sistema(
        computador="Dell OptiPlex Core i7 32GB",
        impressora="HP LaserJet Pro M404dn",
        tela="Monitor LG UltraWide 29 pol",
        preco_computador=4500.00,
        preco_impressora=1800.50,
        preco_tela=1250.90,
    )
    sys1.visualizar_dados()
