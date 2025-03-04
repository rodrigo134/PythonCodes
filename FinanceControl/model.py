from enum import Enum
from sqlmodel import SQLModel, Field, create_engine, Relationship


class Status(Enum):
    PAGO = "Pago"
    NÃO_PAGO = "Não pago"


class Banco(Enum):
    NUBANK = "Nubank"
    CAIXA = "Caixa"
    SANTANDER = "Santander"
    BRADESCO = "Bradesco"
    ITAU = "itau"
    SICOOB = "Sicoob"

# ID | VALOR | DESCRIÇÃO | STATUS


class Divida(SQLModel, table=True):
    id: int = Field(primary_key=True)
    valor: float
    descricao: str
    status: Status = Field(Status.NÃO_PAGO)

    def __str__(self):
        return (
            f"Dívida ID: {self.id}\n"
            f"Descrição: {self.descricao}\n"
            f"Status: {self.status.value}\n"
            f"Valor: R$ {self.valor:.2f}"
        )
#  ID| VALOR |AGENCIA
#  1 |  2000 | NUBANK


class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    valor: float = Field(default=0)
    agencia: Banco = Field(default=Banco.NUBANK)


# Nome do arquivo do banco de dados SQLite
sql_name = 'database.db'

# URL de conexão com o banco de dados SQLite
sql_url = f'sqlite:///{sql_name}'

# Criando o engine (conexão com o banco de dados)
engine = create_engine(sql_url)

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if "__main__" == __name__:
    SQLModel.metadata.create_all(engine)
