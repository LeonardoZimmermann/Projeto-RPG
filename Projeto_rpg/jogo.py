from atributos import Personagem
from estilo_classico import EstiloClassico
from estilo_aventureiro import EstiloAventureiro
from estilo_heroico import EstiloHeroico

class Jogo:
    def iniciar(self):
        print("-- Criação de Personagem --")
        nome = input("Digite o nome do personagem: ")
        personagem = Personagem(nome)

        print("\nEscolha um estilo:")
        print("1 - Clássico (3d6 direto)")
        print("2 - Aventureiro (3d6, jogador distribui os valores)")
        print("3 - Heróico (4d6, descarta o menor, jogador distribui)")
        escolha = input("Opção: ")

        if escolha == "1":
            estilo = EstiloClassico()
        elif escolha == "2":
            estilo = EstiloAventureiro()
        elif escolha == "3":
            estilo = EstiloHeroico()
        else:
            print("Opção inválida.")
            return

        estilo.aplicar(personagem)
        personagem.exibir_atributos()
