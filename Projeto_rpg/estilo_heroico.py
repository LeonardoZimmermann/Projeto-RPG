import random
from distribuicao import EstiloDistribuicao

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
