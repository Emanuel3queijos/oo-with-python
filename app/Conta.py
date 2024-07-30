class Conta:
    def __init__(self, titular, numero):
        self._saldo = 0
        self._numero = numero
        self._titular = titular

    def deposita(self, valor):
        if (valor <= 0):
            print("O Valor a ser depositado nao pode ser negativo ou igual a zero")
        else:
            self._saldo += valor

    def extrato(self):
        print("Cliente ", self._titular, "Saldo Atual: ", self._saldo)


    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("saque realizado com sucesso")
        else:
           print("saldo insuficiente")


    @property
    def saldo(self):
     return self._saldo


    @saldo.setter
    def set_saldo(self, saldo):
       if (saldo < 0):
        print("O Saldo nao pode ser negativo")
       else:
           self._saldo = saldo

