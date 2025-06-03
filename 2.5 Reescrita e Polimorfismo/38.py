class Jogador:
    def __init__(self, nome, energia, pontos):
        self.nome = nome
        self.__energia = energia
        self.pontos = pontos
    
    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
        print(f"{self.nome} ganhou {quantidade} pontos. Pontuação total: {self.pontos}")
    
    def atacar(self, inimigo):
        if self.__energia >= 10:
            inimigo.tomar_dano(10)
            self.__energia -= 10
            self.adicionar_pontos(10)
        else:
            print(f"{self.nome} não tem energia suficiente para atacar!")

class JogadorPremium(Jogador):
    def __init__(self, nome, energia, pontos, multiplicador_pontos):
        super().__init__(nome, energia, pontos)
        self.multiplicador_pontos = multiplicador_pontos
    
    def adicionar_pontos(self, quantidade):
        pontos_adicionados = quantidade * self.multiplicador_pontos
        self.pontos += pontos_adicionados
        print(f"{self.nome} ganhou {pontos_adicionados} pontos (com multiplicador). Pontuação total: {self.pontos}")

jogador_premium = JogadorPremium("Herói Premium", 100, 0, 2)
inimigo = Inimigo("Goblin", 50, 15)
jogador_premium.atacar(inimigo)
