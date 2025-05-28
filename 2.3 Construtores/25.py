class Menu:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def iniciar_jogo(self):
        print(f"{self.titulo} - Iniciando o jogo!")
    
    def mostrar_opcoes(self):
        print(f"{self.titulo} - Escolha uma opção:")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")
    
    def sair(self):
        print(f"{self.titulo} - Saindo do jogo!")

menu = Menu("Menu Principal")
menu.mostrar_opcoes()
menu.iniciar_jogo()
menu.sair()
