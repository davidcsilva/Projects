"""
Exercício 16.15:
Implemente uma classe Data com membros de dados para o dia, mês e ano.
Requisitos:
- Construtor por default e construtor de cópia.
- Funções de acesso (getters e setters).
- Função dias(mes) que devolve o número de dias de cada mês (tratando anos bissextos).
- Função de utilidade normalizar() que assegura que os membros estão na gama correta:
  ano >= 1, 1 <= mês <= 12, 1 <= dia <= dias(mês).
- Função reiniciar(int d, int m, int a) para reiniciar a data de um objeto existente.
- Função adiantar(int d, int m, int a) para avançar a data atual.
- Função imprimir().
"""

from typing import Optional, Union


class Data:
    """
    Representa uma data no calendário gregoriano com dia, mês e ano inteiros.
    """

    # Dias em cada mês em ano não-bissexto (índice 1 = janeiro, ..., 12 = dezembro)
    _DIAS_POR_MES: list[int] = [0, 31, 28, 31,
                                30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(
        self,
        dia_ou_copia: Union[int, "Data"] = 1,
        mes: int = 1,
        ano: int = 2000,
    ) -> None:
        """
        Construtor polimórfico:
        - Construtor de Cópia: Data(outra_data)
        - Construtor Padrão (Default): Data() -> 01/01/2000
        - Construtor Parametrizado: Data(dia, mes, ano)
        """
        self._dia: int = 1
        self._mes: int = 1
        self._ano: int = 1

        if isinstance(dia_ou_copia, Data):
            # Construtor de cópia
            self._dia = dia_ou_copia._dia
            self._mes = dia_ou_copia._mes
            self._ano = dia_ou_copia._ano
        else:
            self.reiniciar(dia_ou_copia, mes, ano)

    @classmethod
    def copia(cls, outra: "Data") -> "Data":
        """Método de fábrica explícito para o construtor de cópia."""
        return cls(outra)

    # --- Função que devolve os dias de cada mês ---

    def eh_bissexto(self, ano: Optional[int] = None) -> bool:
        """Verifica se o ano informado (ou o ano da instância) é bissexto."""
        a = self._ano if ano is None else ano
        return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

    def dias(self, mes: Optional[int] = None, ano: Optional[int] = None) -> int:
        """
        Função membro 'dias':
        Devolve o número de dias do mês especificado (ou do mês atual da instância),
        considerando anos bissextos para fevereiro (29 dias).
        """
        m = self._mes if mes is None else mes
        a = self._ano if ano is None else ano

        if m == 2 and self.eh_bissexto(a):
            return 29
        if 1 <= m <= 12:
            return self._DIAS_POR_MES[m]
        return 30

    # --- Função de Utilidade normalizar() ---

    def normalizar(self) -> None:
        """
        Função de utilidade 'normalizar':
        Assegura que os membros de dados estejam na gama correta:
        ano >= 1, 1 <= mês <= 12, 1 <= dia <= dias(mês).
        Propaga adequadamente excessos de dias para meses e excessos de meses para anos.
        """
        # Garante ano positivo
        if self._ano < 1:
            self._ano = 1

        # 1. Normaliza meses se self._mes > 12 ou self._mes < 1
        if self._mes > 12:
            anos_extras = (self._mes - 1) // 12
            self._ano += anos_extras
            self._mes = ((self._mes - 1) % 12) + 1
        elif self._mes < 1:
            anos_menos = (abs(self._mes) // 12) + 1
            self._ano = max(1, self._ano - anos_menos)
            self._mes = 12 - (abs(self._mes) % 12)

        # 2. Normaliza dias se self._dia exceder os dias do mês atual
        while self._dia > self.dias(self._mes, self._ano):
            dias_no_mes = self.dias(self._mes, self._ano)
            self._dia -= dias_no_mes
            self._mes += 1
            if self._mes > 12:
                self._mes = 1
                self._ano += 1

        # Trata dias negativos ou zero retrocedendo meses
        while self._dia < 1:
            self._mes -= 1
            if self._mes < 1:
                self._mes = 12
                self._ano = max(1, self._ano - 1)
            self._dia += self.dias(self._mes, self._ano)

    # --- Funções de Acesso (Properties / Getters e Setters) ---

    @property
    def dia(self) -> int:
        return self._dia

    @dia.setter
    def dia(self, valor: int) -> None:
        self._dia = int(valor)
        self.normalizar()

    @property
    def mes(self) -> int:
        return self._mes

    @mes.setter
    def mes(self, valor: int) -> None:
        self._mes = int(valor)
        self.normalizar()

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, valor: int) -> None:
        self._ano = int(valor)
        self.normalizar()

    # Métodos explícitos de acesso tradicionais
    def obter_dia(self) -> int:
        return self._dia

    def obter_mes(self) -> int:
        return self._mes

    def obter_ano(self) -> int:
        return self._ano

    # --- Função reiniciar ---

    def reiniciar(self, d: int = 1, m: int = 1, a: int = 2000) -> None:
        """
        Função membro 'reiniciar':
        Reinicializa a data de um objeto existente para os novos valores informados.
        """
        self._dia = int(d)
        self._mes = int(m)
        self._ano = int(a)
        self.normalizar()

    # --- Função adiantar ---

    def adiantar(self, d: int = 0, m: int = 0, a: int = 0) -> None:
        """
        Função membro 'adiantar':
        Avança a data atual adicionando 'd' dias, 'm' meses e 'a' anos,
        normalizando o calendário após a operação.
        """
        self._ano += int(a)
        self._mes += int(m)
        self._dia += int(d)
        self.normalizar()

    # --- Função imprimir ---

    def imprimir(self) -> None:
        """
        Função membro 'imprimir':
        Efetua a visualização formatada da data no padrão brasileiro DD/MM/AAAA.
        """
        print(f"{self._dia:02d}/{self._mes:02d}/{self._ano:04d}")

    def __str__(self) -> str:
        return f"{self._dia:02d}/{self._mes:02d}/{self._ano:04d}"

    def __repr__(self) -> str:
        return f"Data(dia={self._dia}, mes={self._mes}, ano={self._ano})"

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Data):
            return False
        return (self._dia, self._mes, self._ano) == (outro._dia, outro._mes, outro._ano)


