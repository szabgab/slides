require "sqlite3"

DB.open "sqlite3://%3Amemory%3A" do |db|
    db.exec "CREATE TABLE data (
        id INTEGER PRIMARY KEY,
        name TEXT,
        yesno BOOLEAN,
        number INTEGER,
        start DATETIME
    )"
    db.exec "INSERT INTO data (name, yesno, number, start) VALUES (?, ?, ?, ?)",
        "Foo", true, 42, Time.utc
    name = db.scalar "SELECT name FROM data"
    puts name
    puts typeof(name)
    puts name.to_s + " and Bar"

    number = db.scalar "SELECT number FROM data"
    puts number
    puts typeof(number)
    puts number.to_s.to_i + 1

    db.exec "INSERT INTO data (name, yesno, number, start) VALUES (?, ?, ?, ?)",
        "Bar", false, 23, Time.utc
    name = db.scalar "SELECT name FROM data"
    puts name

    count = db.scalar "SELECT COUNT(*) FROM data"
    puts count
    puts typeof(count)

end
