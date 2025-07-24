require 'net/http'

url = "https://code-maven.com/ruby"
uri = URI(url)
puts(uri)

response = Net::HTTP.get_response(uri)
if response.is_a?(Net::HTTPSuccess)
    puts response.body
else
    puts response.code
end
