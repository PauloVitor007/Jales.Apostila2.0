class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} morreu!")
        else:
            print(f"{self.nome} tem {self.vida} de vida restante.")

    def atacar(self, alvo):
        dano = 10
        alvo.tomar_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")

personagem = Personagem("Herói", 100)

inimigo = Personagem("Goblin", 50)

personagem.atacar(inimigo)
