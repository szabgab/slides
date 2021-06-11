require "option_parser"

def get_params(arguments)
  OptionParser.parse(arguments) do |parser|
    parser.banner = "Usage: cli_parser.cr [arguments]"
    parser.on("-v", "--verbose", "Verbose mode") { puts "verbose" }
    parser.on("-d DESTINATION", "--destinaton=DESTINATION", "Where shall we go?") { puts "destination" }
    parser.on("-h", "--help", "Show this help") { puts "help" }
  end
  puts "---"
end

get_params([] of String)
get_params(["-v"])
get_params(["-v", "-d", "10.0.0.1"])
get_params(["-d", "10.0.0.1", "-v"])

