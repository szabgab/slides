require "file_utils"


tmp_dir = xtempdir()
puts tmp_dir
puts tmp_dir + "welcome.txt"
#File.write(tempdir + "welcome.txt", "Hello World")



def xtempdir(cleanup = 1)
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
   
