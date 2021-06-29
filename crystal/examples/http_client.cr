require "http/client"

url = "https://httpbin.org/get"
response = HTTP::Client.get(url)
puts response.status_code
puts response.body

# Setting some values in the header
url = "https://httpbin.org/get"
response = HTTP::Client.get(url, headers: HTTP::Headers{"Key" => "Value"})
puts response.status_code
puts response.body
