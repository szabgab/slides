
filenames = ["README.md", "Other file", "crystal.json"]
filenames.each {|file|
    begin
        result = process(file)
        puts result
    rescue err
        puts "Rescued! #{err.message}"
        puts err.class # File::NotFoundError
    end
}

def process(filename)
    content = File.read(filename)
    return content.size
end