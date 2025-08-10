require "kemal"

get "/" do
  %{
    <a href="/user/foo">/user/foo</a><br>
    <a href="/user/bar/bados">/user/bar/bados</a><br>
    <a href="/user/a/b/c">/user/a/b/c</a><br>
    <a href="/path/a/b/c/d">/path/a/b/c/d</a></br>
  }
end

get "/user/:fname" do |env|
  fname = env.params.url["fname"]
  "received fname: #{fname}"
end

get "/user/:fname/:lname" do |env|
  fname = env.params.url["fname"]
  lname = env.params.url["lname"]
  "received fname: #{fname} and lname: #{lname}"
end

get "/path/*all" do |env|
  all = env.params.url["all"]
  "received #{all}"
end

Kemal.run
