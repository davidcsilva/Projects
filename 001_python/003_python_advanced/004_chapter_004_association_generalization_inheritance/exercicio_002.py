"""
Capítulo 04 - Associação, Generalização e Herança
Exercício 17.2

Enunciado:
17.2 Implemente uma hierarquia Biblioteca que tenha pelo menos uma dezena de classes.
Consideramos uma biblioteca que tenha coleções de livros na área de literatura, humanas, tecnologia etc.

Visão Geral da Arquitetura:
- 19 classes modeladas com herança, polimorfismo, abstração, associação e agregação.
- Hierarquia de Itens do Acervo:
    1. ItemAcervo (ABC)
    2. Periodico
    3. Livro
    4. LivroLiteratura
    5. LivroFiccao
    6. LivroPoesia
    7. LivroHumanas
    8. LivroFilosofia
    9. LivroHistoria
    10. LivroTecnologia
    11. LivroComputacao
    12. LivroInteligenciaArtificial
- Hierarquia de Coleções:
    13. Colecao (Base)
    14. ColecaoLiteratura
    15. ColecaoHumanas
    16. ColecaoTecnologia
- Núcleo de Gestão e Associação:
    17. Usuario
    18. Emprestimo
    19. Biblioteca
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date, timedelta
from typing import Any, Iterator


# ==============================================================================
# EXCEÇÕES CUSTOMIZADAS DO DOMÍNIO
# ==============================================================================

class BibliotecaError(Exception):
    """Exceção base para regras de negócio da biblioteca."""


class ItemIndisponivelError(BibliotecaError):
    """Lançada quando se tenta emprestar um item que já está emprestado."""


class LimiteEmprestimosExcedidoError(BibliotecaError):
    """Lançada quando um usuário atinge sua cota máxima de empréstimos."""


class ItemIncompativelColecaoError(BibliotecaError):
    """Lançada quando um item não corresponde à área temática da coleção."""


# ==============================================================================
# HIERARQUIA 1: ITENS DO ACERVO (GENERALIZAÇÃO / ESPECIALIZAÇÃO)
# ==============================================================================

class ItemAcervo(ABC):
    """
    Classe base abstrata para todos os itens gerenciáveis no acervo da biblioteca.
    Define a interface e os comportamentos essenciais de empréstimo e taxação.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
    ) -> None:
        self.codigo = codigo.strip().upper()
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.ano_publicacao = int(ano_publicacao)
        self.localizacao = localizacao.strip()
        self.disponivel: bool = True

    def emprestar(self) -> None:
        """Marca o item como emprestado se estiver disponível."""
        if not self.disponivel:
            raise ItemIndisponivelError(
                f"O item '{self.titulo}' (Código: {self.codigo}) não está disponível para empréstimo."
            )
        self.disponivel = False

    def devolver(self) -> None:
        """Registra a devolução do item ao acervo."""
        self.disponivel = True

    @property
    @abstractmethod
    def area_conhecimento(self) -> str:
        """Retorna o nome da grande área do conhecimento do item."""

    @abstractmethod
    def calcular_taxa_atraso(self, dias_atraso: int) -> float:
        """
        Calcula o valor da multa por dias de atraso na devolução.
        O valor da taxa varia polimorficamente dependendo da categoria do item.
        """

    @abstractmethod
    def obter_ficha_catalografica(self) -> str:
        """Gera a ficha catalográfica com os detalhes do item."""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(codigo={self.codigo!r}, titulo={self.titulo!r})"

    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.codigo}] {self.titulo} - {self.autor} ({self.ano_publicacao}) [{status}]"


