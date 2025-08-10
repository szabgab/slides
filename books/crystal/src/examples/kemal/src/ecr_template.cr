require "kemal"

get "/" do |env|
  response = ""
  text = env.params.query["text"]?
  if !text.nil?
    response = text
  end
  render "src/views/page.ecr", "src/views/layouts/layout.ecr"
end

Kemal.run
