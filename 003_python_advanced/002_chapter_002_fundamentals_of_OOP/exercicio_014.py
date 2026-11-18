'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 5.14

Enunciado:
Construir uma definição de classe que possa ser utilizada para representar um
empregado de uma companhia. Cada empregado é definido por um número inteiro ID,
um salário e o número máximo de horas de trabalho por semana. Os serviços que
devem proporcionar a classe, pelo menos devem permitir introduzir dados de um novo
empregado, visualizar os dados existentes de um novo empregado e capacidade para
processar as operações necessárias para a inserção e o cancelamento na seguridade
social e nos seguros que a companhia tenha contratado.
'''

from dataclasses import dataclass, field


class Empregado:
    """
    Representa um empregado de uma companhia corporativa.

    Atributos:
    - id_empregado (int): Identificador único do funcionário.
    - nome (str): Nome do empregado.
    - salario (float): Remuneração mensal.
    - max_horas_semanais (int): Carga horária máxima semanal contratada.
    - inscrito_seguridade_social (bool): Status de regularidade previdenciária (INSS/Seguridade).
    - numero_seguridade_social (str): Número de inscrição previdenciária.
    - seguros_contratados (set[str]): Seguros corporativos ativos (saúde, vida, dental, etc.).

    Serviços disponibilizados:
    - Introdução e atualização de dados;
    - Visualização completa da ficha cadastral;
    - Inserção e cancelamento na seguridade social;
    - Inclusão e cancelamento de seguros corporativos.
    """

    def __init__(
        self,
        id_empregado: int,
        nome: str,
        salario: float,
        max_horas_semanais: int = 40
    ) -> None:
        """
        Serviço 1: Introduzir dados de um novo empregado.
        Valida e inicializa os atributos cadastrais obrigatórios.
        """
        self.definir_dados_iniciais(
            id_empregado, nome, salario, max_horas_semanais)

        # Gestão de Seguridade Social
        self.inscrito_seguridade_social: bool = False
        self.numero_seguridade_social: str = "Não cadastrado"

        # Gestão de Seguros da Companhia
        self.seguros_contratados: set[str] = set()

    # --------------------------------------------------------------------------
    # 1. Introdução e Atualização de Dados
    # --------------------------------------------------------------------------
    def definir_dados_iniciais(
        self,
        id_empregado: int,
        nome: str,
        salario: float,
        max_horas_semanais: int
    ) -> None:
        """Valida e aplica os dados de identificação e contrato de trabalho."""
        if id_empregado <= 0:
            raise ValueError(
                "O ID do empregado deve ser um número inteiro positivo.")
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        if not (1 <= max_horas_semanais <= 60):
            raise ValueError(
                "A jornada máxima de trabalho semanal deve estar entre 1 e 60 horas.")

        self._id_empregado = int(id_empregado)
        self.nome = nome.strip()
        self._salario = float(salario)
        self._max_horas_semanais = int(max_horas_semanais)

    @property
    def id_empregado(self) -> int:
        return self._id_empregado

    @property
    def salario(self) -> float:
        return self._salario

    @property
    def max_horas_semanais(self) -> int:
        return self._max_horas_semanais

    def reajustar_salario(self, percentual: float) -> None:
        """Reajusta o salário por percentual positivo."""
        if percentual <= 0:
            raise ValueError("O percentual de aumento deve ser positivo.")
        self._salario *= (1 + percentual / 100)
        print(
            f"[{self.nome}] Salário reajustado em {percentual:.1f}%. Novo valor: R$ {self._salario:.2f}")

    def ajustar_carga_horaria(self, novas_horas: int) -> None:
        """Altera a jornada máxima de trabalho semanal."""
        if not (1 <= novas_horas <= 60):
            raise ValueError("Carga horária inválida.")
        self._max_horas_semanais = novas_horas
        print(
            f"[{self.nome}] Jornada semanal alterada para {self._max_horas_semanais}h.")

    # --------------------------------------------------------------------------
    # 2. Operações de Seguridade Social
    # --------------------------------------------------------------------------
    def inscrever_seguridade_social(self, numero_registro: str) -> None:
        """Registra e ativa o empregado na Seguridade Social do Estado."""
        if not numero_registro.strip():
            raise ValueError(
                "O número de registro da seguridade social é obrigatório.")
        self.inscrito_seguridade_social = True
        self.numero_seguridade_social = numero_registro.strip()
        print(
            f"[Seguridade Social] Empregado '{self.nome}' (ID: {self._id_empregado}) INSCRITO com registro: {self.numero_seguridade_social}.")

    def cancelar_seguridade_social(self, motivo: str = "Desligamento") -> None:
        """Cancela a inscrição ativa do empregado na Seguridade Social."""
        if not self.inscrito_seguridade_social:
            print(
                f"[Seguridade Social] Empregado '{self.nome}' já não possui inscrição ativa.")
            return
        self.inscrito_seguridade_social = False
        registro_anterior = self.numero_seguridade_social
        self.numero_seguridade_social = "Cancelado"
        print(
            f"[Seguridade Social] Inscrição {registro_anterior} de '{self.nome}' CANCELADA. Motivo: {motivo}.")

    # --------------------------------------------------------------------------
    # 3. Operações nos Seguros da Companhia
    # --------------------------------------------------------------------------
    def aderir_seguro(self, nome_seguro: str) -> None:
        """Insere o empregado em uma apólice de seguro contratada pela companhia."""
        nome_seguro = nome_seguro.strip().title()
        if nome_seguro in self.seguros_contratados:
            print(
                f"[Seguros] '{self.nome}' já possui o seguro '{nome_seguro}' ativo.")
            return
        self.seguros_contratados.add(nome_seguro)
        print(
            f"[Seguros] Empregado '{self.nome}' INSERIDO no seguro corporativo: '{nome_seguro}'.")

    def cancelar_seguro(self, nome_seguro: str) -> None:
        """Cancela um seguro corporativo específico do empregado."""
        nome_seguro = nome_seguro.strip().title()
        if nome_seguro not in self.seguros_contratados:
            print(
                f"[Seguros] Seguro '{nome_seguro}' não encontrado para o empregado '{self.nome}'.")
            return
        self.seguros_contratados.remove(nome_seguro)
        print(
            f"[Seguros] Seguro '{nome_seguro}' CANCELADO para '{self.nome}'.")

    def cancelar_todos_seguros(self) -> None:
        """Revoga todas as coberturas de seguro ativas (ex.: rescisão contratual)."""
        total = len(self.seguros_contratados)
        self.seguros_contratados.clear()
        print(
            f"[Seguros] Todos os {total} seguros contratados de '{self.nome}' foram cancelados.")

    # --------------------------------------------------------------------------
    # 4. Visualização dos Dados Existentes
    # --------------------------------------------------------------------------
    def visualizar_dados(self) -> None:
        """Serviço 2: Exibe detalhadamente a ficha funcional do empregado."""
        status_ss = f"Ativa (Registro: {self.numero_seguridade_social})" if self.inscrito_seguridade_social else "Inativa / Não inscrito"
        lista_seguros = ", ".join(sorted(
            self.seguros_contratados)) if self.seguros_contratados else "Nenhum seguro contratado"

        print("\n" + "=" * 60)
        print(
            f"FICHA FUNCIONAL: {self.nome.upper()} (ID: {self._id_empregado:04d})")
        print("=" * 60)
        print(f"Salário Mensal:           R$ {self._salario:10.2f}")
        print(f"Jornada Máxima Semanal:   {self._max_horas_semanais} horas")
        print(f"Seguridade Social:        {status_ss}")
        print(f"Seguros Corporativos:     {lista_seguros}")
        print("=" * 60)

    def __str__(self) -> str:
        return f"Empregado(ID={self._id_empregado}, Nome='{self.nome}', Salario=R${self._salario:.2f})"


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    print("=== 1. Introduzindo dados de um novo empregado ===")
    emp1 = Empregado(
        id_empregado=101,
        nome="Roberto Albuquerque",
        salario=5800.00,
        max_horas_semanais=40
    )
    emp1.visualizar_dados()

    print("\n=== 2. Processando inserção na Seguridade Social ===")
    emp1.inscrever_seguridade_social("SS-887766-BR")

    print("\n=== 3. Inserindo nos seguros corporativos contratados ===")
    emp1.aderir_seguro("Plano de Saúde Premium")
    emp1.aderir_seguro("Seguro de Vida em Grupo")
    emp1.aderir_seguro("Plano Odontológico")

    # Visualização com os dados atualizados
    emp1.visualizar_dados()

    print("\n=== 4. Processando cancelamento de seguro individual ===")
    emp1.cancelar_seguro("Plano Odontológico")

    print("\n=== 5. Processando rescisão / cancelamento de seguridade e seguros ===")
    emp1.cancelar_seguridade_social(motivo="Demissão a pedido")
    emp1.cancelar_todos_seguros()

    # Visualização final após cancelamentos
    emp1.visualizar_dados()
