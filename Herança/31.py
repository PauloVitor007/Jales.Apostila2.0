class Arma:
    def __init__(self, nome):
        self.nome = nome
    
    def atacar(self):
        pass

class Espada(Arma):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo
    
    def atacar(self):
        print(f"{self.nome} é uma espada {self.tipo} e causa um corte rápido!")

class Arco(Arma):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo
    
    def atacar(self):
        print(f"{self.nome} é um arco {self.tipo} e dispara uma flecha a longa distância!")

espada = Espada("Espada Longa", "de duas mãos")
arco = Arco("Arco Curvo", "reflexo")
espada.atacar()
arco.atacar()
