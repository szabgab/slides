require "uri"

url = "https://github.com:443/szabgab/crystal-mine.cr?name=Foo"
uri = URI.parse url
puts uri.scheme
puts uri.host
puts uri.port
puts uri.path
puts uri.query
