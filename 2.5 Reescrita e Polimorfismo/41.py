class Fase:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade
    
    def gerar_inimigos(self):
        pass

class FaseFloresta(Fase):
    def __init__(self, nome, dificuldade, vegetacao):
        super().__init__(nome, dificuldade)
        self.vegetacao = vegetacao
    
    def gerar_inimigos(self):
        print(f"Inimigos da {self.nome}: Lobos e Aranhas.")

class FaseDeserto(Fase):
    def __init__(self, nome, dificuldade, temperatura):
        super().__init__(nome, dificuldade)
        self.temperatura = temperatura
    
    def gerar_inimigos(self):
        print(f"Inimigos da {self.nome}: Escorpiões e Cobras do deserto.")

fase_floresta = FaseFloresta("Floresta Sombria", "Alta", "Densa e cheia de árvores altas")
fase_deserto = FaseDeserto("Deserto Escaldante", "Média", 45)

fase_floresta.gerar_inimigos()
fase_deserto.gerar_inimigos()
