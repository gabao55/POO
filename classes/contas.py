from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self.tipodeconta = self.__class__.__name__

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @ property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, entrada):
        if isinstance(entrada, str):
            entrada.replace('R$','')
            self._saldo = float(entrada)
            return

        self._saldo = entrada

    def depositar(self, value):
        if isinstance(value, str):
            value.replace('R$','')
            value = float(value)
            self._saldo += value

        self._saldo += value

    @abstractmethod
    def sacar(self, *args, **kwargs):
        pass

class ContaPoupanca(Conta):
    def sacar(self, value):
        if isinstance(value, str):
            value.replace('R$','')
            value = float(value)

        if value > self._saldo:
            return print(f'Saldo insuficiente.\nVocê pode sacar até R$ {self._saldo:.2f}')

        self.saldo -= value

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, value):
        if isinstance(value, str):
            value = float(value[2:])

        if isinstance(self._limite, str):
            self._limite.replace('R$', '')
            self._limite = float(self._limite)

        if value > (self._saldo + self._limite):
            return print(f'Saldo insuficiente.\nVocê pode sacar até R$ {(self._saldo + self._limite):.2f}')

        self.saldo -= value