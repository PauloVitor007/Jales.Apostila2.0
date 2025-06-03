class Guerreiro:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder
    
    def atacar(self):
        print(f"{self.nome} está atacando com poder de {self.poder}!")

class AnimalMontaria:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    
    def montar(self):
        print(f"{self.nome} está montado em um {self.tipo}!")

class Cavaleiro(Guerreiro, AnimalMontaria):
    def __init__(self, nome, poder, tipo_montaria, nome_montaria):
        Guerreiro.__init__(self, nome, poder)
        AnimalMontaria.__init__(self, nome_montaria, tipo_montaria)
    
    def atacar(self):
        super().atacar()
        print(f"O cavaleiro {self.nome} ataca montado em {self.nome_montaria}!")

    def montar(self):
        super().montar()
        print(f"{self.nome} agora está pronto para a batalha montado em {self.nome_montaria}!")

cavaleiro = Cavaleiro("Cavaleiro da Luz", 100, "Dragão", "FogoDragão")
cavaleiro.atacar()
cavaleiro.montar()
