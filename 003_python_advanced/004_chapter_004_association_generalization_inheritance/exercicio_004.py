'''

17.4 Implemente uma hierarquia Empregado de qualquer tipo de empresa que seja familiar. A hierarquia deve ter
pelo menos quatro níveis, com herança de membros dado, e métodos. Os métodos devem calcular salários,
demissões, promoção, dar alta, aposentadoria etc. Os métodos devem permitir também calcular aumentos
salariais para Empregados de acordo com sua categoria e produtividade. A hierarquia de herança deve poder
ser utilizada para proporcionar diferentes tipos de acesso a Empregados. Por exemplo, o tipo de acesso
garantido ao público diferirá do tipo de acesso proporcionado a um supervisor de empregado, ao departa-
mento de folha de pagamento, ou ao Ministério da Fazenda. Utilize a herança para distinguir entre pelo
menos quatro tipos diferentes de acesso à informação de Empregado.

'''

from datetime import date


# ==============================================================================
# PARTE 1: HIERARQUIA DE EMPREGADOS (4 NÍVEIS)
# ==============================================================================

class Empregado:
    """Nível 1: Classe base com dados comuns e ciclo de vida do empregado."""

    FATOR_CATEGORIA = 1.0  # Multiplicador base de aumento por categoria

    def __init__(self, matricula: str, nome: str, cpf: str, cargo: str,
                 departamento: str, salario_base: float, anos_servico: int = 0):
        self.matricula = matricula
        self.nome = nome
        self._cpf = cpf                        # Dado sensível (fiscal)
        self.cargo = cargo
        self.departamento = departamento
        self._salario_base = salario_base      # Dado restrito (folha/fazenda)
        self.anos_servico = anos_servico
        self.produtividade = 1.0               # Escala de 0.5 a 1.5
        self.status = "Ativo"                  # Ativo | De Alta | Aposentado | Demitido
        self.historico = [f"{date.today()}: Admitido como {cargo}."]

    def registrar_produtividade(self, indice: float) -> None:
        if not 0.0 <= indice <= 2.0:
            raise ValueError(
                "Índice de produtividade deve estar entre 0.0 e 2.0.")
        self.produtividade = indice

    def calcular_salario_bruto(self) -> float:
        return self._salario_base

    def calcular_imposto_renda(self) -> float:
        bruto = self.calcular_salario_bruto()
        if bruto <= 2500:
            return 0.0
        elif bruto <= 5000:
            return bruto * 0.15
        return bruto * 0.275

    def calcular_salario_liquido(self) -> float:
        return self.calcular_salario_bruto() - self.calcular_imposto_renda()

    def calcular_aumento(self, percentual_base: float) -> float:
        """Calcula o valor do aumento com base na categoria e na produtividade."""
        if self.status != "Ativo":
            return 0.0
        percentual_efetivo = percentual_base * self.FATOR_CATEGORIA * self.produtividade
        return self._salario_base * (percentual_efetivo / 100.0)

    def aplicar_aumento(self, percentual_base: float) -> float:
        aumento = self.calcular_aumento(percentual_base)
        self._salario_base += aumento
        self.historico.append(
            f"{date.today()}: Aumento salarial de R$ {aumento:.2f}.")
        return aumento

    def promover(self, novo_cargo: str, reajuste_percentual: float) -> None:
        if self.status != "Ativo":
            raise RuntimeError(
                "Apenas empregados ativos podem ser promovidos.")
        self.cargo = novo_cargo
        self._salario_base *= (1 + reajuste_percentual / 100.0)
        self.historico.append(f"{date.today()}: Promovido a {novo_cargo}.")

    def dar_alta(self, motivo: str = "Retorno de licença médica") -> None:
        """Registra alta médica/afastamento, reativando o empregado."""
        if self.status in ("Demitido", "Aposentado"):
            raise RuntimeError(
                f"Não é possível dar alta a empregado {self.status}.")
        self.status = "Ativo"
        self.historico.append(f"{date.today()}: Alta concedida ({motivo}).")

    def aposentar(self) -> None:
        if self.anos_servico < 15:
            raise RuntimeError(
                "Tempo mínimo de serviço insuficiente para aposentadoria.")
        self.status = "Aposentado"
        self.historico.append(f"{date.today()}: Aposentadoria concedida.")

    def demitir(self, motivo: str) -> float:
        """Encerra o vínculo e calcula o valor base da rescisão."""
        if self.status == "Demitido":
            raise RuntimeError("Empregado já está demitido.")
        self.status = "Demitido"
        rescisao = self._salario_base * (1 + 0.1 * self.anos_servico)
        self.historico.append(
            f"{date.today()}: Demitido ({motivo}). Rescisão: R$ {rescisao:.2f}.")
        return rescisao


