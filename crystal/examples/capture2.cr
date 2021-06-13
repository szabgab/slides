output, error, exit_code = capture("ls", ["-l", "-a"])
if exit_code == 0
    puts output
else
    puts error
end
puts exit_code


def capture(cmd, params)
  stdout = IO::Memory.new
  stderr = IO::Memory.new
  res = Process.new(cmd, params, output: stdout, error: stderr).wait

  return stdout.to_s, stderr.to_s, res.exit_status
end
