
from POO.bank_account.classes.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self._contas = []

    def abrir_conta(self, conta):
        self._contas.append(conta)