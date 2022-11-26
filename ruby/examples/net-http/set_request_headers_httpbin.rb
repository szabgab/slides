require 'net/http'

url = 'https://httpbin.org/headers'
uri = URI(url)
# puts(uri)

response = Net::HTTP.get_response(uri, initheader = { "Accept" => "json", "Auth" => "secret" })
if response.is_a?(Net::HTTPSuccess)
    #puts "Headers:"
    #puts response.to_hash.inspect
    #puts '------'
    puts response.body
else
    puts response.code
end

