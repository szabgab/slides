require "option_parser"
# Extract the list of imported files
# Verify that all the files are indeed imported

# Optionally verify that the same file is not imported more than once.

class Options
    class_property verbose = false
end


def main
    get_options()
    md_files = get_md_files(Dir.current)
    if Options.verbose
        puts "MD files:\n"
        md_files.each {|path|
            puts path
        }
    end
    imported_files, errors = get_imported_files(md_files)
    # imported_files.each {|file|
    #     puts file
    # }
    files = get_files(Dir.current)
    # files.each {|name|
    #     puts name
    #}
    imported_files.each {|name|
        if files.includes?(name)
            files.delete name
        else
            puts "ERROR #{name} is imported but does not exist"
            errors = true
        end
    }
    files.each {|name|
        puts "ERROR #{name} is not imported"
        errors = true
    }

    if errors
        exit(1)
    end
end

def get_options
    OptionParser.parse do |parser|
        parser.banner = "Usage: check_slides.cr [arguments]"
        parser.on("-v", "--verbose", "Verbose mode") { Options.verbose = true }
        parser.on("-h", "--help", "Show this help") do
            puts parser
            exit
        end
        parser.invalid_option do |flag|
        STDERR.puts "ERROR: #{flag} is not a valid option."
        STDERR.puts parser
        exit(1)
        end
        parser.missing_option do |flag|
        STDERR.puts "ERROR: #{flag} requires a value"
        STDERR.puts parser
        exit(1)
        end
    end
end


def get_imported_files(md_files)
    imported_files = Set(String).new
    errors = false
    md_files.each{|path|
        lines = File.read_lines(path)
        lines.each {|line|
            match = /^!\[\]\((.*)\)\s*$/.match(line)
            if match
                if ! imported_files.add?(match.[1])
                    puts "WARN #{match.[1]} was imported twice"
                    errors = true
                end
            end
        }
    }
    return imported_files, errors
end


def get_files(root)
    skip = Set{"Dockerfile", "shard.lock", "crystal.json"}
    size = root.size
    files = [] of String
    all_files = Dir.glob("#{root}/**/*")
    all_files.each {|path|
        if ! File.file?(path)
            next
        end
        short_name = path[size+1 ..]
        if short_name.starts_with?("bin/") || short_name.starts_with?("lib/")
            next
        end
        if short_name.ends_with?(".md")
            next
        end
        if skip.any?(short_name)
            next
        end
        files.push(short_name)
    }
    files.push(".ameba.yml")

    return files
end

def get_md_files(root)
    all_md_files = Dir.glob("#{root}/*.md")
    md_files = [] of String

    all_md_files.each {|path|
        # TODO use some filter?
        if path.ends_with?("README.md")
            next
        end
        md_files.push(path)
    }
    return md_files
end

#path = ARGV[0]

#dr = Dir.glob("#{path}/**/*")
#dr.each {|name| puts name}

main()
