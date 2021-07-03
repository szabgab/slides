require "kemal"

get "/" do
  form("")
end

post "/" do |env|
  response = ""
  text = env.params.body["text"]?
  if !text.nil?
    response = "You typed in <b>#{text}</b>"
  end
  form(response)
end

def form(response)
  %{
    <form method="POST" action="/">
    <input name="text">
    <input type="submit" value="Echo">
    </form>
    #{response}
  }
end

Kemal.run
