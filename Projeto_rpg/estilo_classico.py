from distribuicao import EstiloDistribuicao

class EstiloClassico(EstiloDistribuicao):
    def aplicar(self, personagem):
        print("\n--- Estilo Clássico ---")
        atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

        for atributo in atributos:
            valor = self.rolar_dados(3, 6)
            setattr(personagem, atributo, valor)
            print(f"{atributo.capitalize()}: {valor}")
