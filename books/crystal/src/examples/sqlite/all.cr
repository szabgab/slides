require "sqlite3"
db_file = "data.db"

create_db(db_file)
insert_data(db_file, "Foo", true, 19)

def create_db(db_file)
  if File.exists?(db_file)
    return
  end
  begin
    DB.open "sqlite3://#{db_file}" do |db|
      db.exec "CREATE TABLE information (
            id INTEGER PRIMARY KEY,
            name TEXT,
            isit BOOLEAN,
            number INTEGER
        )"
    end
  rescue err
    puts "Exception #{err}"
  end
end

def insert_data(db_file, name, isit, number)
  args = [name, isit, number]
  begin
    DB.open "sqlite3://#{db_file}" do |db|
      db.exec "INSERT INTO information
                 (name, isit, number)
                 VALUES (?, ?, ?)", args: args
    end
  rescue err
    puts "Exception #{err}"
  end
end

def get_max
  return db.scalar "SELECT max(number) FROM information"
end

def get_data(db_file)
  DB.open "sqlite3://#{db_file}" do |db|
    db.exec "SELECT * FROM information"
  end
rescue err
  puts "Exception #{err}"
end
