
from model import Banco, Divida, Status, Conta
from view import *


class UI():
    def start(self):
        while True:
            print('[1]: Criar conta')
            print('[2]: Listar dividas')
            print('[3]: Cadastrar divida')
            print('[4]: Valor total dívidas ')
            print('[5]: Calcular Pagamento')
            print("ESCOLHA A OPÇÃO")
            opcao = int(input())

            print(30*"-")
            if opcao == 1:
                self._criar_conta()
            if opcao == 2:
                self._listar_dividas()
            if opcao == 3:
                self._cadastrar_divida()

            if opcao == 4:
                self._valor_total_divida()

            if opcao == 5:
                self._calculo()

    def _criar_conta(self):
        print("Agencias Disponíveis")
        for banco in Banco:
            print(f'---->{banco.value}<----')
        print("Insira o nome da sua agência: ")
        agencia = input().title()
        saldo = int(input("Insira o seu salario mensal: "))
        conta = Conta(valor=saldo, agencia=Banco(agencia))
        criar_conta(conta)

    def _listar_dividas(self):
        dividas = listar_dividas()
        if not dividas:
            print("Não há dívidas cadastradas.")
        for divida in dividas:
            print(divida, '\n')
            print(30*"-", '\n')

    def _cadastrar_divida(self):
        descricao = input("Insira o nome da divida: ")
        valor = float(input("Valor da divida: "))
        minha_divida = Divida(valor=valor, descricao=descricao)
        cadastrar_divida(minha_divida)

    def _valor_total_divida(self):
        valor_total_divida()

    def _calculo(self):
        calculo()


UI().start()
