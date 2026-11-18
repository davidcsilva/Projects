'''
17.8 Implemente uma hierarquia de herança de animais tal que contenha pelo menos seis níveis de derivação e
12 classes.
'''

from abc import ABC, abstractmethod


# ==============================================================================
# NÍVEL 1: REINO (CLASSE BASE ABSTRATA)
# ==============================================================================

class Animal(ABC):
    """Classe 1 (Nível 1 - Reino): Base comum a todos os animais."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int, peso_kg: float):
        self.nome_popular = nome_popular
        self.nome_cientifico = nome_cientifico
        self.idade = idade
        self.peso_kg = peso_kg
        self.energia = 100

    def alimentar(self, alimento: str) -> str:
        self.energia = min(100, self.energia + 20)
        return f"{self.nome_popular} alimentou-se de {alimento} (Energia: {self.energia}%)."

    @abstractmethod
    def emitir_som(self) -> str:
        """Cada espécie produz uma vocalização ou som característico."""

    @abstractmethod
    def locomover(self) -> str:
        """Define o modo principal de deslocamento do animal."""

    def __str__(self) -> str:
        return f"{self.nome_popular} ({self.nome_cientifico}) | {self.peso_kg} kg"


# ==============================================================================
# NÍVEL 2: FILO
# ==============================================================================

class Vertebrado(Animal, ABC):
    """Classe 2 (Nível 2 - Filo): Animais com coluna vertebral e crânio."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, sangue_quente: bool):
        super().__init__(nome_popular, nome_cientifico, idade, peso_kg)
        self.possui_coluna_vertebral = True
        self.sangue_quente = sangue_quente


class Invertebrado(Animal, ABC):
    """Classe 3 (Nível 2 - Filo): Animais sem coluna vertebral."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, exoesqueleto: bool):
        super().__init__(nome_popular, nome_cientifico, idade, peso_kg)
        self.possui_coluna_vertebral = False
        self.exoesqueleto = exoesqueleto


# ==============================================================================
# NÍVEL 3: CLASSE BIOLÓGICA
# ==============================================================================

class Mamifero(Vertebrado, ABC):
    """Classe 4 (Nível 3 - Classe): Vertebrados endotérmicos com glândulas mamárias e pelos."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, periodo_gestacao_dias: int):
        super().__init__(nome_popular, nome_cientifico, idade, peso_kg, sangue_quente=True)
        self.periodo_gestacao_dias = periodo_gestacao_dias

    def amamentar(self) -> str:
        return f"{self.nome_popular} está amamentando seus filhotes."


class Ave(Vertebrado):
    """Classe 5 (Nível 3 - Classe): Vertebrados com penas, bico e asas."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, envergadura_asas_m: float, pode_voar: bool = True):
        super().__init__(nome_popular, nome_cientifico, idade, peso_kg, sangue_quente=True)
        self.envergadura_asas_m = envergadura_asas_m
        self.pode_voar = pode_voar

    def emitir_som(self) -> str:
        return f"{self.nome_popular} canta ou pia."

    def locomover(self) -> str:
        if self.pode_voar:
            return f"{self.nome_popular} voa com envergadura de {self.envergadura_asas_m} m."
        return f"{self.nome_popular} caminha e nada (ave não voadora)."


class Reptil(Vertebrado):
    """Classe 6 (Nível 3 - Classe): Vertebrados ectotérmicos com escamas ou placas córneas."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, peconhento: bool = False):
        super().__init__(nome_popular, nome_cientifico, idade, peso_kg, sangue_quente=False)
        self.peconhento = peconhento

    def regular_temperatura(self) -> str:
        return f"{self.nome_popular} toma sol para aquecer o metabolismo."

    def emitir_som(self) -> str:
        return f"{self.nome_popular} emite um sibilo."

    def locomover(self) -> str:
        return f"{self.nome_popular} rasteja sobre o solo."


