class bancoview:


    def cliente(self):
        return input('qual o nome do cliente? ')

    
    def menu(self):
        print('\n ====== Banco Legal ====== ')
        print('pressione 1 para depositar ')
        print('pressione 2 para sacar ')
        print('pressione 3 para sair ')
        print('pressione 4 para extrato ')
        

    def tipo_transacao(self):
        return int(input())
    def quantia(self):
        return float(input())
    def exibir_mensagem(self, mensagem):
        print(f'\n>> {mensagem}')
  
    