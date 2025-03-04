from enum import Enum
from sqlmodel import SQLModel
from sqlalchemy import create_engine


class Banco(Enum):
    NUBANK = "Nubank"
    CAIXA = "Caixa"
    SANTANDER = "Santander"
    BRADESCO = "Bradesco"
    ITAU = "itau"


class Status(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"


class Conta(SQLModel, table=True):
    ...


sql_name = 'database.db'
sql_url = f'sqlite:///{sql_name}'
engine = create_engine(sql_url, echo=True)


if "__main__" == __name__:
    SQLModel.metadata.create_all(engine)