class Artropode(Invertebrado):
    """Classe 7 (Nível 3 - Classe): Invertebrados com exoesqueleto quitinoso e patas articuladas."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, numero_patas: int):
        super().__init__(nome_popular, nome_cientifico, idade, peso_kg, exoesqueleto=True)
        self.numero_patas = numero_patas

    def emitir_som(self) -> str:
        return f"{self.nome_popular} produz estridulação ou zumbido."

    def locomover(self) -> str:
        return f"{self.nome_popular} desloca-se usando {self.numero_patas} patas articuladas."


# ==============================================================================
# NÍVEL 4: ORDEM
# ==============================================================================

class Carnivoro(Mamifero, ABC):
    """Classe 8 (Nível 4 - Ordem): Mamíferos adaptados à predação com dentes carniceiros."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, periodo_gestacao_dias: int, forca_mordida_psi: int):
        super().__init__(nome_popular, nome_cientifico,
                         idade, peso_kg, periodo_gestacao_dias)
        self.forca_mordida_psi = forca_mordida_psi

    def cacar(self) -> str:
        self.energia = max(0, self.energia - 15)
        return f"{self.nome_popular} está caçando (mordida de {self.forca_mordida_psi} PSI)."


class Primata(Mamifero):
    """Classe 9 (Nível 4 - Ordem): Mamíferos com cérebro desenvolvido e polegares opositores."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, periodo_gestacao_dias: int, usa_ferramentas: bool = True):
        super().__init__(nome_popular, nome_cientifico,
                         idade, peso_kg, periodo_gestacao_dias)
        self.usa_ferramentas = usa_ferramentas

    def emitir_som(self) -> str:
        return f"{self.nome_popular} vocaliza chamados sociais complexos."

    def locomover(self) -> str:
        return f"{self.nome_popular} escala árvores e caminha sobre os membros."


# ==============================================================================
# NÍVEL 5: FAMÍLIA
# ==============================================================================

class Canideo(Carnivoro, ABC):
    """Classe 10 (Nível 5 - Família): Carnívoros corredores com olfato apurado (lobos, cães, raposas)."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, periodo_gestacao_dias: int, forca_mordida_psi: int,
                 velocidade_corrida_kmh: float):
        super().__init__(nome_popular, nome_cientifico, idade, peso_kg,
                         periodo_gestacao_dias, forca_mordida_psi)
        self.velocidade_corrida_kmh = velocidade_corrida_kmh

    def locomover(self) -> str:
        return f"{self.nome_popular} corre em perseguição a até {self.velocidade_corrida_kmh} km/h."


class Felideo(Carnivoro, ABC):
    """Classe 11 (Nível 5 - Família): Carnívoros ágeis com garras retráteis (leões, tigres, gatos)."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, periodo_gestacao_dias: int, forca_mordida_psi: int,
                 garras_retrateis: bool = True):
        super().__init__(nome_popular, nome_cientifico, idade, peso_kg,
                         periodo_gestacao_dias, forca_mordida_psi)
        self.garras_retrateis = garras_retrateis

    def locomover(self) -> str:
        return f"{self.nome_popular} move-se silenciosamente e salta com precisão."


# ==============================================================================
# NÍVEL 6: GÊNERO
# ==============================================================================

class Canis(Canideo, ABC):
    """Classe 12 (Nível 6 - Gênero): Canídeos sociais que vivem em matilhas."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, velocidade_corrida_kmh: float, membro_matilha: bool = True):
        super().__init__(
            nome_popular=nome_popular,
            nome_cientifico=nome_cientifico,
            idade=idade,
            peso_kg=peso_kg,
            periodo_gestacao_dias=63,
            forca_mordida_psi=320,
            velocidade_corrida_kmh=velocidade_corrida_kmh,
        )
        self.membro_matilha = membro_matilha

    def uivar(self) -> str:
        return f"{self.nome_popular} uiva para se comunicar com a matilha."


