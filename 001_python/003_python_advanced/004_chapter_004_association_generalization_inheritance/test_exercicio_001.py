"""
Testes unitários para o Exercício 17.1 (exercicio_001.py).
"""

import unittest
from pathlib import Path
import tempfile

from exercicio_001 import (
    Pessoa,
    Estudante,
    Empregado,
    EstudanteEmpregado,
    instanciar_pessoa_de_registro,
    ler_arquivo_pessoas,
    separar_listas,
    ordenar_por_primeiro_sobrenome,
)


class TestHierarquiaPessoa(unittest.TestCase):
    """Testa a modelagem da hierarquia de classes e herança múltipla."""

    def test_instanciacao_pessoa(self):
        p = Pessoa("Maria Silva Santos", "Rua A, 10", "15/05/1990", "F")
        self.assertEqual(p.nome, "Maria Silva Santos")
        self.assertEqual(p.endereco, "Rua A, 10")
        self.assertEqual(p.data_nascimento, "15/05/1990")
        self.assertEqual(p.sexo, "F")
        self.assertEqual(p.primeiro_sobrenome, "Silva")

    def test_instanciacao_estudante(self):
        e = Estudante("Lucas Pereira Lima", "Av B, 20", "20/08/2002", "M", "MAT101", "Engenharia")
        self.assertTrue(isinstance(e, Pessoa))
        self.assertTrue(isinstance(e, Estudante))
        self.assertFalse(isinstance(e, Empregado))
        self.assertEqual(e.matricula, "MAT101")
        self.assertEqual(e.curso, "Engenharia")
        self.assertEqual(e.primeiro_sobrenome, "Pereira")

    def test_instanciacao_empregado(self):
        emp = Empregado("Ana Souza Costa", "Rua C, 30", "10/02/1985", "F", 5500.0, "Analista")
        self.assertTrue(isinstance(emp, Pessoa))
        self.assertTrue(isinstance(emp, Empregado))
        self.assertFalse(isinstance(emp, Estudante))
        self.assertEqual(emp.salario, 5500.0)
        self.assertEqual(emp.cargo, "Analista")
        self.assertEqual(emp.primeiro_sobrenome, "Souza")

    def test_heranca_multipla_estudante_empregado(self):
        ee = EstudanteEmpregado(
            nome="Rafael Gomes Barbosa",
            endereco="Travessa D, 40",
            data_nascimento="05/01/2000",
            sexo="M",
            matricula="MAT202",
            curso="Ciência da Computação",
            salario=3500.0,
            cargo="Desenvolvedor Jr",
        )
        # Verifica relações 'é-um' (polimorfismo)
        self.assertTrue(isinstance(ee, Pessoa))
        self.assertTrue(isinstance(ee, Estudante))
        self.assertTrue(isinstance(ee, Empregado))
        self.assertTrue(isinstance(ee, EstudanteEmpregado))

        # Verifica integridade dos atributos combinados
        self.assertEqual(ee.nome, "Rafael Gomes Barbosa")
        self.assertEqual(ee.matricula, "MAT202")
        self.assertEqual(ee.curso, "Ciência da Computação")
        self.assertEqual(ee.salario, 3500.0)
        self.assertEqual(ee.cargo, "Desenvolvedor Jr")
        self.assertEqual(ee.primeiro_sobrenome, "Gomes")


