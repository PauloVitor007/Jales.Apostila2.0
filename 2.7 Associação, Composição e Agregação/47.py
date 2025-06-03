class Missao:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
    
    def completar(self):
        print(f"Missão {self.nome} completada: {self.descricao}")

class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
        self.missoes = []
    
    def aceitar_missao(self, missao):
        self.missoes.append(missao)
        print(f"{self.nome} aceitou a missão: {missao.nome}")
    
    def listar_missoes(self):
        if not self.missoes:
            print(f"{self.nome} não tem missões atualmente.")
        else:
            print(f"Missões de {self.nome}:")
            for missao in self.missoes:
                print(f"- {missao.nome}: {missao.descricao}")
    
    def completar_missoes(self):
        if not self.missoes:
            print(f"{self.nome} não tem missões para completar.")
        else:
            for missao in self.missoes:
                missao.completar()

missao1 = Missao("Salvar a aldeia", "Proteger a aldeia dos invasores.")
missao2 = Missao("Exploração da caverna", "Explorar a caverna e coletar itens valiosos.")
missao3 = Missao("Derrotar o dragão", "Derrotar o dragão que ameaça o reino.")
personagem = Personagem("Arthur", 10)
personagem.aceitar_missao(missao1)
personagem.aceitar_missao(missao2)
personagem.aceitar_missao(missao3)
personagem.listar_missoes()
personagem.completar_missoes()
