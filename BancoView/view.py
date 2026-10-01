class bancoview:


    def cliente(self):
        return input('qual o nome do cliente? ')

    
    def menu(self):
        print('\n ====== Banco Legal ====== ')
        print('pressione 1 para depositar ')
        print('pressione 2 para sacar (5% de taxa) ')
        print('pressione 3 para sair ')
        print('pressione 4 para extrato ')
        

    def escolha_banco(self):
        try:
            return int(input())
        except ValueError:
            return None
    def quantia(self):
        return float(input())
    
    def exibir_mensagem(self, mensagem):
        print(f'\n>> {mensagem}')
  
    def input_invalido(self):
        print('Input Invalido') 
    def Movimentacao(self):
        print('Nenhuma movimentação realizada')