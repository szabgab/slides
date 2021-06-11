t0 = Time.monotonic
sleep 1
t1 = Time.monotonic

elapsed = t1-t0
puts elapsed
puts elapsed.seconds
puts elapsed.total_seconds
puts elapsed.total_milliseconds
puts elapsed.microseconds
puts elapsed.total_microseconds
