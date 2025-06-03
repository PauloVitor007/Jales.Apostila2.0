class Menu:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def exibir(self):
        print(f"{self.titulo} - Exibindo opções padrão:")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")

class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
    
    def exibir(self):
        super().exibir()
        print(f"{self.titulo} - Exibindo opções avançadas:")
        print("4. Alterar Configurações")
        print("5. Salvar Jogo")
        print("6. Carregar Jogo")

menu_avancado = MenuAvancado("Menu Avançado")
menu_avancado.exibir()
