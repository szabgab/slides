require "kemal"

get "/" do
  %{
    <a href="/user/foo">/user/foo</a><br>
    <a href="/user/bar">/user/bar</a><br>
    <a href="/user/zorg">/user/zorg</a><br>
  }
end

DATABASE = Set{"foo", "bar"}

get "/user/:fname" do |env|
  fname = env.params.url["fname"]
  if ! DATABASE.includes?(fname)
    halt env, status_code: 404, response: "We don't have this user <b>#{fname}</b>"
  end
  "received fname: #{fname}"
end



Kemal.run
