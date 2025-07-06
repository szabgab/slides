require 'net/http'

url = 'https://httpbin.org/status/500'
uri = URI(url)
# puts(uri)

response = Net::HTTP.get_response(uri)
if response.is_a?(Net::HTTPSuccess)
    #puts "Headers:"
    #puts response.to_hash.inspect
    #puts '------'
    puts response.body
else
    puts response.code
    puts response.msg
end
