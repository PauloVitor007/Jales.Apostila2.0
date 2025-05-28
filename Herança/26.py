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

class NPC(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def atacar(self, alvo):
        print(f"{self.nome} não pode atacar!")

personagem = Personagem("Herói", 100)
npc = NPC("Vendedor", 50)

npc.atacar(personagem)
personagem.atacar(npc)