class Periodico(ItemAcervo):
    """
    Representa periódicos, revistas científicas, anais e boletins.
    Possui taxa de atraso diferenciada devido à sua rápida rotatividade.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        issn: str,
        edicao: int,
        periodicidade: str,
    ) -> None:
        super().__init__(codigo, titulo, autor, ano_publicacao, localizacao)
        self.issn = issn.strip()
        self.edicao = int(edicao)
        self.periodicidade = periodicidade.strip()

    @property
    def area_conhecimento(self) -> str:
        return "Periódicos e Publicações Seriadas"

    def calcular_taxa_atraso(self, dias_atraso: int) -> float:
        # Periódicos têm taxa mais severa (R$ 3,50 por dia)
        return max(0.0, dias_atraso * 3.50)

    def obter_ficha_catalografica(self) -> str:
        return (
            f"PERIÓDICO: {self.titulo}\n"
            f"Editor/Organizador: {self.autor} | ISSN: {self.issn} | Edição: nº {self.edicao}\n"
            f"Periodicidade: {self.periodicidade} | Ano: {self.ano_publicacao} | Localização: {self.localizacao}"
        )


class Livro(ItemAcervo):
    """
    Classe intermediária que generaliza livros tradicionais com ISBN,
    editora e número de páginas.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        edicao: int = 1,
    ) -> None:
        super().__init__(codigo, titulo, autor, ano_publicacao, localizacao)
        self.isbn = isbn.strip()
        self.editora = editora.strip()
        self.numero_paginas = int(numero_paginas)
        self.edicao = int(edicao)

    @property
    def area_conhecimento(self) -> str:
        return "Geral / Multidisciplinar"

    def calcular_taxa_atraso(self, dias_atraso: int) -> float:
        # Taxa base padrão para livros (R$ 1,50 por dia)
        return max(0.0, dias_atraso * 1.50)

    def obter_ficha_catalografica(self) -> str:
        return (
            f"LIVRO: {self.titulo}\n"
            f"Autor(es): {self.autor}\n"
            f"Editora: {self.editora}, {self.edicao}ª ed., {self.ano_publicacao} | {self.numero_paginas} p.\n"
            f"ISBN: {self.isbn} | Área: {self.area_conhecimento} | Estante: {self.localizacao}"
        )


# ------------------------------------------------------------------------------
# SUBCATEGORIA: LITERATURA
# ------------------------------------------------------------------------------

class LivroLiteratura(Livro):
    """
    Especialização para obras literárias (poesia, prosa, teatro, romance).
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        estilo_literario: str,
        idioma_original: str = "Português",
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas, edicao
        )
        self.estilo_literario = estilo_literario.strip()
        self.idioma_original = idioma_original.strip()

    @property
    def area_conhecimento(self) -> str:
        return "Literatura, Letras e Artes"

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        return (
            f"{base}\n"
            f"Gênero Literário: {self.estilo_literario} | Idioma Original: {self.idioma_original}"
        )


class LivroFiccao(LivroLiteratura):
    """
    Especialização de literatura para ficção (científica, fantástica, distopias).
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        subgenero: str,
        universo_ficcional: str = "Realista",
        faixa_etaria_recomendada: int = 14,
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas,
            estilo_literario="Ficção", idioma_original="Português", edicao=edicao
        )
        self.subgenero = subgenero.strip()
        self.universo_ficcional = universo_ficcional.strip()
        self.faixa_etaria_recomendada = faixa_etaria_recomendada

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        return (
            f"{base}\n"
            f"Subgênero de Ficção: {self.subgenero} | Universo: {self.universo_ficcional} | "
            f"Classificação Indicativa: +{self.faixa_etaria_recomendada} anos"
        )


class LivroPoesia(LivroLiteratura):
    """
    Especialização de literatura para obras poéticas e líricas.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        forma_metrica: str,
        antologia: bool = False,
        total_poemas: int = 0,
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas,
            estilo_literario="Poesia", idioma_original="Português", edicao=edicao
        )
        self.forma_metrica = forma_metrica.strip()
        self.antologia = antologia
        self.total_poemas = total_poemas

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        tipo_obra = "Antologia Poética" if self.antologia else "Obra Autoral"
        return (
            f"{base}\n"
            f"Métrica: {self.forma_metrica} | Formato: {tipo_obra} | Total de Poemas: {self.total_poemas}"
        )


# ------------------------------------------------------------------------------
# SUBCATEGORIA: CIÊNCIAS HUMANAS
# ------------------------------------------------------------------------------

class LivroHumanas(Livro):
    """
    Especialização para ciências humanas, sociais aplicadas e filosofia.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        disciplina: str,
        metodologia: str = "Teórica",
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas, edicao
        )
        self.disciplina = disciplina.strip()
        self.metodologia = metodologia.strip()

    @property
    def area_conhecimento(self) -> str:
        return "Ciências Humanas e Sociais"

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        return (
            f"{base}\n"
            f"Disciplina: {self.disciplina} | Metodologia: {self.metodologia}"
        )


