process = Process.new("ls", ["-l", "-a"],
  output: Process::Redirect::Pipe,
  error: Process::Redirect::Pipe,
)

output = process.output.gets_to_end
error = process.error.gets_to_end

res = process.wait
if res.success?
  puts output
else
  puts error
end
puts res.exit_status # exit code
