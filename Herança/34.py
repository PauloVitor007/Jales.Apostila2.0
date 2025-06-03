class Fase:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade
    
    def descrever(self):
        pass

class FaseFloresta(Fase):
    def __init__(self, nome, dificuldade, vegetacao):
        super().__init__(nome, dificuldade)
        self.vegetacao = vegetacao
    
    def descrever(self):
        print(f"Fase: {self.nome}. Dificuldade: {self.dificuldade}. Vegetação: {self.vegetacao}. Uma floresta densa com muitos perigos.")

class FaseDeserto(Fase):
    def __init__(self, nome, dificuldade, temperatura):
        super().__init__(nome, dificuldade)
        self.temperatura = temperatura
    
    def descrever(self):
        print(f"Fase: {self.nome}. Dificuldade: {self.dificuldade}. Temperatura: {self.temperatura}°C. Um deserto árido e quente, onde os desafios são extremos.")

fase_floresta = FaseFloresta("Floresta Sombria", "Alta", "Densa e cheia de árvores altas")
fase_deserto = FaseDeserto("Deserto Escaldante", "Média", 45)
fase_floresta.descrever()
fase_deserto.descrever()
