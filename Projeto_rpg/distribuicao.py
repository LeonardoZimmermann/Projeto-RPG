import random

class EstiloDistribuicao:
    def rolar_dados(self, quantidade, lados):
        """Rola 'quantidade' de dados de 'lados' lados e retorna a soma"""
        return sum(random.randint(1, lados) for _ in range(quantidade))
