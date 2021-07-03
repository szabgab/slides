require "http"

req = HTTP::Request.new("POST",
  "https://code-maven.com/page",
  body: "name=Foo&email=foo@bar.com",
  headers: HTTP::Headers{"Content-Type" => "application/x-www-form-urlencoded"})
p! req
p req.body # IO::Memory
