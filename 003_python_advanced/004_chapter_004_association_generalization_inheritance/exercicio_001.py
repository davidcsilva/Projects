"""
Capítulo 04 - Associação, Generalização e Herança
Exercício 17.1

Enunciado:
17.1 Defina uma classe base Pessoa que contenha informação de propósito geral comum a todas as pessoas
(nome, endereço, data de nascimento, sexo etc.). Projete uma hierarquia de classes que contemple as
classes seguintes: estudante, empregado, estudante_empregado.
Escreva um programa que leia um arquivo de informação e crie uma lista de pessoas:
    a) geral;
    b) estudantes;
    c) empregados;
    d) estudantes empregados.
O propósito deve permitir ordenar alfabeticamente pelo primeiro sobrenome.
"""

from __future__ import annotations

import csv
import functools
from pathlib import Path
import sys
import unicodedata
from typing import Any


# ==============================================================================
# HIERARQUIA DE CLASSES
# ==============================================================================

@functools.total_ordering
class Pessoa:
    """
    Classe base contendo informações gerais comuns a qualquer pessoa.

    Atributos:
        nome (str): Nome completo da pessoa.
        endereco (str): Endereço residencial.
        data_nascimento (str): Data de nascimento (ex: 'DD/MM/AAAA').
        sexo (str): Sexo/gênero da pessoa (ex: 'M', 'F').
    """

    def __init__(
        self,
        nome: str,
        endereco: str,
        data_nascimento: str,
        sexo: str,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.nome = nome.strip()
        self.endereco = endereco.strip()
        self.data_nascimento = data_nascimento.strip()
        self.sexo = sexo.strip().upper()

    @property
    def primeiro_sobrenome(self) -> str:
        """
        Extrai e retorna o primeiro sobrenome da pessoa.

        Regra de extração:
        - O nome completo é dividido por espaços em branco.
        - O primeiro termo é o prenome (ex: 'Maria').
        - O segundo termo é o primeiro sobrenome (ex: 'Silva' em 'Maria Silva Santos').
        - Se o segundo termo for uma preposição comum ('de', 'da', 'do', 'das', 'dos')
          e houver um terceiro termo, avança para ele (ex: 'João da Silva' -> 'Silva').
        - Caso a pessoa possua apenas um nome (monônimo), retorna a própria palavra.
        """
        partes = self.nome.strip().split()
        if len(partes) <= 1:
            return partes[0] if partes else ""

        preposicoes = {"de", "da", "do", "das", "dos"}
        if partes[1].lower() in preposicoes and len(partes) > 2:
            return partes[2]
        return partes[1]

    @property
    def chave_ordenacao(self) -> tuple[str, str]:
        """
        Gera a chave para ordenação alfabética insensível a maiúsculas/minúsculas
        e a acentuação.
        Critério primário: primeiro sobrenome normalizado.
        Critério secundário (desempate): nome completo normalizado.
        """
        def _normalizar(texto: str) -> str:
            nfkd = unicodedata.normalize("NFKD", texto)
            sem_acentos = "".join(
                c for c in nfkd if not unicodedata.combining(c))
            return sem_acentos.casefold()

        return (_normalizar(self.primeiro_sobrenome), _normalizar(self.nome))

    def __lt__(self, other: object) -> bool:
        """Permite ordenação natural comparando pelo primeiro sobrenome."""
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.chave_ordenacao < other.chave_ordenacao

    def __eq__(self, other: object) -> bool:
        """Verifica igualdade com base nos atributos identificadores."""
        if not isinstance(other, Pessoa):
            return NotImplemented
        return (
            self.nome == other.nome
            and self.endereco == other.endereco
            and self.data_nascimento == other.data_nascimento
            and self.sexo == other.sexo
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(nome={self.nome!r}, "
            f"endereco={self.endereco!r}, data_nascimento={self.data_nascimento!r}, "
            f"sexo={self.sexo!r})"
        )

    def __str__(self) -> str:
        return (
            f"[{self.__class__.__name__}] Nome: {self.nome} "
            f"(1º Sobrenome: {self.primeiro_sobrenome}) | "
            f"Nasc: {self.data_nascimento} | Sexo: {self.sexo} | "
            f"Endereço: {self.endereco}"
        )


class Estudante(Pessoa):
    """
    Representa um estudante. Herda atributos gerais de Pessoa e adiciona
    informações acadêmicas.

    Atributos específicos:
        matricula (str): Número ou código de matrícula.
        curso (str): Nome do curso de graduação ou pós-graduação.
    """

    def __init__(
        self,
        nome: str,
        endereco: str,
        data_nascimento: str,
        sexo: str,
        matricula: str,
        curso: str,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            nome=nome,
            endereco=endereco,
            data_nascimento=data_nascimento,
            sexo=sexo,
            **kwargs,
        )
        self.matricula = matricula.strip()
        self.curso = curso.strip()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(nome={self.nome!r}, "
            f"matricula={self.matricula!r}, curso={self.curso!r})"
        )

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Matrícula: {self.matricula} | Curso: {self.curso}"


class Empregado(Pessoa):
    """
    Representa um empregado. Herda atributos gerais de Pessoa e adiciona
    informações trabalhistas/profissionais.

    Atributos específicos:
        salario (float): Salário mensal do empregado.
        cargo (str): Cargo ou função desempenhada na empresa.
    """

    def __init__(
        self,
        nome: str,
        endereco: str,
        data_nascimento: str,
        sexo: str,
        salario: float | str,
        cargo: str,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            nome=nome,
            endereco=endereco,
            data_nascimento=data_nascimento,
            sexo=sexo,
            **kwargs,
        )
        self.salario = float(salario) if salario not in ("", None) else 0.0
        self.cargo = cargo.strip()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(nome={self.nome!r}, "
            f"cargo={self.cargo!r}, salario={self.salario!r})"
        )

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Cargo: {self.cargo} | Salário: R$ {self.salario:,.2f}"


class EstudanteEmpregado(Estudante, Empregado):
    """
    Representa uma pessoa que estuda e trabalha simultaneamente.
    Exemplo clássico de herança múltipla cooperativa em Python (MRO).

    Herda atributos de Estudante (matrícula, curso) e Empregado (salário, cargo),
    além de todos os dados gerais de Pessoa.
    """

    def __init__(
        self,
        nome: str,
        endereco: str,
        data_nascimento: str,
        sexo: str,
        matricula: str,
        curso: str,
        salario: float | str,
        cargo: str,
        **kwargs: Any,
    ) -> None:
        # A chamada cooperativa com super() repassa os argumentos através da MRO:
        # EstudanteEmpregado -> Estudante -> Empregado -> Pessoa -> object
        super().__init__(
            nome=nome,
            endereco=endereco,
            data_nascimento=data_nascimento,
            sexo=sexo,
            matricula=matricula,
            curso=curso,
            salario=salario,
            cargo=cargo,
            **kwargs,
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(nome={self.nome!r}, "
            f"matricula={self.matricula!r}, curso={self.curso!r}, "
            f"cargo={self.cargo!r}, salario={self.salario!r})"
        )

    def __str__(self) -> str:
        # super().__str__() invoca cooperativamente Estudante.__str__ e Empregado.__str__
        return super().__str__()


# ==============================================================================
# LEITURA E PERSISTÊNCIA DE DADOS
# ==============================================================================

def instanciar_pessoa_de_registro(dados: dict[str, str]) -> Pessoa:
    """
    Cria uma instância da classe adequada (Pessoa, Estudante, Empregado ou
    EstudanteEmpregado) a partir de um dicionário com os campos lidos do arquivo.
    """
    # Normaliza chaves para minúsculo
    d = {k.strip().lower(): v.strip()
         for k, v in dados.items() if k is not None}

    tipo = d.get("tipo", "pessoa").lower().replace("-", "_").replace(" ", "_")
    nome = d.get("nome", "")
    endereco = d.get("endereco", "")
    data_nasc = d.get("data_nascimento", "")
    sexo = d.get("sexo", "")
    matricula = d.get("matricula", "")
    curso = d.get("curso", "")
    cargo = d.get("cargo", "")
    salario_raw = d.get("salario", "0.0").replace(",", ".")

    try:
        salario = float(salario_raw) if salario_raw else 0.0
    except ValueError:
        salario = 0.0

    if tipo in ("estudante_empregado", "estudanteempregado"):
        return EstudanteEmpregado(
            nome=nome,
            endereco=endereco,
            data_nascimento=data_nasc,
            sexo=sexo,
            matricula=matricula,
            curso=curso,
            salario=salario,
            cargo=cargo,
        )
    elif tipo == "estudante":
        return Estudante(
            nome=nome,
            endereco=endereco,
            data_nascimento=data_nasc,
            sexo=sexo,
            matricula=matricula,
            curso=curso,
        )
    elif tipo in ("empregado", "funcionario"):
        return Empregado(
            nome=nome,
            endereco=endereco,
            data_nascimento=data_nasc,
            sexo=sexo,
            salario=salario,
            cargo=cargo,
        )
    elif tipo in ("pessoa", ""):
        return Pessoa(
            nome=nome,
            endereco=endereco,
            data_nascimento=data_nasc,
            sexo=sexo,
        )
    else:
        raise ValueError(
            f"Tipo de pessoa não reconhecido no arquivo: '{tipo}'")


def criar_arquivo_padrao_se_ausente(caminho: Path) -> None:
    """
    Cria um arquivo CSV com registros demonstrativos se o arquivo especificado
    não existir no disco.
    """
    if caminho.exists():
        return

    conteudo = (
        "tipo;nome;endereco;data_nascimento;sexo;matricula;curso;salario;cargo\n"
        "pessoa;Mariana Silva Alves;Rua das Acácias, 120;14/03/1995;F;;;;\n"
        "estudante;Carlos Pereira Rocha;Av. Brasil, 450;22/07/2002;M;EST202201;Engenharia de Software;;\n"
        "empregado;Beatriz Souza Santos;Rua Central, 89;10/11/1988;F;;;6500.00;Gerente de Projetos\n"
        "estudante_empregado;Rafael Gomes Barbosa;Rua das Palmeiras, 77;05/01/2000;M;EST202145;Ciência da Computação;3500.00;Desenvolvedor Júnior\n"
        "estudante;Alice Castro Oliveira;Rua Marechal, 310;19/09/2001;F;EST202312;Medicina;;\n"
        "empregado;Daniel Ribeiro Martins;Av. Paulista, 1000;03/04/1983;M;;;8200.00;Arquiteto de Soluções\n"
        "estudante_empregado;Juliana Mendes Duarte;Rua Bela Cintra, 45;17/08/1999;F;EST202088;Administração;4100.00;Assistente Financeiro\n"
        "pessoa;Fernando Lima Ferreira;Rua do Comércio, 55;29/12/1975;M;;;;\n"
        "estudante;Bruno Batista Toledo;Rua XV de Novembro, 88;12/06/2003;M;EST202403;Direito;;\n"
        "empregado;Camila Álvares Costa;Alameda Santos, 900;18/02/1991;F;;;7100.00;Engenheira de Dados\n"
    )
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(conteudo, encoding="utf-8")
    print(f">> Arquivo demonstrativo gerado com sucesso em: {caminho}")


def ler_arquivo_pessoas(caminho_arquivo: str | Path) -> list[Pessoa]:
    """
    Lê o arquivo de informação e instancia os objetos correspondentes.
    Suporta arquivos com delimitador ponto-e-vírgula (;) ou vírgula (,).
    """
    caminho = Path(caminho_arquivo)
    if not caminho.exists():
        criar_arquivo_padrao_se_ausente(caminho)

    linhas_filtradas: list[str] = []
    with caminho.open(mode="r", encoding="utf-8") as f:
        for linha in f:
            linha_limpa = linha.strip()
            # Ignora linhas em branco ou comentários
            if linha_limpa and not linha_limpa.startswith("#"):
                linhas_filtradas.append(linha_limpa)

    if not linhas_filtradas:
        return []

    # Detecta delimitador predominante na primeira linha
    primeira_linha = linhas_filtradas[0]
    delimitador = ";" if primeira_linha.count(
        ";") >= primeira_linha.count(",") else ","

    leitor = csv.DictReader(linhas_filtradas, delimiter=delimitador)
    pessoas: list[Pessoa] = []

    for numero_linha, registro in enumerate(leitor, start=2):
        try:
            pessoa = instanciar_pessoa_de_registro(registro)
            pessoas.append(pessoa)
        except Exception as erro:
            print(
                f"[AVISO] Erro ao processar linha {numero_linha}: {erro}", file=sys.stderr)

    return pessoas


# ==============================================================================
# CRIAÇÃO E ORDENAÇÃO DAS LISTAS
# ==============================================================================

def separar_listas(pessoas: list[Pessoa]) -> dict[str, list[Pessoa]]:
    """
    Cria as 4 listas solicitadas pelo enunciado:
        a) Geral: todas as pessoas cadastradas;
        b) Estudantes: todas as pessoas que são estudantes (isinstance);
        c) Empregados: todas as pessoas que são empregados (isinstance);
        d) Estudantes Empregados: pessoas que são simultaneamente estudante e empregado.
    """
    return {
        "geral": list(pessoas),
        "estudantes": [p for p in pessoas if isinstance(p, Estudante)],
        "empregados": [p for p in pessoas if isinstance(p, Empregado)],
        "estudantes_empregados": [p for p in pessoas if isinstance(p, EstudanteEmpregado)],
    }


def ordenar_por_primeiro_sobrenome(lista: list[Pessoa], reverse: bool = False) -> list[Pessoa]:
    """
    Retorna uma nova lista ordenada alfabeticamente pelo primeiro sobrenome.
    Como a classe Pessoa implementa __lt__ baseado em 'chave_ordenacao',
    a chamada a sorted() nativa produz diretamente esse resultado.
    """
    return sorted(lista, key=lambda p: p.chave_ordenacao, reverse=reverse)


# ==============================================================================
# EXIBIÇÃO FORMATADA DOS RESULTADOS
# ==============================================================================

def formatar_tabela_pessoas(pessoas: list[Pessoa], titulo: str) -> None:
    """
    Imprime no terminal uma tabela elegante exibindo as pessoas da lista,
    evidenciando o primeiro sobrenome e a classe do objeto.
    """
    print("\n" + "=" * 90)
    print(f" {titulo.upper()} (Total: {len(pessoas)})")
    print("=" * 90)

    if not pessoas:
        print("  (Nenhum registro encontrado)")
        return

    cabecalho = f"{'1º SOBRENOME':<16} | {'CLASSE':<20} | {'NOME COMPLETO':<30} | {'DETALHES ESPECÍFICOS'}"
    print(cabecalho)
    print("-" * 90)

    for p in pessoas:
        classe = p.__class__.__name__
        sobrenome = p.primeiro_sobrenome
        nome = p.nome

        detalhes: list[str] = []
        if isinstance(p, Estudante):
            detalhes.append(f"Curso: {p.curso} ({p.matricula})")
        if isinstance(p, Empregado):
            detalhes.append(f"Cargo: {p.cargo} (R$ {p.salario:,.2f})")
        if not isinstance(p, (Estudante, Empregado)):
            detalhes.append(f"Nasc: {p.data_nascimento} - End: {p.endereco}")

        detalhes_str = " | ".join(detalhes)
        print(f"{sobrenome:<16} | {classe:<20} | {nome:<30} | {detalhes_str}")


def main() -> None:
    """Função principal que orquestra a leitura, separação e ordenação."""
    print("=" * 90)
    print(" EXERCÍCIO 17.1 - HIERARQUIA DE PESSOAS E ORDENAÇÃO POR PRIMEIRO SOBRENOME")
    print("=" * 90)

    # Permite especificar o arquivo via argumento de linha de comando ou usa o padrão
    caminho_arquivo = Path(sys.argv[1]) if len(
        sys.argv) > 1 else Path("pessoas.csv")
    print(f"Lendo informações de: {caminho_arquivo.resolve()}")

    pessoas = ler_arquivo_pessoas(caminho_arquivo)
    print(f"Total de registros lidos: {len(pessoas)}")

    # a) Geral, b) Estudantes, c) Empregados, d) Estudantes Empregados
    listas = separar_listas(pessoas)

    titulos = {
        "geral": "a) Lista Geral de Pessoas",
        "estudantes": "b) Lista de Estudantes",
        "empregados": "c) Lista de Empregados",
        "estudantes_empregados": "d) Lista de Estudantes Empregados",
    }

    print("\n" + "#" * 90)
    print(" RESULTADOS ORDENADOS ALFABETICAMENTE PELO PRIMEIRO SOBRENOME")
    print("#" * 90)

    for chave, titulo in titulos.items():
        lista_ordenada = ordenar_por_primeiro_sobrenome(listas[chave])
        formatar_tabela_pessoas(
            lista_ordenada, f"{titulo} (Ordenada por 1º Sobrenome)")

    print("\n" + "=" * 90)
    print(" PROVA DE ORDENAÇÃO (Ordem alfabética do 1º sobrenome na Lista Geral):")
    print("=" * 90)
    geral_ordenada = ordenar_por_primeiro_sobrenome(listas["geral"])
    for i, p in enumerate(geral_ordenada, start=1):
        print(
            f"  {i:2d}. [{p.primeiro_sobrenome:<12}] -> {p.nome} ({p.__class__.__name__})")
    print("=" * 90)


if __name__ == "__main__":
    main()
