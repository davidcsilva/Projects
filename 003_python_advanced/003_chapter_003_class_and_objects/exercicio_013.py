"""
Exercício 16.13:
Implemente a classe Hora. Cada objeto dessa classe representa uma hora específica do dia,
armazenando as horas, os minutos e segundos como inteiros.
Requisitos:
- Um construtor.
- Funções de acesso (getters e setters / properties).
- Uma função adiantar(int h, int m, int s) para adiantar a hora atual de um objeto existente.
- Uma função reiniciar(int h, int m, int s) que reinicializa a hora atual de um objeto existente.
- Uma função imprimir().
"""


class Hora:
    """
    Representa um horário específico do dia com horas, minutos e segundos inteiros.
    Garante valores válidos no formato de relógio de 24 horas (00:00:00 até 23:59:59).
    """

    def __init__(self, horas: int = 0, minutos: int = 0, segundos: int = 0) -> None:
        """
        Construtor da classe Hora.
        Inicializa o objeto com os valores fornecidos ou com 00:00:00 por padrão.
        """
        self._horas: int = 0
        self._minutos: int = 0
        self._segundos: int = 0
        self.reiniciar(horas, minutos, segundos)

    def _normalizar(self) -> None:
        """
        Normaliza segundos e minutos para o intervalo [0, 59] com propagação do 'vai-um'
        e ajusta as horas no formato de 24 horas [0, 23].
        """
        # Ajusta segundos excedentes
        if self._segundos >= 60 or self._segundos < 0:
            extra_min = self._segundos // 60
            self._segundos %= 60
            self._minutos += extra_min

        # Ajusta minutos excedentes
        if self._minutos >= 60 or self._minutos < 0:
            extra_h = self._minutos // 60
            self._minutos %= 60
            self._horas += extra_h

        # Ajusta horas no ciclo de 24 horas
        self._horas %= 24

    # --- Funções de Acesso (Properties / Getters e Setters) ---

    @property
    def horas(self) -> int:
        """Função de acesso para obter as horas."""
        return self._horas

    @horas.setter
    def horas(self, valor: int) -> None:
        """Função de acesso para definir as horas."""
        self._horas = int(valor)
        self._normalizar()

    @property
    def minutos(self) -> int:
        """Função de acesso para obter os minutos."""
        return self._minutos

    @minutos.setter
    def minutos(self, valor: int) -> None:
        """Função de acesso para definir os minutos."""
        self._minutos = int(valor)
        self._normalizar()

    @property
    def segundos(self) -> int:
        """Função de acesso para obter os segundos."""
        return self._segundos

    @segundos.setter
    def segundos(self, valor: int) -> None:
        """Função de acesso para definir os segundos."""
        self._segundos = int(valor)
        self._normalizar()

    # Métodos explícitos de acesso tradicionais (estilo Java/C++)
    def obter_horas(self) -> int:
        return self._horas

    def obter_minutos(self) -> int:
        return self._minutos

    def obter_segundos(self) -> int:
        return self._segundos

    def definir_horas(self, h: int) -> None:
        self.horas = h

    def definir_minutos(self, m: int) -> None:
        self.minutos = m

    def definir_segundos(self, s: int) -> None:
        self.segundos = s

    # --- Função reiniciar ---

    def reiniciar(self, h: int = 0, m: int = 0, s: int = 0) -> None:
        """
        Função membro 'reiniciar':
        Reinicializa a hora atual de um objeto existente para os novos valores informados.
        """
        self._horas = int(h)
        self._minutos = int(m)
        self._segundos = int(s)
        self._normalizar()

    # --- Função adiantar ---

    def adiantar(self, h: int = 0, m: int = 0, s: int = 0) -> None:
        """
        Função membro 'adiantar':
        Adiciona horas (h), minutos (m) e segundos (s) à hora atual do objeto,
        propagando corretamente os minutos, segundos e o ciclo de 24 horas.
        """
        self._horas += int(h)
        self._minutos += int(m)
        self._segundos += int(s)
        self._normalizar()

    # --- Função imprimir ---

    def imprimir(self) -> None:
        """
        Função membro 'imprimir':
        Exibe na tela a hora formatada no padrão clássico de relógio digital: HH:MM:SS.
        """
        print(f"{self._horas:02d}:{self._minutos:02d}:{self._segundos:02d}")

    # --- Métodos utilitários adicionais ---

    def __str__(self) -> str:
        return f"{self._horas:02d}:{self._minutos:02d}:{self._segundos:02d}"

    def __repr__(self) -> str:
        return f"Hora(horas={self._horas}, minutos={self._minutos}, segundos={self._segundos})"


# Alias conforme convenção
hora = Hora


def main() -> None:
    print("=== Exercício 16.13: Classe Hora com Métodos de Modificação ===")

    # 1. Criação com construtor (objeto inicializado em 10:30:45)
    relogio = Hora(10, 30, 45)
    print("1. Objeto criado com construtor Hora(10, 30, 45):")
    print("   Resultado de imprimir(): ", end="")
    relogio.imprimir()

    # 2. Uso das funções de acesso (getters e setters)
    print("\n2. Testando funções de acesso (Getters):")
    print(
        f"   Horas:    {relogio.horas} (via getter: {relogio.obter_horas()})")
    print(
        f"   Minutos:  {relogio.minutos} (via getter: {relogio.obter_minutos()})")
    print(
        f"   Segundos: {relogio.segundos} (via getter: {relogio.obter_segundos()})")

    print("\n   Modificando minutos para 50 via setter:")
    relogio.minutos = 50
    print("   Horário atualizado: ", end="")
    relogio.imprimir()

    # 3. Testando adiantar(h, m, s)
    print("\n3. Testando a função adiantar():")
    # Horário atual: 10:50:45
    # Adiantando 20 segundos -> deve virar 10:51:05
    print("   Adiantando 20 segundos -> adiantar(0, 0, 20):")
    relogio.adiantar(0, 0, 20)
    print("   Novo horário: ", end="")
    relogio.imprimir()

    # Adiantando 15 minutos -> 10:51:05 + 15m = 11:06:05
    print("\n   Adiantando 15 minutos -> adiantar(0, 15, 0):")
    relogio.adiantar(0, 15, 0)
    print("   Novo horário: ", end="")
    relogio.imprimir()

    # Adiantando 14 horas -> 11:06:05 + 14h = 25:06:05 % 24 = 01:06:05 (passagem de dia)
    print("\n   Adiantando 14 horas -> adiantar(14, 0, 0) (virada de 24h):")
    relogio.adiantar(14, 0, 0)
    print("   Novo horário: ", end="")
    relogio.imprimir()

    # 4. Testando reiniciar(h, m, s)
    print("\n4. Testando a função reiniciar(h, m, s):")
    print("   Reiniciando para 23:59:50:")
    relogio.reiniciar(23, 59, 50)
    print("   Horário após reiniciar: ", end="")
    relogio.imprimir()

    print("\n   Adiantando 15 segundos a partir de 23:59:50 -> adiantar(0, 0, 15):")
    relogio.adiantar(0, 0, 15)
    print("   Novo horário: ", end="")
    relogio.imprimir()

    # Reiniciando para meia-noite padrão (0, 0, 0)
    print("\n   Reiniciando com valores default -> reiniciar():")
    relogio.reiniciar()
    print("   Horário zerado: ", end="")
    relogio.imprimir()


if __name__ == "__main__":
    main()