class LivroFilosofia(LivroHumanas):
    """
    Especialização para livros e tratados filosóficos.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        corrente_filosofica: str,
        periodo_historico: str,
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas,
            disciplina="Filosofia", metodologia="Analítico-Conceitual", edicao=edicao
        )
        self.corrente_filosofica = corrente_filosofica.strip()
        self.periodo_historico = periodo_historico.strip()

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        return (
            f"{base}\n"
            f"Corrente Filosófica: {self.corrente_filosofica} | Período: {self.periodo_historico}"
        )


class LivroHistoria(LivroHumanas):
    """
    Especialização para livros de historiografia, história geral e regional.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        epoca_abordada: str,
        regiao_geografica: str,
        fontes_primarias: bool = True,
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas,
            disciplina="História", metodologia="Historiográfica/Documental", edicao=edicao
        )
        self.epoca_abordada = epoca_abordada.strip()
        self.regiao_geografica = regiao_geografica.strip()
        self.fontes_primarias = fontes_primarias

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        fontes = "Sim (Documentos históricos anexos)" if self.fontes_primarias else "Apenas secundárias"
        return (
            f"{base}\n"
            f"Época Abordada: {self.epoca_abordada} | Região: {self.regiao_geografica} | "
            f"Fontes Primárias: {fontes}"
        )


# ------------------------------------------------------------------------------
# SUBCATEGORIA: CIÊNCIAS EXATAS E TECNOLOGIA
# ------------------------------------------------------------------------------

class LivroTecnologia(Livro):
    """
    Especialização para ciências exatas, tecnologia da informação e engenharias.
    Possui taxa de atraso moderadamente superior (R$ 2,00) devido ao alto valor
    do material técnico.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        subdominio_tecnico: str,
        versao_tecnologia: str = "Agnóstica",
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas, edicao
        )
        self.subdominio_tecnico = subdominio_tecnico.strip()
        self.versao_tecnologia = versao_tecnologia.strip()

    @property
    def area_conhecimento(self) -> str:
        return "Ciências Exatas e Tecnologia"

    def calcular_taxa_atraso(self, dias_atraso: int) -> float:
        # Livros de tecnologia possuem taxa de R$ 2,00/dia
        return max(0.0, dias_atraso * 2.00)

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        return (
            f"{base}\n"
            f"Subdomínio Técnico: {self.subdominio_tecnico} | Versão/Padrão: {self.versao_tecnologia}"
        )


class LivroComputacao(LivroTecnologia):
    """
    Especialização para programação, engenharia de software e arquitetura.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        linguagem_programacao: str,
        paradigma: str = "Multiparadigma",
        inclui_codigo_fonte: bool = True,
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas,
            subdominio_tecnico="Ciência da Computação & Engenharia de Software",
            versao_tecnologia=linguagem_programacao, edicao=edicao
        )
        self.linguagem_programacao = linguagem_programacao.strip()
        self.paradigma = paradigma.strip()
        self.inclui_codigo_fonte = inclui_codigo_fonte

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        codigo = "Repositório Git / Código incluso" if self.inclui_codigo_fonte else "Não inclui código"
        return (
            f"{base}\n"
            f"Linguagem Principal: {self.linguagem_programacao} | Paradigma: {self.paradigma} | {codigo}"
        )


class LivroInteligenciaArtificial(LivroTecnologia):
    """
    Especialização para inteligência artificial, aprendizado de máquina e redes neurais.
    """

    def __init__(
        self,
        codigo: str,
        titulo: str,
        autor: str,
        ano_publicacao: int,
        localizacao: str,
        isbn: str,
        editora: str,
        numero_paginas: int,
        ramo_ia: str,
        frameworks: list[str] | None = None,
        foco_matematico: str = "Teórico e Aplicado",
        edicao: int = 1,
    ) -> None:
        super().__init__(
            codigo, titulo, autor, ano_publicacao, localizacao, isbn, editora, numero_paginas,
            subdominio_tecnico="Inteligência Artificial & Ciência de Dados",
            versao_tecnologia=ramo_ia, edicao=edicao
        )
        self.ramo_ia = ramo_ia.strip()
        self.frameworks = frameworks or []
        self.foco_matematico = foco_matematico.strip()

    def obter_ficha_catalografica(self) -> str:
        base = super().obter_ficha_catalografica()
        lista_fw = ", ".join(
            self.frameworks) if self.frameworks else "Conceitual"
        return (
            f"{base}\n"
            f"Ramo de IA: {self.ramo_ia} | Frameworks: {lista_fw} | Foco: {self.foco_matematico}"
        )


# ==============================================================================
# HIERARQUIA 2: COLEÇÕES TEMÁTICAS (AGREGAÇÃO E ESPECIALIZAÇÃO)
# ==============================================================================

