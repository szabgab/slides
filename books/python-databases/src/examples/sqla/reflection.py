from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey

metadata = MetaData()

node_table = Table('node', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(100), unique=True)
                   )

interface_table = Table('interface', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('node_id', Integer, ForeignKey('node.id'), nullable=False),
                   Column('ipv4', String(14), unique=True),
                   Column('ipv6', String(80), unique=True),
                   )

connection_table = Table('connection', metadata,
                    Column('a', Integer, ForeignKey('interface.id'), nullable=False),
                    Column('b', Integer, ForeignKey('interface.id'), nullable=False)
                         )

engine = create_engine('sqlite://', echo=True)
metadata.create_all(engine)


m2 = MetaData()
m2_node_table = Table('node', m2, autoload=True, autoload_with=engine)
m2_interface_table = Table('interface', m2, autoload=True, autoload_with=engine)
print(m2_node_table.columns)
print(m2_interface_table.columns)
print(m2_node_table.__repr__())

from sqlalchemy import inspect

inspector = inspect(engine)
inspector.get_columns('address')
inspector.get_foreign_keys('address')

