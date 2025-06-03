class Item:
    def __init__(self, nome):
        self.nome = nome
    
    def usar(self):
        pass

class Pocao(Item):
    def __init__(self, nome, tipo, efeito):
        super().__init__(nome)
        self.tipo = tipo
        self.efeito = efeito
    
    def usar(self):
        print(f"Você usou {self.nome}, uma poção {self.tipo}. Efeito: {self.efeito}.")

class Equipamento(Item):
    def __init__(self, nome, tipo, durabilidade):
        super().__init__(nome)
        self.tipo = tipo
        self.durabilidade = durabilidade
    
    def usar(self):
        print(f"Você equipou {self.nome}, um {self.tipo}. Durabilidade: {self.durabilidade}.")

pocao = Pocao("Poção de Cura", "de Cura", "Recupera 50 de HP")
equipamento = Equipamento("Espada de Ferro", "Espada", "Durabilidade 100/100")
pocao.usar()
equipamento.usar()
