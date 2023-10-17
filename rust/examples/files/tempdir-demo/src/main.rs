use std::io::{self, Write};
use std::fs::File;
use tempdir::TempDir;


fn main() {
    match write_temp_folder_with_files() {
        Ok(()) => println!("ok"),
        Err(err) => println!("Error {err}"),
    }
}

fn write_temp_folder_with_files() -> io::Result<()> {
    let temp_dir = TempDir::new("demo")?;
    let file_path = temp_dir.path().join("foo.txt");
    println!("{:?}", file_path);

    let mut fh = File::create(file_path)?;
    fh.write_all(b"Hello, world!")?;
    fh.sync_all()?;
    temp_dir.close()?;

    Ok(())
}