class Colecao:
    """
    Classe base para agregação de itens do acervo.
    Gerencia inclusão, exclusão, buscas e estatísticas de um conjunto de itens.
    """

    def __init__(self, codigo: str, nome: str, descricao: str) -> None:
        self.codigo = codigo.strip().upper()
        self.nome = nome.strip()
        self.descricao = descricao.strip()
        self._itens: dict[str, ItemAcervo] = {}

    def validar_item_admissivel(self, item: ItemAcervo) -> None:
        """
        Método 'gancho' (hook) para ser sobrescrito por subclasses especializadas
        garantindo integridade de tipo na coleção.
        """
        if not isinstance(item, ItemAcervo):
            raise TypeError(
                "O item adicionado deve ser uma subclasse de ItemAcervo.")

    def adicionar_item(self, item: ItemAcervo) -> None:
        """Adiciona um item ao catálogo da coleção após validar sua admissibilidade."""
        self.validar_item_admissivel(item)
        self._itens[item.codigo] = item

    def remover_item(self, codigo: str) -> ItemAcervo | None:
        """Remove um item da coleção pelo seu código identificador."""
        return self._itens.pop(codigo.strip().upper(), None)

    def obter_item(self, codigo: str) -> ItemAcervo | None:
        """Recupera um item da coleção pelo código."""
        return self._itens.get(codigo.strip().upper())

    def buscar_por_titulo(self, termo: str) -> list[ItemAcervo]:
        """Busca itens cujo título contenha o termo fornecido (case-insensitive)."""
        termo_lower = termo.strip().lower()
        return [item for item in self._itens.values() if termo_lower in item.titulo.lower()]

    def buscar_por_autor(self, termo: str) -> list[ItemAcervo]:
        """Busca itens cujo autor contenha o termo fornecido (case-insensitive)."""
        termo_lower = termo.strip().lower()
        return [item for item in self._itens.values() if termo_lower in item.autor.lower()]

    def listar_disponiveis(self) -> list[ItemAcervo]:
        """Retorna todos os itens da coleção atualmente disponíveis para empréstimo."""
        return [item for item in self._itens.values() if item.disponivel]

    def estatisticas(self) -> dict[str, Any]:
        """Retorna resumo quantitativo da coleção."""
        total = len(self._itens)
        disponiveis = len(self.listar_disponiveis())
        return {
            "total_itens": total,
            "disponiveis": disponiveis,
            "emprestados": total - disponiveis,
        }

    def __len__(self) -> int:
        return len(self._itens)

    def __iter__(self) -> Iterator[ItemAcervo]:
        return iter(self._itens.values())

    def __contains__(self, codigo: str) -> bool:
        return codigo.strip().upper() in self._itens

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(codigo={self.codigo!r}, nome={self.nome!r}, itens={len(self)})"

    def __str__(self) -> str:
        stats = self.estatisticas()
        return (
            f"Coleção [{self.codigo}] {self.nome} - {stats['total_itens']} itens "
            f"({stats['disponiveis']} disponíveis)"
        )


class ColecaoLiteratura(Colecao):
    """
    Coleção especializada exclusivamente em obras de Literatura.
    Garante que nenhum item de outra área seja misturado.
    """

    def validar_item_admissivel(self, item: ItemAcervo) -> None:
        super().validar_item_admissivel(item)
        if not isinstance(item, LivroLiteratura):
            raise ItemIncompativelColecaoError(
                f"O item '{item.titulo}' não pertence à categoria de Literatura."
            )

    def filtrar_por_estilo(self, estilo: str) -> list[LivroLiteratura]:
        """Filtra obras por estilo literário (Romance, Ficção, Poesia, etc.)."""
        estilo_lower = estilo.strip().lower()
        return [
            item for item in self._itens.values()  # type: ignore[misc]
            if isinstance(item, LivroLiteratura) and estilo_lower in item.estilo_literario.lower()
        ]


class ColecaoHumanas(Colecao):
    """
    Coleção especializada exclusivamente em Ciências Humanas, Filosofia e História.
    """

    def validar_item_admissivel(self, item: ItemAcervo) -> None:
        super().validar_item_admissivel(item)
        if not isinstance(item, LivroHumanas):
            raise ItemIncompativelColecaoError(
                f"O item '{item.titulo}' não pertence à categoria de Ciências Humanas."
            )

    def filtrar_por_disciplina(self, disciplina: str) -> list[LivroHumanas]:
        """Filtra por disciplina (Filosofia, História, Sociologia, etc.)."""
        disc_lower = disciplina.strip().lower()
        return [
            item for item in self._itens.values()  # type: ignore[misc]
            if isinstance(item, LivroHumanas) and disc_lower in item.disciplina.lower()
        ]


