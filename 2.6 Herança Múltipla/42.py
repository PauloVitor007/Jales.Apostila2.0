class Inimigo:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder
    
    def atacar(self):
        print(f"{self.nome} está atacando com poder {self.poder}!")

class Voador:
    def voar(self):
        print("Está voando pelos céus!")

class Dragao(Inimigo, Voador):
    def __init__(self, nome, poder, tipo_fogo):
        Inimigo.__init__(self, nome, poder)
        self.tipo_fogo = tipo_fogo
    
    def atacar(self):
        super().atacar()
        print(f"O dragão lança {self.tipo_fogo} do seu fogo!")

dragao = Dragao("Dragão de Fogo", 100, "fogo ardente")
dragao.atacar()
dragao.voar()
