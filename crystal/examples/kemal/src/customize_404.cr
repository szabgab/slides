require "kemal"

error 404 do
  "This is a customized 404 page."
end

get "/" do
  "Hello World"
end

Kemal.run