class ColecaoTecnologia(Colecao):
    """
    Coleção especializada exclusivamente em Ciência da Computação, Exatas e Tecnologia.
    """

    def validar_item_admissivel(self, item: ItemAcervo) -> None:
        super().validar_item_admissivel(item)
        if not isinstance(item, LivroTecnologia):
            raise ItemIncompativelColecaoError(
                f"O item '{item.titulo}' não pertence à categoria de Tecnologia."
            )

    def filtrar_por_linguagem(self, linguagem: str) -> list[LivroComputacao]:
        """Filtra livros de computação por linguagem de programação."""
        lang_lower = linguagem.strip().lower()
        return [
            item for item in self._itens.values()
            if isinstance(item, LivroComputacao) and lang_lower in item.linguagem_programacao.lower()
        ]


# ==============================================================================
# HIERARQUIA 3: ASSOCIAÇÃO, USUÁRIOS E GESTÃO DA BIBLIOTECA
# ==============================================================================

class Usuario:
    """
    Representa o usuário cadastrado no sistema da biblioteca.
    Possui limite configurável de empréstimos simultâneos.
    """

    def __init__(
        self,
        id_usuario: str,
        nome: str,
        email: str,
        categoria: str = "Estudante",
        limite_emprestimos: int = 3,
    ) -> None:
        self.id_usuario = id_usuario.strip().upper()
        self.nome = nome.strip()
        self.email = email.strip()
        self.categoria = categoria.strip()
        self.limite_emprestimos = limite_emprestimos
        self.emprestimos_ativos: list[Emprestimo] = []

    def pode_pegar_emprestado(self) -> bool:
        """Verifica se o usuário ainda possui margem de empréstimos ativos."""
        return len(self.emprestimos_ativos) < self.limite_emprestimos

    def __repr__(self) -> str:
        return f"Usuario(id={self.id_usuario!r}, nome={self.nome!r}, categoria={self.categoria!r})"

    def __str__(self) -> str:
        return (
            f"[{self.id_usuario}] {self.nome} ({self.categoria}) - "
            f"Ativos: {len(self.emprestimos_ativos)}/{self.limite_emprestimos}"
        )


class Emprestimo:
    """
    Classe de Associação rica entre um Usuario e um ItemAcervo.
    Controla datas de retirada, prazo de devolução e cálculo polimórfico de multas.
    """

    def __init__(
        self,
        id_emprestimo: str,
        usuario: Usuario,
        item: ItemAcervo,
        data_emprestimo: date,
        prazo_dias: int = 14,
    ) -> None:
        self.id_emprestimo = id_emprestimo
        self.usuario = usuario
        self.item = item
        self.data_emprestimo = data_emprestimo
        self.data_prevista_devolucao = data_emprestimo + \
            timedelta(days=prazo_dias)
        self.data_devolucao_real: date | None = None
        self.multa_aplicada: float = 0.0

        # Efetua o bloqueio do item
        self.item.emprestar()
        self.usuario.emprestimos_ativos.append(self)

    def dias_atraso(self, data_referencia: date) -> int:
        """Calcula a quantidade de dias de atraso em relação à data limite."""
        if data_referencia > self.data_prevista_devolucao:
            return (data_referencia - self.data_prevista_devolucao).days
        return 0

    def finalizar_devolucao(self, data_devolucao: date) -> float:
        """
        Registra a devolução do item, libera o exemplar, recalcula a multa
        polimorficamente chamando o método do próprio ItemAcervo e desvincula do usuário.
        """
        self.data_devolucao_real = data_devolucao
        dias = self.dias_atraso(data_devolucao)

        # Polimorfismo em ação: cada tipo de item calcula sua própria taxa!
        self.multa_aplicada = self.item.calcular_taxa_atraso(dias)

        self.item.devolver()
        if self in self.usuario.emprestimos_ativos:
            self.usuario.emprestimos_ativos.remove(self)

        return self.multa_aplicada

    def __repr__(self) -> str:
        return f"Emprestimo(id={self.id_emprestimo!r}, item={self.item.codigo!r}, user={self.usuario.id_usuario!r})"

    def __str__(self) -> str:
        status = f"Devolvido em {self.data_devolucao_real}" if self.data_devolucao_real else "Em andamento"
        return (
            f"Empréstimo #{self.id_emprestimo}: '{self.item.titulo}' para {self.usuario.nome} | "
            f"Limite: {self.data_prevista_devolucao.strftime('%d/%m/%Y')} [{status}]"
        )


