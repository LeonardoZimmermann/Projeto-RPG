class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.classe = None
        self.raca = None

    def exibir_atributos(self):
        print(f"\n-- Atributos do Personagem: {self.nome} --")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Constituição: {self.constituicao}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")
