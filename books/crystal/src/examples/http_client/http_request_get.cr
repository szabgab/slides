require "http"

req = HTTP::Request.new("GET", "https://code-maven.com/page?name=Foo&email=foo@bar.com")
p! req
p req.resource
p req.query_params
p req.body
