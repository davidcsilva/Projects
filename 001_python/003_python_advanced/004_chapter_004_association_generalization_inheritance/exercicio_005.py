'''
17.5 Implemente uma classe Automóvel (Carro) dentro de uma hierarquia de herança múltipla. Considere que,
além de ser um Veículo, um automóvel é também uma comodidade, um símbolo de estado social, um meio de
transporte etc. Automóvel deve ter pelo menos três classes base e três classes derivadas.

'''


# ==============================================================================
# PARTE 1: AS 4 CLASSES BASE (SUPERCLASSES)
# ==============================================================================

class Veiculo:
    """Classe Base 1: Propriedades mecânicas e de locomoção."""

    def __init__(self, marca: str, modelo: str, ano: int, velocidade_maxima: int, **kwargs):
        super().__init__(**kwargs)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0
        self.motor_ligado = False

    def ligar_motor(self) -> str:
        self.motor_ligado = True
        return f"Motor do {self.marca} {self.modelo} ligado."

    def desligar_motor(self) -> str:
        self.velocidade_atual = 0
        self.motor_ligado = False
        return f"Motor do {self.marca} {self.modelo} desligado."

    def acelerar(self, incremento: int) -> int:
        if not self.motor_ligado:
            raise RuntimeError(
                "Não é possível acelerar com o motor desligado.")
        self.velocidade_atual = min(
            self.velocidade_maxima, self.velocidade_atual + incremento)
        return self.velocidade_atual


class Comodidade:
    """Classe Base 2: Recursos de conforto, climatização e entretenimento."""

    def __init__(self, ar_condicionado: bool = True, sistema_som: str = "Básico", **kwargs):
        super().__init__(**kwargs)
        self.ar_condicionado = ar_condicionado
        self.sistema_som = sistema_som
        self.temperatura_interna = 23

    def ajustar_climatizacao(self, graus: int) -> str:
        if not self.ar_condicionado:
            return "Este veículo não possui ar-condicionado."
        self.temperatura_interna = graus
        return f"Climatização ajustada para {self.temperatura_interna}°C (Som: {self.sistema_som})."


class SimboloStatus:
    """Classe Base 3: Valor patrimonial, prestígio social e exclusividade."""

    def __init__(self, valor_mercado: float, nivel_prestigio: str = "Padrão", **kwargs):
        super().__init__(**kwargs)
        self.valor_mercado = valor_mercado
        self.nivel_prestigio = nivel_prestigio

    def calcular_ipva_estimado(self) -> float:
        return self.valor_mercado * 0.04

    def exibir_prestigio(self) -> str:
        return f"Categoria de prestígio: {self.nivel_prestigio} | Valor: R$ {self.valor_mercado:,.2f}"


class MeioTransporte:
    """Classe Base 4: Capacidade de carga/passageiros e eficiência de deslocamento."""

    def __init__(self, capacidade_passageiros: int, capacidade_porta_malas_litros: int,
                 consumo_km_l: float, **kwargs):
        super().__init__(**kwargs)
        self.capacidade_passageiros = capacidade_passageiros
        self.capacidade_porta_malas_litros = capacidade_porta_malas_litros
        self.consumo_km_l = consumo_km_l
        self.ocupantes_atuais = 1

    def embarcar_passageiros(self, quantidade: int) -> str:
        if self.ocupantes_atuais + quantidade > self.capacidade_passageiros:
            raise ValueError(
                f"Capacidade máxima excedida ({self.capacidade_passageiros} lugares).")
        self.ocupantes_atuais += quantidade
        return f"Total de ocupantes a bordo: {self.ocupantes_atuais}/{self.capacidade_passageiros}."

    def calcular_custo_viagem(self, distancia_km: float, preco_combustivel: float) -> float:
        litros_necessarios = distancia_km / self.consumo_km_l
        return litros_necessarios * preco_combustivel


# ==============================================================================
# PARTE 2: CLASSE AUTOMÓVEL (HERANÇA MÚLTIPLA DAS 4 BASES)
# ==============================================================================

class Automovel(Veiculo, Comodidade, SimboloStatus, MeioTransporte):
    """Integra as características de Veículo, Comodidade, Símbolo de Status e Meio de Transporte."""

    def __init__(self, placa: str, **kwargs):
        super().__init__(**kwargs)
        self.placa = placa

    def ficha_tecnica(self) -> str:
        return (
            f"[{self.placa}] {self.marca} {self.modelo} ({self.ano}) | "
            f"Vel. Máx: {self.velocidade_maxima} km/h | "
            f"Lugares: {self.capacidade_passageiros} | "
            f"Consumo: {self.consumo_km_l} km/L | "
            f"{self.exibir_prestigio()}"
        )


