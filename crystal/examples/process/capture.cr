output, error, exit_code = capture("ls", ["-l", "-a"])
if exit_code == 0
  puts output
else
  puts error
end
puts exit_code

def capture(cmd, params)
  process = Process.new(cmd, params,
    output: Process::Redirect::Pipe,
    error: Process::Redirect::Pipe,
  )

  output = process.output.gets_to_end
  error = process.error.gets_to_end

  res = process.wait

  return output, error, res.exit_status
end
