"""
Testes unitários para o Exercício 17.2 (exercicio_002.py).
"""

from datetime import date, timedelta
import unittest

from exercicio_002 import (
    ItemAcervo,
    Periodico,
    Livro,
    LivroLiteratura,
    LivroFiccao,
    LivroPoesia,
    LivroHumanas,
    LivroFilosofia,
    LivroHistoria,
    LivroTecnologia,
    LivroComputacao,
    LivroInteligenciaArtificial,
    Colecao,
    ColecaoLiteratura,
    ColecaoHumanas,
    ColecaoTecnologia,
    Usuario,
    Emprestimo,
    Biblioteca,
    ItemIndisponivelError,
    LimiteEmprestimosExcedidoError,
    ItemIncompativelColecaoError,
)


class TestHierarquiaItensAcervo(unittest.TestCase):
    """Valida as classes da hierarquia de itens do acervo e herança abstrata."""

    def test_item_acervo_classe_abstrata(self):
        # ItemAcervo possui métodos abstratos e não pode ser instanciado diretamente
        with self.assertRaises(TypeError):
            ItemAcervo("COD-01", "Item Genérico", "Autor", 2020, "Estante 1")  # type: ignore[abstract]

    def test_periodico_taxa_atraso(self):
        per = Periodico(
            codigo="PER-01",
            titulo="Nature",
            autor="Springer Nature",
            ano_publicacao=2024,
            localizacao="Estante P1",
            issn="0028-0836",
            edicao=8000,
            periodicidade="Semanal",
        )
        self.assertEqual(per.area_conhecimento, "Periódicos e Publicações Seriadas")
        # Taxa de periódico: R$ 3,50 por dia de atraso
        self.assertEqual(per.calcular_taxa_atraso(4), 14.0)

    def test_livro_base_taxa_atraso(self):
        livro = Livro(
            codigo="LIV-01",
            titulo="Livro Geral",
            autor="Autor A",
            ano_publicacao=2015,
            localizacao="E1",
            isbn="12345",
            editora="Ed A",
            numero_paginas=200,
        )
        # Taxa padrão de livro: R$ 1,50 por dia
        self.assertEqual(livro.calcular_taxa_atraso(10), 15.0)

    def test_livro_tecnologia_taxa_atraso(self):
        tec = LivroTecnologia(
            codigo="TEC-01",
            titulo="Engenharia de Redes",
            autor="Autor B",
            ano_publicacao=2021,
            localizacao="E2",
            isbn="54321",
            editora="Ed B",
            numero_paginas=350,
            subdominio_tecnico="Redes",
        )
        # Taxa de tecnologia: R$ 2,00 por dia
        self.assertEqual(tec.calcular_taxa_atraso(5), 10.0)

    def test_subclasses_literatura(self):
        fic = LivroFiccao(
            codigo="LIT-F1",
            titulo="Duna",
            autor="Frank Herbert",
            ano_publicacao=1965,
            localizacao="E3",
            isbn="111",
            editora="Aleph",
            numero_paginas=680,
            subgenero="Ficção Científica",
            universo_ficcional="Arrakis",
        )
        self.assertIn("Ficção Científica", fic.obter_ficha_catalografica())
        self.assertEqual(fic.area_conhecimento, "Literatura, Letras e Artes")

        poe = LivroPoesia(
            codigo="LIT-P1",
            titulo="Sonetos",
            autor="Camões",
            ano_publicacao=1595,
            localizacao="E4",
            isbn="222",
            editora="Porto",
            numero_paginas=120,
            forma_metrica="Decassílabos",
            antologia=False,
            total_poemas=80,
        )
        self.assertEqual(poe.total_poemas, 80)
        self.assertIn("Decassílabos", poe.obter_ficha_catalografica())

    def test_subclasses_humanas(self):
        fil = LivroFilosofia(
            codigo="HUM-F1",
            titulo="Meditações Metafísicas",
            autor="René Descartes",
            ano_publicacao=1641,
            localizacao="E5",
            isbn="333",
            editora="Martins Fontes",
            numero_paginas=180,
            corrente_filosofica="Racionalismo",
            periodo_historico="Moderno",
        )
        self.assertEqual(fil.disciplina, "Filosofia")
        self.assertEqual(fil.corrente_filosofica, "Racionalismo")

        hist = LivroHistoria(
            codigo="HUM-H1",
            titulo="A Era das Revoluções",
            autor="Eric Hobsbawm",
            ano_publicacao=1962,
            localizacao="E6",
            isbn="444",
            editora="Paz e Terra",
            numero_paginas=400,
            epoca_abordada="1789-1848",
            regiao_geografica="Europa",
        )
        self.assertTrue(hist.fontes_primarias)

    def test_subclasses_tecnologia(self):
        comp = LivroComputacao(
            codigo="TEC-C1",
            titulo="Estruturas de Dados em C",
            autor="Tenenbaum",
            ano_publicacao=1995,
            localizacao="E7",
            isbn="555",
            editora="Pearson",
            numero_paginas=500,
            linguagem_programacao="C",
        )
        self.assertEqual(comp.linguagem_programacao, "C")

        ia = LivroInteligenciaArtificial(
            codigo="TEC-I1",
            titulo="Machine Learning com Scikit-Learn",
            autor="Aurélien Géron",
            ano_publicacao=2019,
            localizacao="E8",
            isbn="666",
            editora="O'Reilly",
            numero_paginas=800,
            ramo_ia="Machine Learning Prático",
            frameworks=["Scikit-Learn", "TensorFlow"],
        )
        self.assertIn("TensorFlow", ia.frameworks)


