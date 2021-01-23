from POO.bank_account.classes.cliente import Cliente

from POO.bank_account.classes.contas import ContaCorrente, ContaPoupanca

from POO.bank_account.classes.banco import Banco

# Criando clientes:

cliente_1 = Cliente('João Luiz', 34)

cliente_2 = Cliente('Carlos Lisboa', 52)

cliente_3 = Cliente('Pedro Alcantara', 18)

# Criando contas:

cp_1 = ContaPoupanca('0001', '638593', 100)

cp_2 = ContaPoupanca('0002', '438527', 0)

cc_1 = ContaCorrente('0236', '040398', 50000, 10000)

cc_2 = ContaCorrente('0236', '040397', 5000, 10000)

cc_3 = ContaCorrente('0002', '040340', 0, 100)

# Atribuindo contas aos respectivos clientes:

cliente_1.abrir_conta(cp_1)

cliente_2.abrir_conta(cc_1)
cliente_2.abrir_conta(cc_3)

cliente_3.abrir_conta(cc_2)
cliente_3.abrir_conta(cp_2)

# Inserindo clientes no banco:

banco = Banco()

banco.inserir_cliente(cliente_1)
banco.inserir_cliente(cliente_2)
banco.inserir_cliente(cliente_3)

banco.listar_clientes()

# Realizando operações financeiras e mostrando os resultados:

banco.depositar('Carlos Lisboa', '0002', '040340', 500)

banco.cliente_especifico('Carlos Lisboa')
banco.cliente_especifico('Pedro Alcantara')

banco.sacar('Pedro Alcantara', '0236', '040398', 'R$6000')

banco.listar_clientes()

banco.sacar('Pedro Alcantara', '0236', '040397', 1000)

banco.cliente_especifico('Pedro Alcantara')

banco.depositar('Pedro Alcantara', '0002', '438527', 10)

banco.cliente_especifico('Pedro Alcantara')

banco.sacar('Pedro Alcantara', '0002', '438527', 50)

cc_1.depositar(100)

cc_1.sacar(100)

cp_2.depositar(200)

banco.listar_clientes()