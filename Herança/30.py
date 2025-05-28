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

class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.configuracoes = {}
    
    def salvar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' salva com o valor '{valor}'.")

    def mostrar_configuracoes(self):
        if self.configuracoes:
            print(f"{self.titulo} - Configurações Salvas:")
            for chave, valor in self.configuracoes.items():
                print(f"{chave}: {valor}")
        else:
            print("Nenhuma configuração salva.")

menu_avancado = MenuAvancado("Menu Avançado")
menu_avancado.salvar_configuracao("Dificuldade", "Média")
menu_avancado.salvar_configuracao("Idioma", "Português")
menu_avancado.mostrar_configuracoes()
menu_avancado.mostrar_opcoes()
menu_avancado.sair()