class TestHierarquiaColecoes(unittest.TestCase):
    """Testa as classes de coleções, agregação e validação de compatibilidade."""

    def test_colecao_literatura_bloqueia_item_incompativel(self):
        col_lit = ColecaoLiteratura("LIT", "Literatura", "Obras Literárias")
        livro_tec = LivroTecnologia("TEC", "C++ Moderno", "Bjarne", 2013, "E1", "1", "Ed", 400, "Computação")

        with self.assertRaises(ItemIncompativelColecaoError):
            col_lit.adicionar_item(livro_tec)

    def test_colecao_humanas_bloqueia_item_incompativel(self):
        col_hum = ColecaoHumanas("HUM", "Humanas", "Ciências Humanas")
        livro_lit = LivroLiteratura("LIT", "Iracema", "José de Alencar", 1865, "E1", "2", "Ed", 150, "Romance")

        with self.assertRaises(ItemIncompativelColecaoError):
            col_hum.adicionar_item(livro_lit)

    def test_colecao_tecnologia_bloqueia_item_incompativel(self):
        col_tec = ColecaoTecnologia("TEC", "Tecnologia", "TI")
        livro_fil = LivroFilosofia("FIL", "Ética", "Spinoza", 1677, "E1", "3", "Ed", 300, "Racionalismo", "Moderno")

        with self.assertRaises(ItemIncompativelColecaoError):
            col_tec.adicionar_item(livro_fil)

    def test_adicao_e_busca_na_colecao(self):
        col_tec = ColecaoTecnologia("TEC", "Tecnologia", "TI")
        livro = LivroComputacao("TEC-PY", "Python Fluente", "Ramalho", 2022, "E1", "4", "O'Reilly", 1000, "Python")
        col_tec.adicionar_item(livro)

        self.assertEqual(len(col_tec), 1)
        self.assertIn("TEC-PY", col_tec)
        self.assertEqual(len(col_tec.buscar_por_titulo("python")), 1)
        self.assertEqual(len(col_tec.filtrar_por_linguagem("python")), 1)


class TestGestaoEmprestimosEBiblioteca(unittest.TestCase):
    """Testa o fluxo integrado de empréstimos, cotas, devoluções e multas."""

    def setUp(self):
        self.biblio = Biblioteca("Biblioteca Universitária", "Campus Central")
        self.col_lit = ColecaoLiteratura("COL-LIT", "Literatura", "Livros Literários")
        self.col_tec = ColecaoTecnologia("COL-TEC", "Tecnologia", "Livros Técnicos")

        self.biblio.registrar_colecao(self.col_lit)
        self.biblio.registrar_colecao(self.col_tec)

        self.livro_lit = LivroLiteratura(
            "LIT-01", "Grande Sertão: Veredas", "Guimarães Rosa", 1956, "E1", "ISBN-1", "Nova Fronteira", 600, "Romance"
        )
        self.livro_tec = LivroComputacao(
            "TEC-01", "Clean Code", "Robert Martin", 2008, "E2", "ISBN-2", "Prentice", 450, "Java"
        )

        self.biblio.adicionar_item("COL-LIT", self.livro_lit)
        self.biblio.adicionar_item("COL-TEC", self.livro_tec)

        self.usuario = Usuario("U01", "Lucas Mendes", "lucas@email.com", limite_emprestimos=1)
        self.biblio.cadastrar_usuario(self.usuario)

    def test_emprestimo_e_devolucao_com_sucesso(self):
        data_ini = date(2026, 11, 1)
        emp = self.biblio.realizar_emprestimo("U01", "TEC-01", data_atual=data_ini, dias_prazo=10)

        # Item deve estar indisponível e associado ao usuário
        self.assertFalse(self.livro_tec.disponivel)
        self.assertEqual(len(self.usuario.emprestimos_ativos), 1)

        # Devolução sem atraso (5 dias após retirada)
        multa = self.biblio.registrar_devolucao(emp.id_emprestimo, data_ini + timedelta(days=5))
        self.assertEqual(multa, 0.0)
        self.assertTrue(self.livro_tec.disponivel)
        self.assertEqual(len(self.usuario.emprestimos_ativos), 0)

    def test_tentativa_emprestimo_item_ja_emprestado(self):
        data_ini = date(2026, 11, 1)
        self.biblio.realizar_emprestimo("U01", "LIT-01", data_atual=data_ini)

        # Criar outro usuário
        outro_user = Usuario("U02", "Ana Paula", "ana@email.com", limite_emprestimos=2)
        self.biblio.cadastrar_usuario(outro_user)

        with self.assertRaises(ItemIndisponivelError):
            self.biblio.realizar_emprestimo("U02", "LIT-01", data_atual=data_ini)

    def test_limite_emprestimos_excedido(self):
        data_ini = date(2026, 11, 1)
        # Limite do usuário U01 é 1
        self.biblio.realizar_emprestimo("U01", "LIT-01", data_atual=data_ini)

        with self.assertRaises(LimiteEmprestimosExcedidoError):
            self.biblio.realizar_emprestimo("U01", "TEC-01", data_atual=data_ini)

    def test_calculo_multa_atraso(self):
        data_ini = date(2026, 11, 1)
        emp = self.biblio.realizar_emprestimo("U01", "TEC-01", data_atual=data_ini, dias_prazo=10)

        # Devolução com 15 dias (5 dias de atraso). LivroTecnologia cobra R$ 2,00/dia = R$ 10,00
        multa = self.biblio.registrar_devolucao(emp.id_emprestimo, data_ini + timedelta(days=15))
        self.assertEqual(multa, 10.0)

    def test_pesquisa_global_acervo(self):
        res = self.biblio.pesquisar_acervo("Sertão")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0][1].codigo, "LIT-01")


if __name__ == "__main__":
    unittest.main()
