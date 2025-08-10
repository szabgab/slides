require "sqlite3"

# Based on the example in the documentation
db_file = "data.db"
if File.exists?(db_file)
  puts "File #{db_file} already exists. Aborting"
  exit(1)
end
DB.open "sqlite3://#{db_file}" do |db|
  db.exec "CREATE TABLE contacts (name TEXT, age INTEGER)"
  db.exec "INSERT INTO contacts VALUES (?, ?)", "John Doe", 30

  args = [] of DB::Any
  args << "Sarah"
  args << 33
  db.exec "INSERT INTO contacts VALUES (?, ?)", args: args

  puts "max age:"
  puts db.scalar "SELECT max(age) FROM contacts" # => 33

  puts "contacts:"
  db.query "SELECT name, age FROM contacts ORDER BY age DESC" do |rs|
    puts "#{rs.column_name(0)} (#{rs.column_name(1)})"
    # => name (age)
    rs.each do
      puts "#{rs.read(String)} (#{rs.read(Int32)})"
      # => Sarah (33)
      # => John Doe (30)
    end
  end
end
