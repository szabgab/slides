require "kemal"

get "/" do
  form()
end

post "/user/:name" do |env|
  form(env.params.url["name"], env.params.query["email"]?, env.params.body["text"]?)
end

def form(route = "", get = "", post = "")
  %{
    <form method="POST" action="/user/foobar?email=foo@bar.com">
    <input name="text">
    <input type="submit" value="Echo">
    </form>
    <div>route: #{route}</div>
    <div>get: #{get}</div>
    <div>post: #{post}</div>
  }
end

Kemal.run