class Panthera(Felideo, ABC):
    """Classe 13 (Nível 6 - Gênero): Grandes felinos capazes de rugir devido à anatomia da laringe."""

    def __init__(self, nome_popular: str, nome_cientifico: str, idade: int,
                 peso_kg: float, forca_mordida_psi: int):
        super().__init__(
            nome_popular=nome_popular,
            nome_cientifico=nome_cientifico,
            idade=idade,
            peso_kg=peso_kg,
            periodo_gestacao_dias=110,
            forca_mordida_psi=forca_mordida_psi,
            garras_retrateis=True,
        )

    def rugir(self) -> str:
        return f"{self.nome_popular} emite um rugido audível a quilômetros!"


# ==============================================================================
# NÍVEL 7: ESPÉCIE (CONCRETAS)
# ==============================================================================

class CachorroDomestico(Canis):
    """Classe 14 (Nível 7 - Espécie): Subespécie domesticada de Canis lupus."""

    def __init__(self, nome_individuo: str, raca: str, idade: int, peso_kg: float):
        super().__init__(
            nome_popular=f"Cachorro ({nome_individuo} - {raca})",
            nome_cientifico="Canis lupus familiaris",
            idade=idade,
            peso_kg=peso_kg,
            velocidade_corrida_kmh=45.0,
            membro_matilha=True,
        )
        self.raca = raca

    def emitir_som(self) -> str:
        return f"{self.nome_popular}: Au! Au!"

    def obedecer_comando(self, comando: str) -> str:
        return f"{self.nome_popular} executou o comando '{comando}'."


class Leao(Panthera):
    """Classe 15 (Nível 7 - Espécie): Grande felino africano de vida social em bandos."""

    def __init__(self, nome_individuo: str, idade: int, peso_kg: float, possui_juba: bool = True):
        super().__init__(
            nome_popular=f"Leão ({nome_individuo})",
            nome_cientifico="Panthera leo",
            idade=idade,
            peso_kg=peso_kg,
            forca_mordida_psi=650,
        )
        self.possui_juba = possui_juba

    def emitir_som(self) -> str:
        return self.rugir()


# ==============================================================================
# EXECUÇÃO E VERIFICAÇÃO DA PROFUNDIDADE DA HIERARQUIA
# ==============================================================================

if __name__ == "__main__":
    rex = CachorroDomestico("Rex", "Pastor Alemão", idade=4, peso_kg=34.0)
    simba = Leao("Simba", idade=6, peso_kg=190.0, possui_juba=True)
    aguia = Ave("Águia-real", "Aquila chrysaetos", idade=5,
                peso_kg=4.8, envergadura_asas_m=2.1)
    cobra = Reptil("Cascavel", "Crotalus durissus",
                   idade=3, peso_kg=1.5, peconhento=True)
    abelha = Artropode("Abelha-europeia", "Apis mellifera",
                       idade=1, peso_kg=0.0001, numero_patas=6)

    # Verificando os 7 níveis de derivação via MRO (Method Resolution Order)
    cadeia_heranca = [
        cls.__name__ for cls in CachorroDomestico.__mro__ if cls not in (object, ABC)]
    print(
        f"Profundidade da cadeia de CachorroDomestico ({len(cadeia_heranca)} níveis):")
    print(" -> ".join(reversed(cadeia_heranca)))
    print("-" * 80)

    # Demonstração polimórfica de todos os ramos da árvore
    animais: list[Animal] = [rex, simba, aguia, cobra, abelha]
    for animal in animais:
        print(animal)
        print(f"  Som:        {animal.emitir_som()}")
        print(f"  Locomoção:  {animal.locomover()}")
        print(f"  Alimentar:  {animal.alimentar('ração/presa natural')}\n")

    # Métodos específicos herdados nos níveis intermediários
    print(rex.amamentar())                 # Herdado de Mamifero (Nível 3)
    print(rex.uivar())                     # Herdado de Canis (Nível 6)
    # Próprio de CachorroDomestico (Nível 7)
    print(rex.obedecer_comando("Sentar"))
    print(simba.cacar())                   # Herdado de Carnivoro (Nível 4)
