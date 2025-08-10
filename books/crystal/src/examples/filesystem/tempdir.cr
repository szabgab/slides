require "file_utils"

tempdir = File.tempname
FileUtils.mkdir(tempdir)
original = Dir.current
puts tempdir
FileUtils.cd(tempdir)

File.write("welcome.txt", "Hello World")

FileUtils.cd(original)
FileUtils.rm_rf(tempdir)
