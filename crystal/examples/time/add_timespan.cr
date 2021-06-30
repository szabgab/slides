now = Time.utc
tomorrow = now + Time::Span.new(days: 1)
puts now
puts tomorrow

puts now + 1.days
puts now + 24.hours
puts now + 1440.minutes
puts now + 86_400.seconds
