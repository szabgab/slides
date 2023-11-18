use sqlite::State;

fn main() {
    let connection = sqlite::open(":memory:").unwrap();
    let query = "
        CREATE TABLE users (name TEXT, age INTEGER);

        INSERT INTO users VALUES ('Alice', 42);
        INSERT INTO users VALUES ('Bob', 69);
        ";
    connection.execute(query).unwrap();

    let query = "SELECT * FROM users WHERE age > ?";
    let mut statement = connection.prepare(query).unwrap();
    statement.bind((1, 50)).unwrap();

    while let Ok(State::Row) = statement.next() {
        println!("name = {}", statement.read::<String, _>("name").unwrap());
        println!("age = {}", statement.read::<i64, _>("age").unwrap());
    }

}
