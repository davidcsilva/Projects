'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.15

Enunciado:
Declarar uma classe Data com os dados fundamentais de um dia do ano e que pelo
menos tenha um método que permita aceitar dois valores de datas diferentes e
devolva a data mais próxima do dia atual.
'''

from datetime import date


class Data:
    """
    Representa uma data com os dados fundamentais de um dia do ano (Dia, Mês, Ano).

    Inclui:
    - Validação de dias por mês considerando anos bissextos;
    - Operações de diferença e distância absoluta em dias entre duas datas;
    - Método para obter a data atual do sistema (hoje);
    - Método principal: aceita duas datas diferentes e retorna a mais próxima do dia atual.
    """

    DIAS_POR_MES = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, dia: int = 1, mes: int = 1, ano: int = 2026) -> None:
        """Inicializa e valida os dados fundamentais da data."""
        if not self.data_valida(dia, mes, ano):
            raise ValueError(f"Data inválida: {dia:02d}/{mes:02d}/{ano}.")
        self._dia = int(dia)
        self._mes = int(mes)
        self._ano = int(ano)

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
    # Validações e Cálculos de Calendário
    # --------------------------------------------------------------------------
    @staticmethod
    def eh_bissexto(ano: int) -> bool:
        """Regra do ano bissexto no calendário gregoriano."""
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    @classmethod
    def dias_no_mes(cls, mes: int, ano: int) -> int:
        if not (1 <= mes <= 12):
            return 0
        if mes == 2 and cls.eh_bissexto(ano):
            return 29
        return cls.DIAS_POR_MES[mes]

    @classmethod
    def data_valida(cls, dia: int, mes: int, ano: int) -> bool:
        if ano < 1 or not (1 <= mes <= 12):
            return False
        return 1 <= dia <= cls.dias_no_mes(mes, ano)

    # --------------------------------------------------------------------------
    # Fábrica: Data Atual (Hoje)
    # --------------------------------------------------------------------------
    @classmethod
    def hoje(cls) -> "Data":
        """Cria e retorna uma instância com a data atual do sistema."""
        atual = date.today()
        return cls(atual.day, atual.month, atual.year)

    # --------------------------------------------------------------------------
    # Cálculo de Dias Absolutos (Rata Die) para Diferenças Exatas
    # --------------------------------------------------------------------------
    def para_dias_absolutos(self) -> int:
        """
        Converte a data para um número absoluto de dias desde o ano 1 (Rata Die),
        permitindo calcular distâncias exatas entre quaisquer datas.
        """
        y = self._ano
        m = self._mes
        d = self._dia

        # Ajuste de anos e meses para contagem contínua
        if m <= 2:
            y -= 1
            m += 12

        dias = (
            365 * y +
            (y // 4) -
            (y // 100) +
            (y // 400) +
            (153 * (m + 1)) // 5 +
            d - 428
        )
        return dias

    def distancia_em_dias(self, outra: "Data") -> int:
        """Retorna o valor absoluto da distância em dias entre duas datas."""
        return abs(self.para_dias_absolutos() - outra.para_dias_absolutos())

    def __sub__(self, outra: "Data") -> int:
        """Sobrecarga do operador '-': d1 - d2 retorna a diferença em dias."""
        return self.para_dias_absolutos() - outra.para_dias_absolutos()

    # --------------------------------------------------------------------------
    # Método Solicitado: Devolve a data mais próxima do dia atual
    # --------------------------------------------------------------------------
    @classmethod
    def data_mais_proxima(
        cls,
        data1: "Data",
        data2: "Data",
        referencia: "Data | None" = None
    ) -> "Data":
        """
        Aceita dois valores de datas diferentes e devolve a data mais próxima
        do dia atual (ou de uma data de referência especificada).

        Se houver empate (equidistantes no passado e no futuro), retorna data1
        com aviso de equidistância.
        """
        alvo = referencia if referencia is not None else cls.hoje()

        distancia1 = alvo.distancia_em_dias(data1)
        distancia2 = alvo.distancia_em_dias(data2)

        print(f"[Comparação] Data Alvo (Hoje): {alvo}")
        print(f"  -> Data 1: {data1} | Distância: {distancia1} dia(s)")
        print(f"  -> Data 2: {data2} | Distância: {distancia2} dia(s)")

        if distancia1 < distancia2:
            print(f"  ==> {data1} é a mais próxima de {alvo}!")
            return data1
        elif distancia2 < distancia1:
            print(f"  ==> {data2} é a mais próxima de {alvo}!")
            return data2
        else:
            print(
                f"  ==> Ambas as datas são equidistantes ({distancia1} dias de diferença).")
            return data1

    def mais_proxima_de_mim(self, data1: "Data", data2: "Data") -> "Data":
        """Versão de método de instância: compara em relação a self."""
        return self.data_mais_proxima(data1, data2, referencia=self)

    # --------------------------------------------------------------------------
    # Representação Textual e Comparações
    # --------------------------------------------------------------------------
    def __str__(self) -> str:
        return f"{self._dia:02d}/{self._mes:02d}/{self._ano:04d}"

    def __repr__(self) -> str:
        return f"Data({self._dia}, {self._mes}, {self._ano})"

    def __eq__(self, outra: object) -> bool:
        if not isinstance(outra, Data):
            return False
        return (self._dia, self._mes, self._ano) == (outra._dia, outra._mes, outra._ano)

    def __lt__(self, outra: "Data") -> bool:
        return (self._ano, self._mes, self._dia) < (outra._ano, outra._mes, outra._dia)


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    hoje = Data.hoje()
    print(f"=== Data Atual do Sistema: {hoje} ===\n")

    # Exemplo 1: Uma data recente no passado vs. uma data futura distante
    d1 = Data(15, 11, 2026)   # Poucos dias antes de 18/11/2026
    d2 = Data(25, 12, 2026)   # Natal (mais de 1 mês à frente)
    print("--- Cenário 1 ---")
    mais_prox = Data.data_mais_proxima(d1, d2)
    print(f"Resultado retornado: {mais_prox}\n")

    # Exemplo 2: Uma data daqui a 3 dias vs. uma data de 10 dias atrás
    d3 = Data(21, 11, 2026)   # 3 dias no futuro
    d4 = Data(5, 11, 2026)    # 13 dias no passado
    print("--- Cenário 2 ---")
    mais_prox2 = Data.data_mais_proxima(d3, d4)
    print(f"Resultado retornado: {mais_prox2}\n")

    # Exemplo 3: Usando método de instância
    print("--- Cenário 3 (Método de Instância) ---")
    data_evento = Data(1, 1, 2027)  # Ano Novo 2027
    opcao_a = Data(28, 12, 2026)    # 4 dias antes
    opcao_b = Data(10, 1, 2027)     # 9 dias depois
    mais_prox_evento = data_evento.mais_proxima_de_mim(opcao_a, opcao_b)
    print(f"Mais próxima do Réveillon: {mais_prox_evento}")
