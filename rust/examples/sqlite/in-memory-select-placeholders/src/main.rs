use sqlite::State;

fn main() {
    let connection = sqlite::open(":memory:").unwrap();
    connection.execute("CREATE TABLE users (name TEXT, age INTEGER, grade INTEGER);").unwrap();
    connection.execute("INSERT INTO users VALUES ('Alice', 42, 80);").unwrap();
    connection.execute("INSERT INTO users VALUES ('Bob', 69, 70);").unwrap();


    //let query = "SELECT * FROM users WHERE age > 50 AND grade > 50";
    let age = 50;
    let grade = 50;
    //let query = "SELECT * FROM users WHERE age > ? AND grade > ?";
    let query = "SELECT * FROM users WHERE age > :age AND grade > :grade";
    let mut statement = connection.prepare(query).unwrap();
    //statement.bind((1, age)).unwrap();
    //statement.bind((2, grade)).unwrap();

    // bind in one step
    //statement.bind::<&[(_, sqlite::Value)]>(&[(1, age.into()), (2, grade.into())]).unwrap();
    // 1 and 2 refer to the order number of the placeholders
    statement.bind::<&[(_, sqlite::Value)]>(&[(":age", age.into()), (":grade", grade.into())]).unwrap();

    //let params = vec![(1, age.into()), (2, grade.into())];
    //statement.bind::<&[(_, sqlite::Value)]>(&params).unwrap();


    while let Ok(State::Row) = statement.next() {
        println!("name = {}", statement.read::<String, _>("name").unwrap());
        println!("age = {}", statement.read::<i64, _>("age").unwrap());
        println!("grade = {}", statement.read::<i64, _>("grade").unwrap());
    }

}