class EmpregadoOperacional(Empregado):
    """Nível 2: Funcionário técnico/operacional com horas extras e adicional de turno."""

    FATOR_CATEGORIA = 1.05

    def __init__(self, matricula: str, nome: str, cpf: str, cargo: str,
                 departamento: str, salario_base: float, anos_servico: int = 0,
                 adicional_turno: float = 0.0):
        super().__init__(matricula, nome, cpf, cargo,
                         departamento, salario_base, anos_servico)
        self.adicional_turno = adicional_turno
        self.horas_extras = 0.0

    def registrar_horas_extras(self, horas: float) -> None:
        self.horas_extras += horas

    def calcular_salario_bruto(self) -> float:
        valor_hora = self._salario_base / 220.0
        pagamento_extras = self.horas_extras * valor_hora * 1.5
        return super().calcular_salario_bruto() + self.adicional_turno + pagamento_extras


class Supervisor(EmpregadoOperacional):
    """Nível 3: Coordena uma equipe e recebe gratificação de liderança."""

    FATOR_CATEGORIA = 1.15

    def __init__(self, matricula: str, nome: str, cpf: str, cargo: str,
                 departamento: str, salario_base: float, anos_servico: int = 0,
                 bonus_lideranca: float = 800.0):
        super().__init__(matricula, nome, cpf, cargo,
                         departamento, salario_base, anos_servico)
        self.bonus_lideranca = bonus_lideranca
        self.equipe: list[Empregado] = []

    def adicionar_subordinado(self, empregado: Empregado) -> None:
        self.equipe.append(empregado)

    def calcular_salario_bruto(self) -> float:
        # Bônus proporcional ao tamanho da equipe ativa
        ativos = sum(1 for e in self.equipe if e.status == "Ativo")
        return super().calcular_salario_bruto() + self.bonus_lideranca + (ativos * 100.0)


class Diretor(Supervisor):
    """Nível 4: Executivo responsável por unidade de negócio, com PLR."""

    FATOR_CATEGORIA = 1.30

    def __init__(self, matricula: str, nome: str, cpf: str, cargo: str,
                 departamento: str, salario_base: float, anos_servico: int = 0,
                 bonus_lideranca: float = 2000.0, percentual_plr: float = 0.15):
        super().__init__(matricula, nome, cpf, cargo, departamento, salario_base,
                         anos_servico, bonus_lideranca)
        self.percentual_plr = percentual_plr

    def calcular_salario_bruto(self) -> float:
        base_supervisor = super().calcular_salario_bruto()
        return base_supervisor + (self._salario_base * self.percentual_plr)


# ==============================================================================
# PARTE 2: HIERARQUIA DE NÍVEIS DE ACESSO (4 NÍVEIS)
# ==============================================================================

class AcessoPublico:
    """Nível 1 de Acesso: Dados institucionais básicos visíveis ao público."""

    nivel_nome = "Público Geral"

    def consultar_dados(self, emp: Empregado) -> dict:
        return {
            "nome": emp.nome,
            "cargo": emp.cargo,
            "departamento": emp.departamento,
            "status": emp.status,
        }


