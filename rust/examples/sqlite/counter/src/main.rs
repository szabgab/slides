//use sqlite::{State, Value};
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = "counter.db";

    let exists = std::path::Path::new(filename).exists();

    let connection = sqlite::open(filename).unwrap();
    if !exists {
        let query = "CREATE TABLE counter (name TEXT, cnt INTEGER);";
        connection.execute(query).unwrap();
    }

    if args.len() == 2 {
        let name = &args[1];
        let mut cnt = 0;
        let query = "SELECT * FROM counter WHERE name = :name";
        let mut statement = connection.prepare(query).unwrap();
        statement
            .bind::<&[(_, sqlite::Value)]>(&[(":name", sqlite::Value::String(name.into()))])
            .unwrap();

        let mut insert = true;

        if let Ok(sqlite::State::Row) = statement.next() {
            //println!("{} = {}", name, statement.read::<String, _>("cnt").unwrap());
            cnt = statement.read::<String, _>("cnt").unwrap().parse().unwrap();
            insert = false;
        }

        cnt += 1;

        if insert {
            let mut insert_statement = connection
                .prepare("INSERT INTO counter VALUES (:name, :cnt);")
                .unwrap();

            match insert_statement.bind_iter::<_, (_, sqlite::Value)>([
                (":name", sqlite::Value::String(name.into())),
                (":cnt", sqlite::Value::Integer(cnt)),
            ]) {
                Ok(val) => println!("{:?}", val),
                Err(err) => println!("{}", err),
            }
            let _ = insert_statement.next();
        } else {
            let mut update_statement = connection
                .prepare("UPDATE counter SET cnt = :cnt WHERE name = :name;")
                .unwrap();

            match update_statement.bind_iter::<_, (_, sqlite::Value)>([
                (":cnt", sqlite::Value::Integer(cnt)),
                (":name", sqlite::Value::String(name.into())),
            ]) {
                Ok(val) => println!("{:?}", val),
                Err(err) => println!("{}", err),
            }
            let _ = update_statement.next();
        }
    }

    if args.len() == 1 {
        let query = "SELECT * FROM counter";
        let mut statement = connection.prepare(query).unwrap();

        while let Ok(sqlite::State::Row) = statement.next() {
            println!(
                "{} = {}",
                statement.read::<String, _>("name").unwrap(),
                statement.read::<String, _>("cnt").unwrap()
            );
        }
    }
}
