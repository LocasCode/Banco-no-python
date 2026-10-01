class Cliente:
     def __init__(self, cliente = ''):
          self.cliente  = cliente
          self.movimentaçõesD = []
          self.movimentaçõesS = []
class Conta:

    def __init__(self, saldo=0, limite_saque=1000):
        self.saldo = saldo
        self.limite_saque = limite_saque
        
        

    def depositar(self, valor):
            if valor > 0:
                self.saldo += valor
                return self.saldo 
            return self.saldo    
    def porcentagem(self, valor, porcentagem):    
         return valor * (porcentagem/100)
    def sacar(self, valor):
        taxa = self.porcentagem(valor, 5)
        valor_total = valor + taxa
        
        if self.saldo >= valor_total and valor <= self.limite_saque and valor > 0:
            self.saldo -= valor_total 
            return self.saldo
        return None
    
