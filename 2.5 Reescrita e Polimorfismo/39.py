class Jogo:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def iniciar(self):
        print(f"{self.titulo} - Iniciando o jogo!")

    def mostrar_opcoes(self):
        print(f"{self.titulo} - Escolha uma opção:")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")
    
    def sair(self):
        print(f"{self.titulo} - Saindo do jogo!")

class JogoMultiplayer(Jogo):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.jogadores = []
    
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"{jogador} foi adicionado ao jogo!")

    def mostrar_jogadores(self):
        if self.jogadores:
            print("Jogadores no jogo:")
            for jogador in self.jogadores:
                print(jogador)
        else:
            print("Não há jogadores no jogo.")

    def iniciar(self):
        if len(self.jogadores) > 1:
            print(f"{self.titulo} - Jogo Multiplayer Iniciado!")
            print("Jogadores conectados:")
            self.mostrar_jogadores()
        else:
            print("Não é possível iniciar o jogo. É necessário mais de um jogador.")

jogo_multiplayer = JogoMultiplayer("Jogo Online Multiplayer")

jogo_multiplayer.adicionar_jogador("Jogador1")
jogo_multiplayer.adicionar_jogador("Jogador2")

jogo_multiplayer.iniciar()
jogo_multiplayer.mostrar_opcoes()
jogo_multiplayer.sair()