# Alias conforme convenção
data = Data


def main() -> None:
    print("=== Exercício 16.15: Classe Data Completa ===")

    # 1. Testando construtor por default e parametrizado
    d_padrao = Data()
    print("1. Data criada com construtor por default:")
    print("   d_padrao.imprimir(): ", end="")
    d_padrao.imprimir()

    d1 = Data(28, 2, 2024)  # 2024 é ano bissexto
    print(
        f"\n2. Data criada: {d1} (Ano bissexto? {d1.eh_bissexto()} | Dias em fev/2024: {d1.dias()})")

    # 2. Testando construtor de cópia
    print("\n3. Testando construtor de cópia Data(d1):")
    d_copia = Data(d1)
    print(f"   Original d1: {d1} (id: {id(d1)})")
    print(f"   Cópia:       {d_copia} (id: {id(d_copia)})")
    print(
        f"   São iguais em valor? {d1 == d_copia} | São o mesmo objeto na memória? {d1 is d_copia}")

    # 3. Testando funções de acesso
    print("\n4. Testando funções de acesso (Getters e Setters):")
    print(f"   Dia: {d1.dia} | Mês: {d1.mes} | Ano: {d1.ano}")
    print("   Alterando o dia de d1 para 15 via setter:")
    d1.dia = 15
    print(f"   d1 atualizado: {d1}")

    # 4. Testando a função adiantar()
    print("\n5. Testando a função adiantar():")
    # Começando em 15/02/2024
    print(f"   Data base: {d1}")

    # Adiantando 15 dias -> deve ir para 01/03/2024 (fev/2024 tem 29 dias)
    print("   Adiantando 15 dias -> adiantar(d=15, m=0, a=0):")
    d1.adiantar(d=15)
    print(f"   Resultado: {d1} (esperado: 01/03/2024)")

    # Adiantando 10 meses -> 01/03/2024 + 10 meses = 01/01/2025
    print("\n   Adiantando 10 meses -> adiantar(d=0, m=10, a=0):")
    d1.adiantar(m=10)
    print(f"   Resultado: {d1} (esperado: 01/01/2025)")

    # Adiantando 60 dias a partir de 01/01/2025 (ano comum: jan=31, fev=28) -> 02/03/2025
    print("\n   Adiantando 60 dias em ano comum -> adiantar(d=60):")
    d1.adiantar(d=60)
    print(f"   Resultado: {d1} (esperado: 02/03/2025)")

    # 5. Testando a função reiniciar(d, m, a)
    print("\n6. Testando reiniciar():")
    print("   Reiniciando d1 para 31/12/2026:")
    d1.reiniciar(31, 12, 2026)
    print(f"   d1 após reiniciar: {d1}")

    print("\n   Adiantando 1 dia a partir de 31/12/2026:")
    d1.adiantar(d=1)
    print(f"   Resultado (virada de ano): {d1} (esperado: 01/01/2027)")


if __name__ == "__main__":
    main()