class AcessoSupervisor(AcessoPublico):
    """Nível 2 de Acesso: Herda visão pública + gestão de desempenho e alta."""

    nivel_nome = "Supervisor"

    def consultar_dados(self, emp: Empregado) -> dict:
        dados = super().consultar_dados(emp)
        dados.update({
            "matricula": emp.matricula,
            "anos_servico": emp.anos_servico,
            "produtividade": emp.produtividade,
            "historico_operacional": emp.historico,
        })
        return dados

    def conceder_alta(self, emp: Empregado, motivo: str) -> None:
        emp.dar_alta(motivo)


class AcessoFolhaPagamento(AcessoSupervisor):
    """Nível 3 de Acesso: Herda visão de supervisor + salários, aumentos e rescisões."""

    nivel_nome = "Departamento de Folha de Pagamento"

    def consultar_dados(self, emp: Empregado) -> dict:
        dados = super().consultar_dados(emp)
        dados.update({
            "salario_base": round(emp._salario_base, 2),
            "salario_bruto": round(emp.calcular_salario_bruto(), 2),
            "salario_liquido": round(emp.calcular_salario_liquido(), 2),
        })
        return dados

    def processar_aumento(self, emp: Empregado, percentual_base: float) -> float:
        return emp.aplicar_aumento(percentual_base)

    def processar_promocao(self, emp: Empregado, novo_cargo: str, reajuste: float) -> None:
        emp.promover(novo_cargo, reajuste)

    def processar_demissao(self, emp: Empregado, motivo: str) -> float:
        return emp.demitir(motivo)


class AcessoMinisterioFazenda(AcessoFolhaPagamento):
    """Nível 4 de Acesso: Acesso completo incluindo CPF e retenções tributárias."""

    nivel_nome = "Ministério da Fazenda"

    def consultar_dados(self, emp: Empregado) -> dict:
        dados = super().consultar_dados(emp)
        dados.update({
            "cpf": emp._cpf,
            "irrf_retido": round(emp.calcular_imposto_renda(), 2),
            "categoria_classe": type(emp).__name__,
        })
        return dados


# ==============================================================================
# EXEMPLO DE EXECUÇÃO E DEMONSTRAÇÃO
# ==============================================================================

if __name__ == "__main__":
    # Criando empregados nos 4 níveis da hierarquia
    op = EmpregadoOperacional("M101", "Carlos Silva", "111.222.333-44",
                              "Técnico de Manutenção", "Produção", 3200.0,
                              anos_servico=4, adicional_turno=300.0)
    op.registrar_horas_extras(10)
    op.registrar_produtividade(1.2)

    sup = Supervisor("M202", "Mariana Costa", "222.333.444-55",
                     "Supervisora de Linha", "Produção", 6500.0, anos_servico=8)
    sup.adicionar_subordinado(op)
    sup.registrar_produtividade(1.3)

    diretor = Diretor("M303", "Roberto Almeida", "333.444.555-66",
                      "Diretor Industrial", "Operações", 18000.0, anos_servico=16)
    diretor.adicionar_subordinado(sup)

    # Instanciando os 4 perfis de acesso
    perfis = [
        AcessoPublico(),
        AcessoSupervisor(),
        AcessoFolhaPagamento(),
        AcessoMinisterioFazenda(),
    ]

    print("=== CONSULTA DE DADOS POR NÍVEL DE ACESSO (Empregado: Carlos Silva) ===")
    for perfil in perfis:
        print(f"\n[{perfil.nivel_nome}]")
        for chave, valor in perfil.consultar_dados(op).items():
            print(f"  {chave}: {valor}")

    # Operações administrativas via perfis autorizados
    folha = AcessoFolhaPagamento()
    aumento = folha.processar_aumento(op, percentual_base=5.0)
    print(f"\nAumento aplicado pela Folha a {op.nome}: R$ {aumento:.2f}")
    print(
        f"Novo salário bruto de {op.nome}: R$ {op.calcular_salario_bruto():.2f}")

    # Aposentadoria do Diretor (16 anos de serviço >= 15)
    diretor.aposentar()
    print(f"Status do Diretor {diretor.nome}: {diretor.status}")
