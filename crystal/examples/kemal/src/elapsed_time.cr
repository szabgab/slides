require "kemal"

class HTTP::Server::Context
  getter start_time : Time::Span = Time.monotonic
end

get "/" do |env|
  # spend some time
  x = 0
  loop do
    x += 1
    break if x > 10_000_000
  end
  text = "This is some text"
  render "src/views/time.ecr", "src/views/layouts/layout_with_elapsed_time.ecr"
end

Kemal.run
