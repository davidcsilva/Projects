"""
Exercício 16.3:
Crie uma classe chamada hora que tenha membros dado separados de tipo int para horas,
minutos e segundos.
- Um construtor iniciará este dado em 0 e outro o iniciará em valores fixos.
- Uma função membro deverá visualizar a hora em formato 11:59:59.
- Outra função membro irá somar dois objetos de tipo hora passados como argumentos.
- Uma função principal main() cria dois objetos inicializados e um que não está inicializado.
  Some os dois valores inicializados e deixe o resultado no objeto não inicializado.
- Por último, visualize o valor resultante.
"""


class Hora:
    """
    Representa um horário com horas, minutos e segundos.

    Em Python, a sobrecarga de construtores tradicional (como em C++) é realizada
    através de parâmetros opcionais com valores padrão no método __init__.
    - Sem argumentos: inicializa com 0 (hora() -> 00:00:00).
    - Com argumentos: inicializa com valores fixos (hora(h, m, s)).
    """

    def __init__(self, horas: int = 0, minutos: int = 0, segundos: int = 0) -> None:
        self.horas: int = int(horas)
        self.minutos: int = int(minutos)
        self.segundos: int = int(segundos)
        self._ajustar()

    def _ajustar(self) -> None:
        """
        Normaliza os valores caso segundos >= 60 ou minutos >= 60,
        mantendo o formato padrão de relógio (24 horas).
        """
        if self.segundos >= 60 or self.segundos < 0:
            extra_min = self.segundos // 60
            self.segundos %= 60
            self.minutos += extra_min

        if self.minutos >= 60 or self.minutos < 0:
            extra_h = self.minutos // 60
            self.minutos %= 60
            self.horas += extra_h

        self.horas %= 24

    def visualizar(self) -> None:
        """
        Exibe a hora formatada no padrão 11:59:59 (com dois dígitos por campo).
        """
        print(f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")

    def somar(self, h1: "Hora", h2: "Hora") -> None:
        """
        Soma dois objetos do tipo Hora passados como argumentos e armazena
        o resultado no próprio objeto (self).

        Trata adequadamente o 'vai-um' para segundos e minutos e ajusta as horas
        no formato de 24 horas.
        """
        total_segundos = h1.segundos + h2.segundos
        vai_um_min = total_segundos // 60
        self.segundos = total_segundos % 60

        total_minutos = h1.minutos + h2.minutos + vai_um_min
        vai_um_horas = total_minutos // 60
        self.minutos = total_minutos % 60

        self.horas = (h1.horas + h2.horas + vai_um_horas) % 24

    def __str__(self) -> str:
        """Retorna a representação textual formatada."""
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"

    def __repr__(self) -> str:
        return f"Hora(horas={self.horas}, minutos={self.minutos}, segundos={self.segundos})"

    def __add__(self, outro: "Hora") -> "Hora":
        """
        Sobrecarga do operador '+' em Python (h1 + h2).
        Retorna uma nova instância com a soma calculada.
        """
        if not isinstance(outro, Hora):
            return NotImplemented
        resultado = Hora()
        resultado.somar(self, outro)
        return resultado


# Alias para permitir a instanciação tanto por Hora() quanto por hora()
hora = Hora


def main() -> None:
    """
    Função principal:
    - Cria dois objetos inicializados com valores fixos.
    - Cria um objeto não inicializado (iniciado em 0).
    - Soma os dois valores inicializados e guarda no objeto não inicializado.
    - Visualiza o valor resultante.
    """
    print("=== Exercício 16.3: Classe Hora ===")

    # Dois objetos inicializados com valores fixos
    hora1 = Hora(10, 45, 35)
    hora2 = Hora(2, 20, 40)

    # Um objeto que não está inicializado com valores específicos (iniciado em 0)
    hora_resultado = Hora()

    print("\nHora 1 (inicializada):")
    hora1.visualizar()

    print("\nHora 2 (inicializada):")
    hora2.visualizar()

    print("\nHora resultado (não inicializada / padrão 0):")
    hora_resultado.visualizar()

    # Somar os dois objetos inicializados e deixar o resultado no objeto não inicializado
    hora_resultado.somar(hora1, hora2)

    print("\nHora resultante após a soma (hora_resultado.somar(hora1, hora2)):")
    hora_resultado.visualizar()

    # Demonstração adicional com virada de dia (passando de 23h)
    print("\n--- Teste adicional com passagem de 24 horas ---")
    h_noite = Hora(23, 50, 00)
    h_tempo = Hora(1, 15, 30)
    h_final = Hora()
    h_final.somar(h_noite, h_tempo)

    print(f"{h_noite} + {h_tempo} = {h_final}")


# Mantendo também o alias 'maim' referente ao erro tipográfico do enunciado original
maim = main


if __name__ == "__main__":
    main()
