from model import Conta, Status, Divida, Banco, engine
from sqlmodel import select, Session, func


def criar_conta(conta: Conta):
    with Session(engine) as session:
        # nao posso ter 2 contas no mesmo banco
        statement = select(Conta).where(conta.agencia == Conta.agencia)
        results = session.exec(statement).all()

        if results:
            print(60 * "#")
            print("-----|ja existe conta nesse banco|-----")
            print(60 * "#")
            return None

        session.add(conta)
        session.commit()

        return conta


# nova_conta = Conta(agencia=Banco.NUBANK, valor=500)
# criar_conta(nova_conta)
def cadastrar_divida(divida: Divida):
    with Session(engine) as session:

        session.add(divida)
        session.commit()

        return divida
# p1= Divida(valor=40.0,descricao='user')
# cadastrar_divida(p1)


def listar_dividas():
    with Session(engine) as session:
        statement = select(Divida)
        results = session.exec(statement).all()

        return results


def valor_total_divida():
    with Session(engine) as session:
        # Selecionando a coluna valor na tabela dívida e fazendo a soma total
        statement = select(func.sum(Divida.valor))

        soma_valores = session.exec(statement).first()
        print(f'VALOR TOTAL DA DÍVIDA É {soma_valores} \n ')

        return soma_valores


def calculo():
    with Session(engine) as session:
        # Seleciona a primeira conta com saldo maior que 0
        statement = select(Conta).where(Conta.valor > 0)
        # Pega a primeira conta com saldo maior que 0
        conta_com_dinheiro = session.exec(statement).first()

        if conta_com_dinheiro:  # Verifica se há uma conta com saldo
            total_conta = conta_com_dinheiro.valor  # Acessa o valor da conta encontrada

            print(
                f"Conta no banco {conta_com_dinheiro.agencia.value} com saldo: R${total_conta:.2f}")

            # Pegando todas as dívidas cadastradas
            total_dividas = valor_total_divida()

            # Calculando se a conta consegue pagar as dívidas
            if total_conta >= total_dividas:
                saldo_restante = total_conta - total_dividas
                print(
                    f"✅ Você pode pagar todas as dívidas! Saldo restante: R${saldo_restante:.2f} \n")
            else:
                print(
                    f"❌ Você não tem saldo suficiente para pagar todas as dívidas! Faltam R${total_dividas - total_conta:.2f}")
        else:
            print("❌ Não há contas com saldo positivo.")
