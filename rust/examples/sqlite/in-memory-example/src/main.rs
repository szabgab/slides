use sqlite::State;

fn main() {
    let connection = sqlite::open(":memory:").unwrap();
    connection.execute("CREATE TABLE users (name TEXT, age INTEGER);").unwrap();
    connection.execute("INSERT INTO users VALUES ('Alice', 42);").unwrap();
    connection.execute("INSERT INTO users VALUES ('Bob', 69);").unwrap();

    let query = "SELECT * FROM users";
    //let query = "SELECT * FROM users WHERE age > 50";
    let mut statement = connection.prepare(query).unwrap();

    while let Ok(State::Row) = statement.next() {
        println!("name = {}", statement.read::<String, _>("name").unwrap());
        println!("age = {}", statement.read::<i64, _>("age").unwrap());
    }

}
