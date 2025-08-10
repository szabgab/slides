require "option_parser"

verbose = false
destination = "127.0.0.1"

OptionParser.parse do |parser|
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

if verbose
  puts "Verbose mode"
end
puts "Destination: #{destination}"
