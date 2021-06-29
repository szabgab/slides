time1 = Time.utc(2016, 2, 15, 10, 20, 30)
time2 = Time.utc(2016, 2, 16, 10, 20, 30)
elapsed = time2 - time1 # Time::Span
puts elapsed.days
puts elapsed.total_seconds
