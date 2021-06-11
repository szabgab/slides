require "option_parser"

def get_params(arguments)
  verbose = false
  destination = "127.0.0.1"

  OptionParser.parse(arguments) do |parser|
    parser.banner = "Usage: cli_parser.cr [arguments]"
    parser.on("-v", "--verbose", "Verbose mode") { verbose = true }
    parser.on("-d DESTINATION", "--destinaton=DESTINATION", "Where shall we go?") { |name| destination = name }
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
  return {verbose, destination}
end

verbose, destination = get_params([] of String)
puts verbose
puts destination

verbose, destination = get_params(["-v"])
puts verbose
puts destination

verbose, destination = get_params(["-v", "-d", "10.0.0.1"])
puts verbose
puts destination

