require "kemal"

get "/" do |env|
  response = ""
  text = env.params.query["text"]?
  if !text.nil?
    response = "You typed in <b>#{text}</b>"
  end
  %{
    <form method="GET" action="/">
    <input name="text">
    <input type="submit" value="Echo">
    </form>
    #{response}
  }
end

Kemal.run
