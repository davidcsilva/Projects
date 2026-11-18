'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.8

Enunciado:
Construir uma classe Data que permita verificar que todos os dias úteis estão
compreendidos entre 1 e 31, mas considerando todos os meses do ano. A classe
deverá ter entre suas funções a possibilidade de calcular a data do dia seguinte
e assim mesmo decidir se o ano em questão é ou não bissexto.
'''


class Data:
    """
    Classe que representa uma data no calendário gregoriano (Dia, Mês, Ano).

    Funcionalidades:
    - Validação de dias por mês (considerando meses de 28, 29, 30 e 31 dias);
    - Verificação de ano bissexto;
    - Cálculo da data do dia seguinte (virada de mês e de ano);
    - Verificação de dia útil (segunda a sexta-feira);
    - Formatação visual amigável (DD/MM/AAAA).
    """

    # Dias por mês em anos normais (índice 0 não utilizado para alinhar mês 1..12)
    DIAS_POR_MES = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    NOMES_MESES = [
        "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    DIAS_DA_SEMANA = [
        "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira",
        "Quinta-feira", "Sexta-feira", "Sábado"
    ]

    def __init__(self, dia: int = 1, mes: int = 1, ano: int = 2026) -> None:
        """
        Construtor da classe Data.
        Valida se os valores informados constituem uma data válida no calendário.
        """
        if not self.data_valida(dia, mes, ano):
            dias_max = self.dias_no_mes(mes, ano) if 1 <= mes <= 12 else 31
            raise ValueError(
                f"Data inválida: {dia:02d}/{mes:02d}/{ano}. "
                f"Para o mês {mes}, o dia deve estar entre 1 e {dias_max}."
            )

        self._dia = dia
        self._mes = mes
        self._ano = ano

    # --------------------------------------------------------------------------
    # Propriedades de Acesso
    # --------------------------------------------------------------------------
    @property
    def dia(self) -> int:
        return self._dia

    @property
    def mes(self) -> int:
        return self._mes

    @property
    def ano(self) -> int:
        return self._ano

    # --------------------------------------------------------------------------
    # 1. Verificação de Ano Bissexto
    # --------------------------------------------------------------------------
    @staticmethod
    def ano_bissexto(ano: int) -> bool:
        """
        Verifica se um ano específico é bissexto de acordo com o calendário gregoriano:
        - Divisível por 4 E NÃO divisível por 100; OU
        - Divisível por 400.
        """
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    def eh_bissexto(self) -> bool:
        """Determina se o ano da instância atual é bissexto."""
        return self.ano_bissexto(self._ano)

    # --------------------------------------------------------------------------
    # 2. Validação dos Dias Considerando Todos os Meses do Ano
    # --------------------------------------------------------------------------
    @classmethod
    def dias_no_mes(cls, mes: int, ano: int) -> int:
        """Retorna a quantidade máxima de dias para um mês e ano específicos."""
        if not (1 <= mes <= 12):
            return 0
        if mes == 2 and cls.ano_bissexto(ano):
            return 29
        return cls.DIAS_POR_MES[mes]

    @classmethod
    def data_valida(cls, dia: int, mes: int, ano: int) -> bool:
        """
        Valida se uma data é consistente:
        - Ano deve ser maior ou igual a 1;
        - Mês deve estar entre 1 e 12;
        - Dia deve estar entre 1 e o limite específico daquele mês/ano.
        """
        if ano < 1:
            return False
        if not (1 <= mes <= 12):
            return False
        max_dias = cls.dias_no_mes(mes, ano)
        return 1 <= dia <= max_dias

    # --------------------------------------------------------------------------
    # 3. Cálculo da Data do Dia Seguinte
    # --------------------------------------------------------------------------
    def dia_seguinte(self) -> "Data":
        """
        Calcula e retorna uma nova instância de Data representando o dia seguinte,
        tratando automaticamente viradas de mês e de ano.
        """
        dia = self._dia
        mes = self._mes
        ano = self._ano

        max_dias = self.dias_no_mes(mes, ano)

        if dia < max_dias:
            dia += 1
        else:
            # Virada de mês
            dia = 1
            if mes < 12:
                mes += 1
            else:
                # Virada de ano
                mes = 1
                ano += 1

        return Data(dia, mes, ano)

    def avancar_um_dia(self) -> None:
        """Modifica a data atual avançando-a para o dia seguinte."""
        proxima = self.dia_seguinte()
        self._dia = proxima.dia
        self._mes = proxima.mes
        self._ano = proxima.ano

    # --------------------------------------------------------------------------
    # 4. Verificação de Dias Úteis e Dia da Semana
    # --------------------------------------------------------------------------
    def dia_da_semana(self) -> str:
        """
        Calcula o dia da semana utilizando a congruência de Zeller.
        Retorna: 'Domingo', 'Segunda-feira', ..., 'Sábado'.
        """
        q = self._dia
        m = self._mes
        y = self._ano

        # Na congruência de Zeller, Janeiro e Fevereiro contam como meses 13 e 14 do ano anterior
        if m in (1, 2):
            m += 12
            y -= 1

        k = y % 100
        j = y // 100

        # Fórmula de Zeller para calendário gregoriano (h: 0 = Sábado, 1 = Domingo, ..., 6 = Sexta)
        h = (q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7

        # Mapeamento do resultado: h=0 (Sábado), h=1 (Domingo), h=2 (Segunda), ...
        dias_zeller = {
            0: "Sábado",
            1: "Domingo",
            2: "Segunda-feira",
            3: "Terça-feira",
            4: "Quarta-feira",
            5: "Quinta-feira",
            6: "Sexta-feira"
        }
        return dias_zeller[h]

    def eh_dia_util(self) -> bool:
        """
        Verifica se a data em questão é um dia útil (Segunda a Sexta-feira),
        excluindo fins de semana (Sábado e Domingo).
        """
        dia_sem = self.dia_da_semana()
        return dia_sem not in ("Sábado", "Domingo")

    # --------------------------------------------------------------------------
    # Representação Textual e Operadores
    # --------------------------------------------------------------------------
    def __str__(self) -> str:
        return f"{self._dia:02d}/{self._mes:02d}/{self._ano:04d}"

    def __repr__(self) -> str:
        return f"Data(dia={self._dia}, mes={self._mes}, ano={self._ano})"

    def formato_longo(self) -> str:
        """Retorna formato expandido: '18 de Novembro de 2026 (Quarta-feira)'."""
        nome_mes = self.NOMES_MESES[self._mes]
        dia_sem = self.dia_da_semana()
        return f"{self._dia:02d} de {nome_mes} de {self._ano:04d} ({dia_sem})"


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    print("=== 1. Teste de Validação e Anos Bissextos ===")
    d1 = Data(28, 2, 2024)
    print(f"Data: {d1} -> Ano {d1.ano} é bissexto? {d1.eh_bissexto()}")

    # 2024 é bissexto: 29 de fevereiro é válido
    d2 = Data(29, 2, 2024)
    print(f"Data bissexta válida: {d2.formato_longo()}")

    # 2025 NÃO é bissexto: testando captura de erro
    try:
        Data(29, 2, 2025)
    except ValueError as e:
        print(f"[Tratamento de Exceção]: {e}")

    # Mês com 30 dias (Abril) não aceita 31
    try:
        Data(31, 4, 2026)
    except ValueError as e:
        print(f"[Tratamento de Exceção]: {e}")

    print("\n=== 2. Teste do Cálculo do Dia Seguinte ===")
    # Caso A: dia normal dentro do mês
    dt = Data(15, 8, 2026)
    print(f"Atual: {dt} -> Dia seguinte: {dt.dia_seguinte()}")

    # Caso B: virada de mês (31 de Março -> 1 de Abril)
    fim_marco = Data(31, 3, 2026)
    print(f"Atual: {fim_marco} -> Dia seguinte: {fim_marco.dia_seguinte()}")

    # Caso C: virada de Fevereiro em ano bissexto (28/02/2024 -> 29/02/2024 -> 01/03/2024)
    fev_bissexto = Data(28, 2, 2024)
    dia29 = fev_bissexto.dia_seguinte()
    dia01 = dia29.dia_seguinte()
    print(
        f"Atual: {fev_bissexto} -> Dia seguinte: {dia29} -> Dia seguinte: {dia01}")

    # Caso D: virada de ano (31 de Dezembro -> 1 de Janeiro do ano seguinte)
    fim_ano = Data(31, 12, 2026)
    ano_novo = fim_ano.dia_seguinte()
    print(f"Atual: {fim_ano} -> Dia seguinte (Ano Novo!): {ano_novo}")

    print("\n=== 3. Teste de Verificação de Dias Úteis ===")
    datas_teste = [
        Data(18, 11, 2026),  # Quarta-feira
        Data(20, 11, 2026),  # Sexta-feira
        Data(21, 11, 2026),  # Sábado
        Data(22, 11, 2026),  # Domingo
        Data(23, 11, 2026),  # Segunda-feira
    ]

    for d in datas_teste:
        util = "Sim (Dia Útil)" if d.eh_dia_util() else "Não (Fim de semana)"
        print(f"{d.formato_longo()} -> Dia útil? {util}")
