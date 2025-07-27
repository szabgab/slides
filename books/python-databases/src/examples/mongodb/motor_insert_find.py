import asyncio
import motor.motor_asyncio
import datetime

mary = {
    'name'      : 'Mary',
    'email'     : 'mary@example.com',
    'birthdate' : datetime.datetime.strptime('2002-01-02', '%Y-%m-%d'),
    'student'   : True,
}


async def examples():
    conn_str = 'mongodb://mongodb:27017'
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)

    db = client.demo
    db.people.insert_one(mary)

    results = db.people.find()
    async for person in results:
        print(person)

loop = asyncio.get_event_loop()
loop.run_until_complete(examples())

