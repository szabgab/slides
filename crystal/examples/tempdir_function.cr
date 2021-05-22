require "file_utils"


tempdir(cleanup: true) do |tmp_dir|
    puts tmp_dir
    path = Path.new(tmp_dir, "welcome.txt")
    File.write(path, "Hello World")
end


def tempdir(cleanup = true)
    tmp_dir = File.tempname
    begin
         FileUtils.mkdir(tmp_dir)
         yield tmp_dir
    ensure
        if cleanup
            FileUtils.rm_rf(tmp_dir)
        end
    end
end

