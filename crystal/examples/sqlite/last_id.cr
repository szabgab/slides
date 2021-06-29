require "sqlite3"

db_file = "data.db"
if File.exists?(db_file)
  puts "File #{db_file} already exists. Aborting"
  exit(1)
end

DB.open "sqlite3://#{db_file}" do |db|
  db.exec "CREATE TABLE contacts (
        id INTEGER PRIMARY KEY,
        name TEXT
    )"
  res = db.exec "INSERT INTO contacts (name) VALUES (?)", "John Doe"
  puts res.rows_affected
  puts res.last_insert_id

  res = db.exec "INSERT INTO contacts (name) VALUES (?)", "Jane Doe"
  puts res.rows_affected
  puts res.last_index_id

  puts "contacts:"
  db.query "SELECT id, name FROM contacts" do |rs|
    puts "#{rs.column_name(0)} (#{rs.column_name(1)})"
    rs.each do
      puts "#{rs.read(Int64)} #{rs.read(String)}"
    end
  end
end
