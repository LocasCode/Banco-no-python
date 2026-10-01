from BancoView.view import bancoview
from BancoModel.model import Conta
from BancoModel.model import Cliente



class Controller:
    def __init__(self):
        self.model = Conta()
        self.view = bancoview()
        self.cliente = Cliente()
    def iniciar(self):
        self.cliente.cliente = self.view.cliente()
        
        self.view.exibir_mensagem(f'oi, {self.cliente.cliente}. seu saldo é de {self.model.saldo}')
        loop = 0
        while  True:

            self.view.menu()
            escolha = self.view.escolha_banco()
            if escolha is None or escolha >= 5 or escolha <= 0:
                self.view.input_invalido()
            
            elif escolha == 1:
                try:
                    
                    ValorSacado = self.view.quantia()
                    if ValorSacado > 0:
                        resultado = self.model.depositar(ValorSacado)
                    else:
                        self.view.exibir_mensagem('Apenas numeros positivos!')
                except ValueError:
                    return self.view.input_invalido()
                self.view.exibir_mensagem(f'Seu saldo é: R${resultado}')
                self.cliente.movimentaçõesD.append(ValorSacado)
            elif escolha == 2:
                try:
                    ValorSacado = self.view.quantia()
                    resultado = self.model.sacar(ValorSacado)
                    if (resultado != None):
                        self.cliente.movimentaçõesS.append(ValorSacado)
                        self.view.exibir_mensagem(f'Seu saldo é: R${resultado}')
                    else:
                        self.view.exibir_mensagem(f'Dinheiro Insuficiente, acima do limite de saque R$({self.model.limite_saque} ou numero inválido (negativo)')
                except ValueError:
                    return self.view.input_invalido()
            elif escolha == 3:
                
                break
            elif escolha == 4 and loop > 0:
                
                for movimentacoes in self.cliente.movimentaçõesD:
                    self.view.exibir_mensagem(f'depositos: R${movimentacoes}')
                for movimentacoes in self.cliente.movimentaçõesS:
                    self.view.exibir_mensagem(f'saques: R${movimentacoes}')
            elif escolha == 4 and loop == 0:
                self.view.Movimentacao()
                break
            loop+= 1
           