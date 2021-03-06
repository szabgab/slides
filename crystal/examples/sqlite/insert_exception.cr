require "sqlite3"

db_file = "data.db"
if File.exists?(db_file)
  puts "File #{db_file} already exists. Aborting"
  exit(1)
end

begin
  DB.open "sqlite3://#{db_file}" do |db|
    db.exec "CREATE TABLE contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            UNIQUE (name)
        )"
    res = db.exec "INSERT INTO contacts (name, email) VALUES (?, ?)", "John Doe", "john@example.com"
    puts typeof(res)       # DB::ExecResult
    puts res.rows_affected # 1

    begin
      res = db.exec "INSERT INTO contacts (name, email) VALUES (?, ?)", "John Doe", "john@example.com"
      puts res.rows_affected
    rescue err
      puts "Exception #{err}" # SQLite3::Exception  UNIQUE constraint failed: contacts.name
    end

    puts "contacts:"
    db.query "SELECT id, name, email FROM contacts" do |rs|
      puts "#{rs.column_name(0)} (#{rs.column_name(1)}) (#{rs.column_name(2)})"
      rs.each do
        puts "#{rs.read(Int64)} #{rs.read(String)} (#{rs.read(String)})"
      end
    end
  end
rescue err
  puts "Exception #{err}"
  # The external begin/rescue is needed because of this bug:
  # https://github.com/crystal-lang/crystal-sqlite3/issues/52
end
