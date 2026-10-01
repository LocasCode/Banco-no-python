from view.view import bancoview
from model.model import Conta



class Controller:
    def __init__(self):
        self.model = Conta()
        self.view = bancoview()
        
    def iniciar(self):
        clientenome = self.view.cliente()

        self.view.exibir_mensagem(f'oi! {clientenome}')
        
        while  True:
            self.view.menu()
            