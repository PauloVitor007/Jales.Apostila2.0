class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    
    def atacar(self):
        print(f"A arma {self.nome} causa {self.dano} de dano!")

class Jogador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.arma = None
    
    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nome} agora está equipado com {self.arma.nome}.")
    
    def atacar(self):
        if self.arma:
            print(f"{self.nome} está atacando com a {self.arma.nome}!")
            self.arma.atacar()
        else:
            print(f"{self.nome} não está equipado com nenhuma arma.")

espada = Arma("Espad