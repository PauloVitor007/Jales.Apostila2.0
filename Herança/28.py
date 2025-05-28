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

class JogadorPremium(Jogador):
    def __init__(self, nome, energia, pontos, bonus_pontos):
        super().__init__(nome, energia, pontos)
        self.bonus_pontos = bonus_pontos
    
    def vencer_desafio(self):
        self.pontos += 10 + self.bonus_pontos
        print(f"{self.nome} venceu o desafio! Pontos bônus: {self.bonus_pontos}. Pontuação total: {self.pontos}")

jogador_premium = JogadorPremium("Herói Premium", 100, 0, 5)

inimigo = Inimigo("Goblin", 50, 15)
jogador_premium.atacar(inimigo)
jogador_premium.vencer_desafio()
