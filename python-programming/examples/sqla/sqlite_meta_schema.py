from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey


def get_meta():
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
    return metadata
