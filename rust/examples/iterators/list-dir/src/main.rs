use std::path::Path;

fn main() {
    let path_from_user = ".";
    let path = Path::new(path_from_user);
    match path.read_dir() {
        Ok(dh) => {  // A ReadDir instance
            for entry in dh {
                println!("{:?}", entry);
            }
        },
        Err(err) => println!("Could not open directory '{}': {}", path_from_user, err),
    }
}

