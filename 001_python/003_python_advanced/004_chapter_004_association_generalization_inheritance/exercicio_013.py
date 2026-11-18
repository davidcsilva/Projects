'''
17.13 Projete um diagrama de objetos que represente a estrutura de um carro. Indique as possíveis relações de
associação, generalização e agregação.


'''

# ==============================================================================
# 1. GENERALIZAÇÃO (HERANÇA: Veiculo -> Carro / Motor -> Combustão e Elétrico)
# ==============================================================================


class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0.0

    def ligar(self) -> str:
        self.ligado = True
        return f"{self.marca} {self.modelo} está LIGADO."

    def desligar(self) -> str:
        self.velocidade = 0.0
        self.ligado = False
        return f"{self.marca} {self.modelo} está DESLIGADO."


class Motor:
    def __init__(self, potencia_cv: int):
        self.potencia_cv = potencia_cv


class MotorCombustao(Motor):
    def __init__(self, potencia_cv: int, combustivel: str):
        super().__init__(potencia_cv)
        self.combustivel = combustivel

    def __str__(self) -> str:
        return f"Combustão ({self.potencia_cv} cv, {self.combustivel})"


class MotorEletrico(Motor):
    def __init__(self, potencia_cv: int, bateria_kwh: float):
        super().__init__(potencia_cv)
        self.bateria_kwh = bateria_kwh

    def __str__(self) -> str:
        return f"Elétrico ({self.potencia_cv} cv, bateria {self.bateria_kwh} kWh)"


# ==============================================================================
# 2. COMPOSIÇÃO E AGREGAÇÃO (Partes do Carro)
# ==============================================================================

class Chassi:
    """Composição: nasce e morre junto com o Carro."""

    def __init__(self, numero_serie: str, material: str = "Aço de alta resistência"):
        self.numero_serie = numero_serie
        self.material = material


class Roda:
    """Agregação: existe de forma independente e pode ser substituída."""

    def __init__(self, aro: int, pressao_psi: float = 32.0):
        self.aro = aro
        self.pressao_psi = pressao_psi


class SistemaMultimidia:
    """Agregação: componente opcional e removível."""

    def __init__(self, marca_aparelho: str, tela_polegadas: float):
        self.marca_aparelho = marca_aparelho
        self.tela_polegadas = tela_polegadas


# ==============================================================================
# 3. CLASSE PRINCIPAL (CARRO) E ASSOCIAÇÃO (MOTORISTA)
# ==============================================================================

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, placa: str,
                 numero_chassi: str, motor: Motor, rodas: list[Roda],
                 multimidia: SistemaMultimidia | None = None):
        super().__init__(marca, modelo, ano)
        self.placa = placa

        # Composição
        self.chassi = Chassi(numero_chassi)
        self.motor = motor

        # Agregação
        if len(rodas) != 4:
            raise ValueError("O carro precisa ter exatamente 4 rodas.")
        self.rodas = rodas
        self.multimidia = multimidia

    def acelerar(self, incremento: float) -> str:
        if not self.ligado:
            return "Erro: Ligue o carro antes de acelerar."
        self.velocidade += incremento
        return f"Velocidade atual: {self.velocidade:.1f} km/h."

    def trocar_rodas(self, novas_rodas: list[Roda]) -> str:
        if len(novas_rodas) != 4:
            raise ValueError("São necessárias 4 rodas para a troca.")
        self.rodas = novas_rodas
        return f"Rodas substituídas por jogo de aro {novas_rodas[0].aro}."

    def exibir_ficha(self) -> None:
        midia = (
            f"{self.multimidia.marca_aparelho} ({self.multimidia.tela_polegadas}'')"
            if self.multimidia else "Não instalada"
        )
        print("\n" + "=" * 55)
        print(
            f"VEÍCULO: {self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa}")
        print(
            f"Status:  {'Ligado' if self.ligado else 'Desligado'} | Velocidade: {self.velocidade:.1f} km/h")
        print(
            f"[Composição] Chassi: {self.chassi.numero_serie} ({self.chassi.material})")
        print(f"[Composição] Motor:  {self.motor}")
        print(
            f"[Agregação]  Rodas:  4x Aro {self.rodas[0].aro} ({self.rodas[0].pressao_psi} PSI)")
        print(f"[Agregação]  Mídia:  {midia}")
        print("=" * 55)


class Motorista:
    """Associação: utiliza o Carro sem fazer parte da estrutura dele."""

    def __init__(self, nome: str, cnh: str):
        self.nome = nome
        self.cnh = cnh

    def assumir_direcao(self, carro: Carro) -> str:
        return f"Motorista {self.nome} (CNH: {self.cnh}) assumiu o volante do {carro.marca} {carro.modelo}."


# ==============================================================================
# PROGRAMA PRINCIPAL INTERATIVO
# ==============================================================================

def main():
    print("=== CADASTRO DA ESTRUTURA DO CARRO ===")
    marca = input("Marca do carro: ")
    modelo = input("Modelo do carro: ")
    ano = int(input("Ano: "))
    placa = input("Placa: ")
    chassi = input("Número do Chassi: ")

    tipo_motor = input(
        "Tipo de motor (1 - Combustão | 2 - Elétrico): ").strip()
    potencia = int(input("Potência (cv): "))
    if tipo_motor == "2":
        bateria = float(input("Capacidade da bateria (kWh): "))
        motor = MotorEletrico(potencia, bateria)
    else:
        combustivel = input("Combustível (ex: Flex, Gasolina): ")
        motor = MotorCombustao(potencia, combustivel)

    aro = int(input("Aro das 4 rodas (ex: 16, 17, 18): "))
    rodas = [Roda(aro) for _ in range(4)]

    tem_midia = input("Possui sistema multimídia? (s/n): ").strip().lower()
    multimidia = None
    if tem_midia == "s":
        marca_midia = input("Marca da multimídia: ")
        tela = float(input("Tamanho da tela (polegadas): "))
        multimidia = SistemaMultimidia(marca_midia, tela)

    carro = Carro(marca, modelo, ano, placa, chassi, motor, rodas, multimidia)

    nome_mot = input("\nNome do motorista (Associação): ")
    cnh_mot = input("CNH do motorista: ")
    motorista = Motorista(nome_mot, cnh_mot)

    print("\n" + motorista.assumir_direcao(carro))
    carro.exibir_ficha()

    while True:
        print(
            "\nAções: [1] Ligar  [2] Acelerar  [3] Trocar Rodas  [4] Ficha Completa  [0] Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            print(carro.ligar())
        elif opcao == "2":
            inc = float(input("Incremento de velocidade (km/h): "))
            print(carro.acelerar(inc))
        elif opcao == "3":
            novo_aro = int(input("Novo aro das rodas: "))
            print(carro.trocar_rodas([Roda(novo_aro) for _ in range(4)]))
        elif opcao == "4":
            carro.exibir_ficha()
        elif opcao == "0":
            print(carro.desligar())
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
