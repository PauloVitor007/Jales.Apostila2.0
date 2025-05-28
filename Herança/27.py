class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca
    
    def atacar(self, alvo):
        dano = self.forca
        alvo.tomar_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} morreu!")
        else:
            print(f"{self.nome} tem {self.vida} de vida restante.")

class Chefe(Inimigo):
    def __init__(self, nome):
        super().__init__(nome, vida=200, forca=30)
chefe = Chefe("Dragão Supremo")
inimigo = Inimigo("Goblin", 50, 15)
chefe.atacar(inimigo)
inimigo.atacar(chefe)
