class Main:
    pass

from Cliente import Cliente
from Conta import Conta

cliente = Cliente("Emanuel", "71983838579")
conta = Conta(cliente.get_nome, 12356)

conta.deposita(100)
conta.extrato()
