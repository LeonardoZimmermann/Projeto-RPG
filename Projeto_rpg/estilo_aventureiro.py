from distribuicao import EstiloDistribuicao

class EstiloAventureiro(EstiloDistribuicao):
    def aplicar(self, personagem):
        print("\n--- Estilo Aventureiro ---")
        atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

        valores = [self.rolar_dados(3, 6) for _ in range(6)]
        print("Valores rolados:", valores)

        for valor in valores:
            print(f"\nValor disponível: {valor}")
            print("Atributos disponíveis:", [a.capitalize() for a in atributos])

            while True:
                escolha = input("Escolha um atributo para aplicar este valor: ").lower()
                if escolha in atributos:
                    setattr(personagem, escolha, valor)
                    atributos.remove(escolha)
                    break
                else:
                    print("Atributo inválido, tente novamente.")
