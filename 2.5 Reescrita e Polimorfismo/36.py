class Personagem:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print(f"{self.nome} diz: Olá, sou um personagem comum!")

class NPC(Personagem):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo
    
    def falar(self):
        print(f"{self.nome} diz: Sou um NPC do tipo {self.tipo}, aqui para ajudar!")

personagem = Personagem("Herói")
npc = NPC("Vendedor", "Comerciante")
personagem.falar()
npc.falar()