# ==============================================================================
# PARTE 3: AS 3 CLASSES DERIVADAS DE AUTOMÓVEL
# ==============================================================================

class CarroPopular(Automovel):
    """Derivada 1: Focado em baixo custo operacional e uso diário urbano."""

    def __init__(self, placa: str, marca: str, modelo: str, ano: int, valor_mercado: float):
        super().__init__(
            placa=placa,
            marca=marca,
            modelo=modelo,
            ano=ano,
            velocidade_maxima=175,
            ar_condicionado=True,
            sistema_som="Rádio Bluetooth",
            valor_mercado=valor_mercado,
            nivel_prestigio="Econômico / Urbano",
            capacidade_passageiros=5,
            capacidade_porta_malas_litros=300,
            consumo_km_l=14.8,
        )
        self.modo_eco_ativo = True

    def alternar_modo_eco(self) -> str:
        self.modo_eco_ativo = not self.modo_eco_ativo
        ajuste = 1.1 if self.modo_eco_ativo else (1 / 1.1)
        self.consumo_km_l = round(self.consumo_km_l * ajuste, 2)
        estado = "ativado" if self.modo_eco_ativo else "desativado"
        return f"Modo ECO {estado}. Novo consumo médio: {self.consumo_km_l} km/L."


class SUV(Automovel):
    """Derivada 2: Focado em espaço familiar, conforto e tração integral."""

    def __init__(self, placa: str, marca: str, modelo: str, ano: int,
                 valor_mercado: float, tracao_4x4: bool = True):
        super().__init__(
            placa=placa,
            marca=marca,
            modelo=modelo,
            ano=ano,
            velocidade_maxima=210,
            ar_condicionado=True,
            sistema_som="Multimídia 10'' + Som Premium",
            valor_mercado=valor_mercado,
            nivel_prestigio="Executivo / Familiar",
            capacidade_passageiros=7,
            capacidade_porta_malas_litros=620,
            consumo_km_l=10.2,
        )
        self.tracao_4x4 = tracao_4x4
        self.modo_offroad = False

    def ativar_offroad(self) -> str:
        if not self.tracao_4x4:
            return "Este modelo não dispõe de tração 4x4."
        self.modo_offroad = True
        return f"{self.marca} {self.modelo}: Tração 4x4 e controle de descida ativados."


class CarroEsportivoLuxo(Automovel):
    """Derivada 3: Focado em desempenho extremo, exclusividade e status elevado."""

    def __init__(self, placa: str, marca: str, modelo: str, ano: int,
                 valor_mercado: float, potencia_cv: int):
        super().__init__(
            placa=placa,
            marca=marca,
            modelo=modelo,
            ano=ano,
            velocidade_maxima=330,
            ar_condicionado=True,
            sistema_som="Sistema Surround Hi-Fi 16 Alto-falantes",
            valor_mercado=valor_mercado,
            nivel_prestigio="Alto Luxo / Colecionador",
            capacidade_passageiros=2,
            capacidade_porta_malas_litros=135,
            consumo_km_l=6.5,
        )
        self.potencia_cv = potencia_cv
        self.modo_pista = False

    def ativar_modo_pista(self) -> str:
        self.modo_pista = True
        return (
            f"{self.marca} {self.modelo} ({self.potencia_cv} cv): "
            f"Suspensão rebaixada e escapamento esportivo abertos!"
        )


# ==============================================================================
# EXEMPLO DE EXECUÇÃO E VERIFICAÇÃO DO MRO
# ==============================================================================

if __name__ == "__main__":
    print("Ordem de Resolução de Métodos (MRO) de Automovel:")
    print(" -> ".join(cls.__name__ for cls in Automovel.__mro__))
    print("-" * 75)

    popular = CarroPopular("ABC-1234", "Fiat", "Argo", 2025, 85000.0)
    suv = SUV("XYZ-9876", "Toyota", "SW4", 2026, 380000.0, tracao_4x4=True)
    esportivo = CarroEsportivoLuxo(
        "LUX-0001", "Porsche", "911 Turbo S", 2026, 1650000.0, 650)

    for carro in (popular, suv, esportivo):
        print(carro.ficha_tecnica())
        print(f"  IPVA estimado: R$ {carro.calcular_ipva_estimado():,.2f}")
        print(
            f"  Custo viagem (300 km, gasolina R$ 6,00): R$ {carro.calcular_custo_viagem(300, 6.0):.2f}\n")

    # Testando métodos herdados das diferentes classes base e derivados
    print(esportivo.ligar_motor())
    print(f"Velocidade após acelerar: {esportivo.acelerar(140)} km/h")
    print(esportivo.ajustar_climatizacao(20))
    print(esportivo.ativar_modo_pista())
    print(suv.embarcar_passageiros(4))
    print(suv.ativar_offroad())
