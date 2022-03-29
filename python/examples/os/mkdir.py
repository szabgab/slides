import os

# create a single directory
path_to_new_dir = 'abc'
os.mkdir(path_to_new_dir)

# create also the parent directories, if needed
path_to_new_dir = 'dir/subdir/subdir'
# os.mkdir(path_to_new_dir) # will fail if 'dir' or 'dir/subdir' does not exist
os.makedirs(path_to_new_dir)


#  remove a file (both)
os.remove(path_to_file)
os.unlink(path_to_file)

# remove single empty directory
os.rmdir(path_to_dir)

# remove directory tree if there are no files in them
os.removedirs(path_to_dir)

# Remove a whole directory structure (subdirs and files)
# Like rm -rf
shutil.rmtree(path_to_dir)

