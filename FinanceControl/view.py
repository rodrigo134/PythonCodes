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
        print(Conta.valor)
        print(divida.valor)

        return divida
# p1= Divida(valor=40.0,descricao='user')
# cadastrar_divida(p1)


def listar_dividas():
    with Session(engine) as session:
        statement = select(Divida)
        results = session.exec(statement).all()

        if not results:
            print('Sem dívidas')

        for divida in results:
            print(f'{divida}')
            print(30*"-", '\n')


def valor_total_divida():
    with Session(engine) as session:
        statement = select(func.sum(Divida.valor))
        soma_valores = session.exec(statement).first()
        print(f'VALOR TOTAL DA DÍVIDA É {soma_valores} \n ')



