process = Process.new("ls", ["-l", "-a"],
    output: Process::Redirect::Pipe,
    error: Process::Redirect::Pipe,
    )

output = process.output.gets_to_end
error  = process.error.gets_to_end
if process.wait.success?
    puts output
else
    puts error
end
