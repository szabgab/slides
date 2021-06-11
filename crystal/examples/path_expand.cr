some_path = "~/work"
path = Path[some_path].expand(home: true)
puts path


puts Path["~/other"].expand(home: true)
puts Path["~/other"].expand()
