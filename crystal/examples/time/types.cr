now = Time.utc
puts typeof(now)
puts now

monotonic = Time.monotonic
puts typeof(monotonic)
puts monotonic

timespan = Time::Span.new(days: 1)
puts typeof(timespan)
puts timespan

