from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

metadata = MetaData()
user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(100), unique=True),
                   Column('balance', Integer, nullable=False)
                   )
print(user_table.name)
print(user_table.c.name)
print(user_table.c.id)

print(user_table.c)
print(user_table.columns)  # A bit like a Python dictionary, but it is an associative array



from sqlalchemy import create_engine
engine = create_engine('sqlite://')
metadata.create_all(engine)

from sqlalchemy import ForeignKey

address_table = Table('address', metadata,
                Column('id', Integer, primary_key=True),
                Column('stree', String(100)),
                Column('user_id', Integer, ForeignKey('user.id'))
                )
address_table.create(engine)

from sqlalchemy import Unicode, UnicodeText, ForeignKeyConstraint, DateTime

story_table = Table('story', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('version', Integer, primary_key=True),
                    Column('headline', Unicode(100), nullable=False),
                    Column('body', UnicodeText)
                    )
published_table = Table('published', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('timestamp', DateTime, nullable=False),
                    Column('story_id', Integer, nullable=False),
                    Column('version', Integer, nullable=False),
                    ForeignKeyConstraint(
                        ['story_id', 'version_id'],
                        ['story.story_id', 'story.version_id']
                    )
                )


conn.execute(user_table.insert(), [
    {'username': 'Jack', 'fullname': 'Jack Burger'},
    {'username': 'Jane', 'fullname': 'Jane Doe'}
])

from sqlalchemy import select
select_stmt = select([user_table.c.username, user_table.c.fullname]).where(user_table.c.username == 'ed')
result = conn.execute(select_stmt)
for row in result:
    print(row)

select_stmt = select([user_table])
conn.execute(select_stmt).fetchall()

select_stmt = select([user_table]).where(
    or_(
        user_table.c.username == 'ed',
        user_table.c.usernane == 'wendy'
    )
)

joined_obj = user_table.join(address_table, user_table.c.id = address_table.c.user_id)
