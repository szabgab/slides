require 'net/http'

url = 'https://httpbin.org/post'
uri = URI(url)

response = Net::HTTP.post_form(uri, {
   "name" => "Foo Bar",
   "height" => 175,
  },
)
if response.is_a?(Net::HTTPSuccess)
    puts response.body
else
    puts response.code
end
