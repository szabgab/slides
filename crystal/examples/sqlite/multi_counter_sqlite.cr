require "sqlite3"

db_file = "counter.db"
if ! File.exists?(db_file)
    DB.open "sqlite3://#{db_file}" do |db|
        db.exec "CREATE TABLE counters (name TEXT, count INTEGER, UNIQUE(name))"
    end
end

DB.open "sqlite3://#{db_file}" do |db|
    if ARGV.size == 1
        name = ARGV[0]
        count = 0
        db.query "SELECT count FROM counters WHERE name=?", name do |rs|
            rs.each do
                count = rs.read(Int32)
            end
        end

        count += 1
        puts count

        if count == 1
            db.exec "INSERT INTO counters VALUES (?, ?)", name, count
        else
            db.exec "UPDATE counters SET count=? WHERE name=?", count, name
        end
    else
        db.query "SELECT name, count FROM counters ORDER BY name DESC" do |rs|
            puts "#{rs.column_name(0)} (#{rs.column_name(1)})"
            rs.each do
              puts "#{rs.read(String)} (#{rs.read(Int32)})"
            end
        end
    end
end
