class Jogador:
    def __init__(self, nome, energia, pontos):
        self.nome = nome
        self.__energia = energia
        self.pontos = pontos
    
    def atacar(self, inimigo):
        if self.__energia >= 10:
            inimigo.tomar_dano(10)
            self.__energia -= 10
            self.pontos += 10
            print(f"{self.nome} atacou {inimigo.nome} causando 10 de dano. Pontos: {self.pontos}")
        else:
            print(f"{self.nome} não tem energia suficiente para atacar!")
    
    def descansar(self):
        self.__energia = min(self.__energia + 20, 100)
        print(f"{self.nome} descansou. Energia atual: {self.__energia}")
    
    def mostrar_energia(self):
        print(f"{self.nome} tem {self.__energia} de energia restante.")

jogador = Jogador("Herói", 100, 0)
inimigo = Inimigo("Goblin", 50, 15)

jogador.atacar(inimigo)
jogador.descansar()
jogador.mostrar_energia()
