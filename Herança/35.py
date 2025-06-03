class Aliado:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
    
    def habilidade_especial(self):
        pass

class Mago(Aliado):
    def __init__(self, nome, poder_magico):
        super().__init__(nome, "Mago")
        self.poder_magico = poder_magico
    
    def habilidade_especial(self):
        print(f"{self.nome} usou 'Raio de Fogo'! Causa {self.poder_magico} de dano mágico aos inimigos.")

class Guerreiro(Aliado):
    def __init__(self, nome, forca_fisica):
        super().__init__(nome, "Guerreiro")
        self.forca_fisica = forca_fisica
    
    def habilidade_especial(self):
        print(f"{self.nome} usou 'Golpe Mortal'! Causa {self.forca_fisica} de dano físico aos inimigos.")

mago = Mago("Gandalf", 50)
guerreiro = Guerreiro("Conan", 70)
mago.habilidade_especial()
guerreiro.habilidade_especial()
