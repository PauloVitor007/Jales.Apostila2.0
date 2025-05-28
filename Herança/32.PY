class Missao:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade
    
    def recompensar(self):
        pass

class MissaoPrincipal(Missao):
    def __init__(self, nome, dificuldade, recompensa):
        super().__init__(nome, dificuldade)
        self.recompensa = recompensa
    
    def recompensar(self):
        print(f"Missão Principal: {self.nome}. Recompensa: {self.recompensa}. Dificuldade: {self.dificuldade}.")

class MissaoSecundaria(Missao):
    def __init__(self, nome, dificuldade, recompensa):
        super().__init__(nome, dificuldade)
        self.recompensa = recompensa
    
    def recompensar(self):
        print(f"Missão Secundária: {self.nome}. Recompensa: {self.recompensa}. Dificuldade: {self.dificuldade}.")

missao_principal = MissaoPrincipal("Salvar a Aldeia", "Alta", "1000 de Ouro")
missao_secundaria = MissaoSecundaria("Caçar Lobos", "Média", "50 de Ouro")
missao_principal.recompensar()
missao_secundaria.recompensar()
