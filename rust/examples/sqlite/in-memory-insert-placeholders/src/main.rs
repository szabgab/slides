use sqlite::State;

fn main() {
    let connection = sqlite::open(":memory:").unwrap();
    connection.execute("CREATE TABLE users (name TEXT, age INTEGER, grade INTEGER);").unwrap();

    let mut insert_statement = connection.prepare("INSERT INTO users VALUES (:name, :age, :grade);").unwrap();

    //insert_statement
    match insert_statement.bind_iter::<_, (_, sqlite::Value)>([
        (":name", "Mary".into()),
        (":age", 100.into()),
        (":grade", 99.into()),
    ]) {
        Ok(val) => println!("{:?}", val),
        Err(err) => println!("{}", err),
    }
    let _ = insert_statement.next();

    let _ = insert_statement.reset();
    match insert_statement.bind_iter::<_, (_, sqlite::Value)>([
        (":name", "George".into()),
        (":age", 99.into()),
        (":grade", 65.into()),
    ]) {
        Ok(val) => println!("{:?}", val),
        Err(err) => println!("{}", err),
    }
    let _ = insert_statement.next();



    let query = "SELECT * FROM users";
    let mut statement = connection.prepare(query).unwrap();

    while let Ok(State::Row) = statement.next() {
        println!("name = {}", statement.read::<String, _>("name").unwrap());
        println!("age = {}", statement.read::<i64, _>("age").unwrap());
        println!("grade = {}", statement.read::<i64, _>("grade").unwrap());
    }

}
