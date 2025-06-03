class Mago:
    def __init__(self, nome, poder_magia):
        self.nome = nome
        self.poder_magia = poder_magia
    
    def lançar_magia(self):
        print(f"{self.nome} lançou uma magia com poder de {self.poder_magia}!")

class MagiaElemental:
    def __init__(self, elemento):
        self.elemento = elemento
    
    def lançar_magia(self):
        print(f"Lançando magia do elemento {self.elemento}!")

class MagoElemental(Mago, MagiaElemental):
    def __init__(self, nome, poder_magia, elemento):
        Mago.__init__(self, nome, poder_magia)
        MagiaElemental.__init__(self, elemento)
    
    def lançar_magia(self):
        super().lançar_magia()
        print(f"{self.nome} lança uma poderosa magia de {self.elemento} com {self.poder_magia} de poder!")

mago_fogo = MagoElemental("Mago do Fogo", 100, "Fogo")
mago_fogo.lançar_magia()
mago_agua = MagoElemental("Mago da Água", 80, "Água")
mago_agua.lançar_magia()
