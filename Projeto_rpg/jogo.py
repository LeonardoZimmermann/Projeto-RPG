from atributos import Personagem
from distribuicao import EstiloClassico, EstiloAventureiro, EstiloHeroico
from classe import Guerreiro, Ladrao, Mago
from raca import Humano, Elfo, Anao, Halfling

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
            print("Opção Inválida.")
            return
        estilo.aplicar(personagem)
        
        print("\nEscolha uma raça: ")
        racas = {
            "1": Humano,
            "2": Elfo,
            "3": Anao,
            "4": Halfling
        }

        for k, cls in racas.items():
            print(f"{k} - {cls.__name__}")
        escolha_raca = input("Opção: ")
        raca_cls = racas.get(escolha_raca)
        
        if not raca_cls:
            print("Opção Inválida.")
            return
        personagem.raca = raca_cls()

        print("\nEscolha uma classe: ")
        classes = {
            "1": Guerreiro,
            "2": Ladrao,
            "3": Mago
        }

        for k, cls in classes.items():
            print(f"{k} - {cls.__name__}")
        
        escolha_classe = input("Opção: ")
        classe_cls = classes.get(escolha_classe)
        if not classe_cls:
            print("Opção Inválida.")
            return

        personagem.classe = classe_cls()
        print("\n==============================")
        print("   PERSONAGEM FINALIZADO")
        print("==============================")
        personagem.exibir_atributos()
        personagem.raca.exibir_info()
        personagem.classe.exibir_info()
        print("==============================")