class Biblioteca:
    """
    Classe orquestradora (Fachada e Agregadora Central).
    Compõe múltiplas coleções temáticas, gerencia usuários e coordena empréstimos.
    """

    def __init__(self, nome: str, endereco: str) -> None:
        self.nome = nome.strip()
        self.endereco = endereco.strip()
        self.colecoes: dict[str, Colecao] = {}
        self.usuarios: dict[str, Usuario] = {}
        self.historico_emprestimos: list[Emprestimo] = []
        self._contador_emprestimos: int = 1000

    def registrar_colecao(self, colecao: Colecao) -> None:
        """Adiciona uma coleção temática à biblioteca."""
        self.colecoes[colecao.codigo] = colecao

    def cadastrar_usuario(self, usuario: Usuario) -> None:
        """Registra um usuário na biblioteca."""
        self.usuarios[usuario.id_usuario] = usuario

    def adicionar_item(self, codigo_colecao: str, item: ItemAcervo) -> None:
        """Encaminha a inclusão de um item para a coleção temática correspondente."""
        colecao = self.colecoes.get(codigo_colecao.strip().upper())
        if colecao is None:
            raise KeyError(
                f"Coleção com código '{codigo_colecao}' não encontrada.")
        colecao.adicionar_item(item)

    def realizar_emprestimo(
        self,
        id_usuario: str,
        codigo_item: str,
        data_atual: date,
        dias_prazo: int = 14,
    ) -> Emprestimo:
        """
        Executa um empréstimo validando cotas de usuário e disponibilidade do item
        em qualquer uma das coleções.
        """
        usuario = self.usuarios.get(id_usuario.strip().upper())
        if not usuario:
            raise KeyError(f"Usuário '{id_usuario}' não encontrado.")

        if not usuario.pode_pegar_emprestado():
            raise LimiteEmprestimosExcedidoError(
                f"O usuário '{usuario.nome}' atingiu o limite de {usuario.limite_emprestimos} empréstimos."
            )

        # Procura o item nas coleções
        item_alvo: ItemAcervo | None = None
        for col in self.colecoes.values():
            if codigo_item in col:
                item_alvo = col.obter_item(codigo_item)
                break

        if not item_alvo:
            raise KeyError(
                f"Item com código '{codigo_item}' não existe em nenhuma coleção.")

        self._contador_emprestimos += 1
        id_emp = f"EMP-{self._contador_emprestimos}"

        emprestimo = Emprestimo(
            id_emprestimo=id_emp,
            usuario=usuario,
            item=item_alvo,
            data_emprestimo=data_atual,
            prazo_dias=dias_prazo,
        )
        self.historico_emprestimos.append(emprestimo)
        return emprestimo

    def registrar_devolucao(
        self, id_emprestimo: str, data_devolucao: date
    ) -> float:
        """Processa a devolução de um empréstimo pelo ID e retorna a multa (se houver)."""
        for emp in self.historico_emprestimos:
            if emp.id_emprestimo == id_emprestimo:
                return emp.finalizar_devolucao(data_devolucao)
        raise KeyError(f"Empréstimo '{id_emprestimo}' não encontrado.")

    def pesquisar_acervo(self, termo: str) -> list[tuple[str, ItemAcervo]]:
        """Pesquisa um termo por título em todas as coleções temáticas."""
        resultados: list[tuple[str, ItemAcervo]] = []
        for col in self.colecoes.values():
            for item in col.buscar_por_titulo(termo):
                resultados.append((col.nome, item))
        return resultados

    def total_itens(self) -> int:
        """Calcula o total de itens somando todas as coleções."""
        return sum(len(col) for col in self.colecoes.values())

    def gerar_relatorio_inventario(self) -> str:
        """Gera um relatório completo de todas as coleções e seus itens."""
        linhas: list[str] = []
        linhas.append("=" * 80)
        linhas.append(f" INVENTÁRIO GERAL: {self.nome.upper()}")
        linhas.append(f" Endereço: {self.endereco}")
        linhas.append(
            f" Total de Coleções: {len(self.colecoes)} | Total de Itens: {self.total_itens()}")
        linhas.append("=" * 80)

        for col in self.colecoes.values():
            stats = col.estatisticas()
            linhas.append(
                f"\n>> {col.nome.upper()} [{col.codigo}] - {col.descricao}")
            linhas.append(
                f"   Acervo: {stats['total_itens']} itens | Disponíveis: {stats['disponiveis']}")
            linhas.append("-" * 80)

            for item in col:
                linhas.append(f"   • {item}")

        linhas.append("\n" + "=" * 80)
        return "\n".join(linhas)


# ==============================================================================
# DEMONSTRAÇÃO PRÁTICA DO SISTEMA
# ==============================================================================