class TestExtracaoSobrenomeEOrdenacao(unittest.TestCase):
    """Testa a extração do primeiro sobrenome e ordenação alfabética."""

    def test_extracao_primeiro_sobrenome_simples(self):
        p1 = Pessoa("Ana Silva", "End", "01/01/2000", "F")
        self.assertEqual(p1.primeiro_sobrenome, "Silva")

    def test_extracao_com_multiplos_sobrenomes(self):
        p2 = Pessoa("Carlos Pereira Rocha Santos", "End", "01/01/2000", "M")
        self.assertEqual(p2.primeiro_sobrenome, "Pereira")

    def test_extracao_com_preposicao(self):
        p3 = Pessoa("João da Silva Barbosa", "End", "01/01/2000", "M")
        self.assertEqual(p3.primeiro_sobrenome, "Silva")

        p4 = Pessoa("Maria de Oliveira", "End", "01/01/2000", "F")
        self.assertEqual(p4.primeiro_sobrenome, "Oliveira")

    def test_extracao_mononimo(self):
        p5 = Pessoa("Sócrates", "End", "01/01/2000", "M")
        self.assertEqual(p5.primeiro_sobrenome, "Sócrates")

    def test_ordenacao_alfabetica_primeiro_sobrenome(self):
        p_souza = Pessoa("Beatriz Souza Santos", "", "", "")
        p_batista = Pessoa("Bruno Batista Toledo", "", "", "")
        p_alvares = Pessoa("Camila Álvares Costa", "", "", "")
        p_castro = Pessoa("Alice Castro Oliveira", "", "", "")

        lista = [p_souza, p_batista, p_alvares, p_castro]
        ordenada = ordenar_por_primeiro_sobrenome(lista)

        sobrenomes_ordenados = [p.primeiro_sobrenome for p in ordenada]
        self.assertEqual(sobrenomes_ordenados, ["Álvares", "Batista", "Castro", "Souza"])

        # Testa operador < nativo
        self.assertTrue(p_batista < p_souza)
        self.assertTrue(p_alvares < p_batista)


class TestProcessamentoArquivoEListas(unittest.TestCase):
    """Testa a leitura de arquivo e a separação em 4 listas."""

    def test_separacao_em_quatro_listas(self):
        p = Pessoa("Pessoa Genérica", "", "", "")
        e = Estudante("Aluno 1", "", "", "", "M1", "C1")
        emp = Empregado("Func 1", "", "", "", 3000, "Cargo 1")
        ee = EstudanteEmpregado("Aluno Func", "", "", "", "M2", "C2", 4000, "Cargo 2")

        todos = [p, e, emp, ee]
        listas = separar_listas(todos)

        # a) Geral: todos os 4
        self.assertEqual(len(listas["geral"]), 4)

        # b) Estudantes: Aluno 1 e Aluno Func
        self.assertEqual(len(listas["estudantes"]), 2)
        self.assertIn(e, listas["estudantes"])
        self.assertIn(ee, listas["estudantes"])

        # c) Empregados: Func 1 e Aluno Func
        self.assertEqual(len(listas["empregados"]), 2)
        self.assertIn(emp, listas["empregados"])
        self.assertIn(ee, listas["empregados"])

        # d) Estudantes Empregados: Aluno Func
        self.assertEqual(len(listas["estudantes_empregados"]), 1)
        self.assertIn(ee, listas["estudantes_empregados"])

    def test_leitura_arquivo_temporario(self):
        conteudo = (
            "tipo;nome;endereco;data_nascimento;sexo;matricula;curso;salario;cargo\n"
            "pessoa;Mariana Silva;Rua 1;01/01/1990;F;;;;\n"
            "estudante;Carlos Rocha;Rua 2;02/02/1995;M;E10;Física;;\n"
            "empregado;Beatriz Santos;Rua 3;03/03/1985;F;;;5000.0;Dev\n"
            "estudante_empregado;Rafael Gomes;Rua 4;04/04/2000;M;E20;Química;2500.0;Estagiário\n"
        )
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".csv", delete=False) as tmp:
            tmp.write(conteudo)
            tmp_path = Path(tmp.name)

        try:
            pessoas = ler_arquivo_pessoas(tmp_path)
            self.assertEqual(len(pessoas), 4)
            self.assertEqual(type(pessoas[0]), Pessoa)
            self.assertEqual(type(pessoas[1]), Estudante)
            self.assertEqual(type(pessoas[2]), Empregado)
            self.assertEqual(type(pessoas[3]), EstudanteEmpregado)
        finally:
            tmp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
