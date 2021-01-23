class Banco:
    def __init__(self):
        self._clientes = {}
        self.saque = None
        self.deposito = None

    def inserir_cliente(self, cliente):
        infos = {}
        dados_bancarios = {}
        numero_contas = 1
        infos['Idade:'] = cliente._idade
        infos['Número de contas:'] = len(cliente._contas)

        for i in cliente._contas:
            dados_bancarios['Tipo de Conta:'] = i.tipodeconta
            dados_bancarios['Agência:'] = i._agencia
            dados_bancarios['Conta:'] = i._conta
            dados_bancarios['Saldo:'] = i._saldo

            if i.tipodeconta == 'ContaCorrente':
                dados_bancarios['Limite:'] = i._limite

            infos[f'{numero_contas}ª conta:'] = dados_bancarios
            dados_bancarios = {}
            numero_contas += 1

        self._clientes[cliente._nome] = infos

    def listar_clientes(self):
        print('Bem vindo ao nossa banco, essas são as informações dos clientes:\n')
        for cliente, dado in self._clientes.items():
            print(cliente, end='\n')

            for chave, valor in dado.items():
                if str(type(valor)) == "<class 'dict'>":
                    print(f'\n{chave}')
                    for chave_especifica, valor_especifico in valor.items():
                        print(chave_especifica, valor_especifico)

                else:
                    print(chave, valor, end='\n')

            print()

    def cliente_especifico(self, nome):
        for cliente, dado in self._clientes.items():
            if str(cliente) == nome:
                print('Informações de cliente específico:\n')
                print(cliente, end='\n')

                for chave, valor in dado.items():
                    if str(type(valor)) == "<class 'dict'>":
                        print(f'\n{chave}')
                        for chave_especifica, valor_especifico in valor.items():
                            print(chave_especifica, valor_especifico)

                    else:
                        print(chave, valor, end='\n')

                print()

    def sacar(self, nome, agencia, conta, value):
        for cliente, dado in self._clientes.items():
            if str(cliente) == nome:
                for chave, valor in dado.items():
                    if str(type(valor)) == "<class 'dict'>":
                        if str(valor['Agência:']) == agencia and str(valor['Conta:']) == conta:
                            if isinstance(value, str):
                                value.replace('R$', '')
                                value = float(value)

                            if str(valor['Tipo de Conta:']) == 'ContaPoupanca':
                                if value > valor['Saldo:']:
                                    return print(f'Saldo insuficiente.\nVocê pode sacar até R$ {valor["Saldo:"]:.2f}')

                                valor['Saldo:'] -= value

                            else:
                                if isinstance(valor['Limite:'], str):
                                    valor['Limite:'].replace('R$', '')
                                    valor['Limite:'] = float(valor['Limite:'])

                                if value > (valor['Saldo:'] + valor['Limite:']):
                                    return print(f'Saldo insuficiente.\nVocê pode sacar até R$ {(valor["Saldo:"] + valor["Limite:"]):.2f}')

                                valor['Saldo:'] -= value

    def depositar(self, nome, agencia, conta, value):
        for cliente, dado in self._clientes.items():
            if str(cliente) == nome:
                for chave, valor in dado.items():
                    if str(type(valor)) == "<class 'dict'>":
                        if str(valor['Agência:']) == agencia and str(valor['Conta:']) == conta:
                            if isinstance(value, str):
                                value.replace('R$', '')
                                value = float(value)

                            valor['Saldo:'] += value