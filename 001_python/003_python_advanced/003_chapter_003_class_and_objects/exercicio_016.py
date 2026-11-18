"""
Exercício 16.16:
Amplie o programa da classe Data (exercício anterior) de maneira que possa aceitar anos bissextos.
Regra formal de ano bissexto:
- Um ano é bissexto se é divisível por 400, ou se é divisível por 4 mas não por 100.
Exemplos do enunciado:
- 1992 e 2000: SÃO bissextos (fevereiro tem 29 dias).
- 1997 e 1900: NÃO são bissextos (fevereiro tem 28 dias).
"""

from typing import Optional, Union


class Data:
    """
    Representa uma data com suporte completo ao cálculo e regras de anos bissextos
    no calendário gregoriano.
    """

    # Número de dias por mês em anos comuns (não-bissextos)
    _DIAS_MES_COMUM: list[int] = [0, 31, 28,
                                  31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(
        self,
        dia_ou_copia: Union[int, "Data"] = 1,
        mes: int = 1,
        ano: int = 2000,
    ) -> None:
        """
        Construtor da classe:
        - Construtor de cópia: Data(outra_data)
        - Construtor padrão/parametrizado: Data(dia, mes, ano)
        """
        self._dia: int = 1
        self._mes: int = 1
        self._ano: int = 1

        if isinstance(dia_ou_copia, Data):
            self._dia = dia_ou_copia._dia
            self._mes = dia_ou_copia._mes
            self._ano = dia_ou_copia._ano
        else:
            self.reiniciar(dia_ou_copia, mes, ano)

    # --- Verificação de Ano Bissexto ---

    @staticmethod
    def eh_bissexto_ano(ano: int) -> bool:
        """
        Método estático para verificar se um dado ano é bissexto.
        Regra:
        (ano % 400 == 0) ou (ano % 4 == 0 e ano % 100 != 0)
        """
        return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

    def eh_bissexto(self) -> bool:
        """
        Função membro que verifica se o ano desta instância é bissexto.
        """
        return Data.eh_bissexto_ano(self._ano)

    # Alias sem acento
    bissexto = eh_bissexto

    # --- Função dias do mês ---

    def dias(self, mes: Optional[int] = None, ano: Optional[int] = None) -> int:
        """
        Retorna a quantidade de dias do mês solicitado (ou do mês atual do objeto),
        considerando fevereiro com 29 dias em anos bissextos e 28 em anos comuns.
        """
        m = self._mes if mes is None else mes
        a = self._ano if ano is None else ano

        if m == 2:
            return 29 if Data.eh_bissexto_ano(a) else 28

        if 1 <= m <= 12:
            return self._DIAS_MES_COMUM[m]

        return 30

    # --- Função de Normalização ---

    def normalizar(self) -> None:
        """
        Função de utilidade 'normalizar':
        Garante que dia, mês e ano obedeçam rigorosamente às regras do calendário:
        - ano >= 1
        - 1 <= mes <= 12
        - 1 <= dia <= dias(mes, ano)
        Propaga adequadamente excessos de dias entre meses e anos.
        """
        if self._ano < 1:
            self._ano = 1

        # 1. Normalização dos meses
        if self._mes > 12:
            anos_a_somar = (self._mes - 1) // 12
            self._ano += anos_a_somar
            self._mes = ((self._mes - 1) % 12) + 1
        elif self._mes < 1:
            anos_a_subtrair = (abs(self._mes) // 12) + 1
            self._ano = max(1, self._ano - anos_a_subtrair)
            self._mes = 12 - (abs(self._mes) % 12)

        # 2. Normalização dos dias para frente
        while self._dia > self.dias(self._mes, self._ano):
            dias_no_mes = self.dias(self._mes, self._ano)
            self._dia -= dias_no_mes
            self._mes += 1
            if self._mes > 12:
                self._mes = 1
                self._ano += 1

        # 3. Normalização dos dias para trás
        while self._dia < 1:
            self._mes -= 1
            if self._mes < 1:
                self._mes = 12
                self._ano = max(1, self._ano - 1)
            self._dia += self.dias(self._mes, self._ano)

    # --- Funções de Acesso ---

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

    # --- Funções de Manipulação da Data ---

    def reiniciar(self, d: int = 1, m: int = 1, a: int = 2000) -> None:
        """Reinicia a data do objeto existente com novos valores."""
        self._dia = int(d)
        self._mes = int(m)
        self._ano = int(a)
        self.normalizar()

    def adiantar(self, d: int = 0, m: int = 0, a: int = 0) -> None:
        """Avança a data em dias, meses e anos."""
        self._ano += int(a)
        self._mes += int(m)
        self._dia += int(d)
        self.normalizar()

    def imprimir(self) -> None:
        """Exibe a data formatada no padrão DD/MM/AAAA."""
        print(f"{self._dia:02d}/{self._mes:02d}/{self._ano:04d}")

    # --- Métodos Utilitários e Sobrecarga de Operadores ---

    def __str__(self) -> str:
        return f"{self._dia:02d}/{self._mes:02d}/{self._ano:04d}"

    def __repr__(self) -> str:
        return f"Data(dia={self._dia}, mes={self._mes}, ano={self._ano})"

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Data):
            return False
        return (self._dia, self._mes, self._ano) == (outro._dia, outro._mes, outro._ano)

    def __lt__(self, outro: "Data") -> bool:
        return (self._ano, self._mes, self._dia) < (outro._ano, outro._mes, outro._dia)

    def __le__(self, outro: "Data") -> bool:
        return (self._ano, self._mes, self._dia) <= (outro._ano, outro._mes, outro._dia)


# Alias conforme convenção
data = Data


def main() -> None:
    print("=== Exercício 16.16: Classe Data com Suporte a Anos Bissextos ===")

    # 1. Validação dos anos citados explicitamente no enunciado
    print("\n--- 1. Validação dos Anos Citados no Enunciado ---")
    anos_teste = [1992, 2000, 1997, 1900]
    for a in anos_teste:
        bissexto = Data.eh_bissexto_ano(a)
        explicacao = (
            "Divisível por 400"
            if a % 400 == 0
            else (
                "Divisível por 4 e não por 100"
                if a % 4 == 0 and a % 100 != 0
                else (
                    "Divisível por 100 mas NÃO por 400"
                    if a % 100 == 0
                    else "Não divisível por 4"
                )
            )
        )
        status = "BISSEXTO (29 dias em fev)" if bissexto else "NÃO BISSEXTO (28 dias em fev)"
        print(f"  Ano {a:4d}: {status:<30} -> Motivo: {explicacao}")

    # 2. Testando a virada de 28 para 29 de fevereiro em anos bissextos vs não bissextos
    print("\n--- 2. Comportamento ao adiantar 1 dia a partir de 28 de fevereiro ---")

    # Caso A: Ano 2000 (bissexto) -> deve ir para 29/02/2000
    d_2000 = Data(28, 2, 2000)
    print(f"  Data inicial: {d_2000} (Ano 2000 é bissexto)")
    d_2000.adiantar(d=1)
    print(f"  Após adiantar 1 dia: {d_2000} (esperado: 29/02/2000)")
    d_2000.adiantar(d=1)
    print(f"  Após adiantar mais 1 dia: {d_2000} (esperado: 01/03/2000)\n")

    # Caso B: Ano 1900 (não bissexto) -> deve pular direto para 01/03/1900
    d_1900 = Data(28, 2, 1900)
    print(f"  Data inicial: {d_1900} (Ano 1900 NÃO é bissexto)")
    d_1900.adiantar(d=1)
    print(f"  Após adiantar 1 dia: {d_1900} (esperado: 01/03/1900)\n")

    # Caso C: Ano 1992 (bissexto)
    d_1992 = Data(28, 2, 1992)
    print(f"  Data inicial: {d_1992} (Ano 1992 é bissexto)")
    d_1992.adiantar(d=1)
    print(f"  Após adiantar 1 dia: {d_1992} (esperado: 29/02/1992)\n")

    # Caso D: Ano 1997 (não bissexto)
    d_1997 = Data(28, 2, 1997)
    print(f"  Data inicial: {d_1997} (Ano 1997 NÃO é bissexto)")
    d_1997.adiantar(d=1)
    print(f"  Após adiantar 1 dia: {d_1997} (esperado: 01/03/1997)")

    # 3. Teste de tentativa de atribuir 29/02 a um ano comum
    print("\n--- 3. Tentativa de atribuir 29/02 em ano comum (normalização automática) ---")
    d_ajuste = Data(29, 2, 2023)  # 2023 não é bissexto
    print(
        f"  Data(29, 2, 2023) normalizada automaticamente para: {d_ajuste} (esperado: 01/03/2023)")


if __name__ == "__main__":
    main()
