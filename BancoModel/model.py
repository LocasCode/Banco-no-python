from datetime import datetime


class Cliente:
     def __init__(self, cliente = ''):
          self.cliente  = cliente
          
class Conta:

    def __init__(self, saldo=0, limite_saque=1000):
        self.saldo = saldo
        self.limite_saque = limite_saque
        self.movimentacoesD = []
        self.movimentacoesS = []
        

    def depositar(self, valor):
            if valor > 0 and valor <= self.limite_saque:
                self.saldo += valor
                horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                self.movimentacoesD.append((valor, horario))
                return self.saldo 
            return self.saldo 
    
    def porcentagem(self, valor, porcentagem):    
         return valor * (porcentagem/100)
    
    def sacar(self, valor):
        taxa = self.porcentagem(valor, 5)
        valor_total = valor + taxa
        
        if self.saldo >= valor_total and valor <= self.limite_saque and valor > 0:
            self.saldo -= valor_total 
            horario = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.movimentacoesS.append((valor, horario, valor_total))
            return self.saldo
        return None