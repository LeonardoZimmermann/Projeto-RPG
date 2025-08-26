import random

class EstiloDistribuicao:
    def rolar_dados(self, quantidade, lados):
        """Rola 'quantidade' de dados de 'lados' lados e retorna a soma"""
        return sum(random.randint(1, lados) for _ in range(quantidade))


class EstiloClassico(EstiloDistribuicao):
    def aplicar(self, personagem):
        print("\n--- Estilo Clássico ---")
        atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

        for atributo in atributos:
            valor = self.rolar_dados(3, 6)
            setattr(personagem, atributo, valor)
            print(f"{atributo.capitalize()}: {valor}")


class EstiloAventureiro(EstiloDistribuicao):
    def aplicar(self, personagem):
        print("\n--- Estilo Aventureiro ---")
        atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

        valores = [self.rolar_dados(3, 6) for _ in range(6)]


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


class EstiloHeroico(EstiloDistribuicao):
    def aplicar(self, personagem):
        print("\n--- Estilo Heróico ---")
        atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

        valores = []
        for _ in range(6):
            dados = [random.randint(1, 6) for _ in range(4)]
            dados.remove(min(dados))  
            valores.append(sum(dados))

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