def main() -> None:
    """Execução demonstrativa de todas as classes e comportamentos da Biblioteca."""
    print("=" * 85)
    print(" EXERCÍCIO 17.2 - SISTEMA INTEGRADO DE BIBLIOTECA (HIERARQUIA DE 19 CLASSES)")
    print("=" * 85)

    # 1. Instanciação da Biblioteca Central
    biblio = Biblioteca(
        nome="Biblioteca Central do Saber e Tecnologia",
        endereco="Av. das Humanidades, 1500 - Cidade Universitária",
    )

    # 2. Instanciação das Coleções Temáticas Especializadas
    col_lit = ColecaoLiteratura(
        codigo="COL-LIT",
        nome="Coleção Clássicos e Contemporâneos da Literatura",
        descricao="Obras de prosa, ficção científica, distopias e lírica poética mundial.",
    )
    col_hum = ColecaoHumanas(
        codigo="COL-HUM",
        nome="Coleção Ciências Humanas, Sociais e Filosofia",
        descricao="Obras essenciais de história, sociologia e correntes do pensamento filosófico.",
    )
    col_tec = ColecaoTecnologia(
        codigo="COL-TEC",
        nome="Coleção Tecnologia da Informação e Ciências Exatas",
        descricao="Livros técnicos de engenharia de software, ciência da computação e IA.",
    )

    biblio.registrar_colecao(col_lit)
    biblio.registrar_colecao(col_hum)
    biblio.registrar_colecao(col_tec)

    # 3. Povoamento da Coleção de Literatura (LivroLiteratura, LivroFiccao, LivroPoesia)
    col_lit.adicionar_item(
        LivroLiteratura(
            codigo="LIT-001",
            titulo="Dom Casmurro",
            autor="Machado de Assis",
            ano_publicacao=1899,
            localizacao="Estante L1-A",
            isbn="978-8572325394",
            editora="Garnier",
            numero_paginas=256,
            estilo_literario="Realismo Psicológico",
        )
    )
    col_lit.adicionar_item(
        LivroFiccao(
            codigo="LIT-002",
            titulo="1984",
            autor="George Orwell",
            ano_publicacao=1949,
            localizacao="Estante L1-B",
            isbn="978-8535914849",
            editora="Companhia das Letras",
            numero_paginas=416,
            subgenero="Distopia Política",
            universo_ficcional="Oceania Totalitária",
            faixa_etaria_recomendada=16,
        )
    )
    col_lit.adicionar_item(
        LivroPoesia(
            codigo="LIT-003",
            titulo="A Rosa do Povo",
            autor="Carlos Drummond de Andrade",
            ano_publicacao=1945,
            localizacao="Estante L2-A",
            isbn="978-8535921823",
            editora="Record",
            numero_paginas=240,
            forma_metrica="Versos Livres e Modernistas",
            antologia=False,
            total_poemas=55,
        )
    )

    # 4. Povoamento da Coleção de Humanas (LivroHumanas, LivroFilosofia, LivroHistoria)
    col_hum.adicionar_item(
        LivroFilosofia(
            codigo="HUM-001",
            titulo="Crítica da Razão Pura",
            autor="Immanuel Kant",
            ano_publicacao=1781,
            localizacao="Estante H1-A",
            isbn="978-8533618336",
            editora="Vozes",
            numero_paginas=680,
            corrente_filosofica="Idealismo Transcendental",
            periodo_historico="Iluminismo Moderno",
        )
    )
    col_hum.adicionar_item(
        LivroFilosofia(
            codigo="HUM-002",
            titulo="O Existencialismo é um Humanismo",
            autor="Jean-Paul Sartre",
            ano_publicacao=1946,
            localizacao="Estante H1-B",
            isbn="978-8520921470",
            editora="Nova Fronteira",
            numero_paginas=130,
            corrente_filosofica="Existencialismo",
            periodo_historico="Filosofia Contemporânea",
        )
    )
    col_hum.adicionar_item(
        LivroHistoria(
            codigo="HUM-003",
            titulo="Raízes do Brasil",
            autor="Sérgio Buarque de Holanda",
            ano_publicacao=1936,
            localizacao="Estante H2-C",
            isbn="978-8535908923",
            editora="Companhia das Letras",
            numero_paginas=220,
            epoca_abordada="Brasil Colonial até Século XX",
            regiao_geografica="Brasil / América Latina",
            fontes_primarias=True,
        )
    )

    # 5. Povoamento da Coleção de Tecnologia (LivroTecnologia, LivroComputacao, LivroIA)
    col_tec.adicionar_item(
        LivroComputacao(
            codigo="TEC-001",
            titulo="Clean Architecture: O Guia do Artesão",
            autor="Robert C. Martin",
            ano_publicacao=2017,
            localizacao="Estante T1-A",
            isbn="978-8550804606",
            editora="Alta Books",
            numero_paginas=432,
            linguagem_programacao="Agnóstica (Java / Python / C++)",
            paradigma="Orientado a Objetos e Arquitetura Limpa",
            inclui_codigo_fonte=True,
        )
    )
    col_tec.adicionar_item(
        LivroComputacao(
            codigo="TEC-002",
            titulo="Fluent Python: Clear, Concise, and Effective Programming",
            autor="Luciano Ramalho",
            ano_publicacao=2022,
            localizacao="Estante T1-B",
            isbn="978-1492056355",
            editora="O'Reilly Media",
            numero_paginas=1014,
            linguagem_programacao="Python 3.10+",
            paradigma="Orientado a Objetos e Funcional",
            inclui_codigo_fonte=True,
            edicao=2,
        )
    )
    col_tec.adicionar_item(
        LivroInteligenciaArtificial(
            codigo="TEC-003",
            titulo="Deep Learning",
            autor="Ian Goodfellow, Yoshua Bengio e Aaron Courville",
            ano_publicacao=2016,
            localizacao="Estante T2-A",
            isbn="978-0262035613",
            editora="MIT Press",
            numero_paginas=800,
            ramo_ia="Redes Neurais Profundas & Representação de Dados",
            frameworks=["PyTorch", "TensorFlow"],
            foco_matematico="Álgebra Linear e Otimização Diferencial",
        )
    )

    # 6. Exibição do Inventário Geral
    print(biblio.gerar_relatorio_inventario())

    # 7. Demonstração de Polimorfismo e Ficha Catalográfica
    print("\n" + "=" * 80)
    print(" DEMONSTRAÇÃO DE POLIMORFISMO: FICHAS CATALOGRÁFICAS DETALHADAS")
    print("=" * 80)
    livros_amostra: list[ItemAcervo] = [
        col_lit.obter_item("LIT-002"),  # LivroFiccao
        col_hum.obter_item("HUM-001"),  # LivroFilosofia
        col_tec.obter_item("TEC-003"),  # LivroIA
    ]
    for livro in livros_amostra:
        if livro:
            print(f"\n{livro.obter_ficha_catalografica()}")
            print("-" * 50)

    # 8. Demonstração de Usuários, Empréstimo e Cálculo de Multas com Polimorfismo
    print("\n" + "=" * 80)
    print(" FLUXO OPERACIONAL DE EMPRÉSTIMO E DEVOLUÇÃO COM MULTA")
    print("=" * 80)

    usuario1 = Usuario(id_usuario="USR-01", nome="Camila Alencar",
                       email="camila@univ.br", categoria="Mestranda", limite_emprestimos=3)
    biblio.cadastrar_usuario(usuario1)

    data_hoje = date(2026, 11, 1)
    print(f"Data da Operação: {data_hoje.strftime('%d/%m/%Y')}")

    # Realiza empréstimo do livro de tecnologia
    emp1 = biblio.realizar_emprestimo(
        id_usuario="USR-01",
        codigo_item="TEC-001",
        data_atual=data_hoje,
        dias_prazo=14,
    )
    print(f"Empréstimo efetuado: {emp1}")

    # Simula devolução 20 dias após a data limite (atraso de 6 dias além do prazo de 14 dias)
    data_devolucao = data_hoje + timedelta(days=20)
    dias_atraso = emp1.dias_atraso(data_devolucao)
    multa = biblio.registrar_devolucao(emp1.id_emprestimo, data_devolucao)

    print(f"Data de devolução real: {data_devolucao.strftime('%d/%m/%Y')}")
    print(f"Dias de atraso: {dias_atraso} dias")
    print(
        f"Multa calculada (Taxa R$ 2,00/dia para Tecnologia): R$ {multa:,.2f}")
    print(
        f"Status do item 'TEC-001' após devolução: {'Disponível' if emp1.item.disponivel else 'Emprestado'}")

    # 9. Demonstração de Pesquisa Global no Acervo
    print("\n" + "=" * 80)
    print(" PESQUISA MULTI-COLEÇÃO: TERMO 'Python'")
    print("=" * 80)
    resultados = biblio.pesquisar_acervo("Python")
    for nome_col, item in resultados:
        print(f"Encontrado na [{nome_col}]: {item}")

    print("\n>> Execução concluída com sucesso!")


if __name__ == "__main__":
    main()
