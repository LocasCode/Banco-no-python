from BancoView.view import bancoview
from BancoModel.model import Conta
from BancoModel.model import Cliente


class BancoController:
    def __init__(self):
        self.model = Conta()
        self.view = bancoview()
        self.cliente = Cliente()
    def iniciar(self):
        self.cliente.cliente = self.view.cliente()
        self.view.exibir_mensagem(f'olá, {self.cliente.cliente}. seu saldo é de {self.model.saldo}')
        loop = 0
        while True:

            self.view.menu()
            escolha = self.view.escolha_banco()
            if escolha is None or escolha >= 5 or escolha <= 0:
                self.view.input_invalido()
            
            elif escolha == 1:
                    ValorDepositado = self.view.quantia()
                    if ValorDepositado > 0:
                        resultado = self.model.depositar(ValorDepositado)
                    else:
                        self.view.exibir_mensagem('Apenas números positivos!')
                
                        
            elif escolha == 2:
                    
                    ValorSacado = self.view.quantia()
                    resultado = self.model.sacar(ValorSacado)
                    if resultado is None:
                        self.view.exibir_mensagem(f'Dinheiro Insuficiente, acima do limite de saque R${self.model.limite_saque} ou numero inválido')
                
            elif escolha == 3:
                
                break
            elif escolha == 4 and loop > 0:
                self.view.exibir_mensagem(f'Seu saldo é: R${self.model.saldo}')
                for valor, horario in self.model.movimentacoesD:
                    self.view.exibir_mensagem(f'depositos: {valor}, {horario}')
                for valor, horario, taxa in self.model.movimentacoesS:
                    self.view.exibir_mensagem(f'saques: {valor}, {horario} valor após taxa: {taxa}')
            elif escolha == 4 and loop == 0:
                self.view.Movimentacao()
            loop+= 1