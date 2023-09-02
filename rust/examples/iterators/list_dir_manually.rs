use std::path::Path;

fn main() {
    let path_from_user = ".";
    let path = Path::new(path_from_user);
    match path.read_dir() {
        Ok(mut dh) => {  // A ReadDir instance
            loop {
                let entry = dh.next();
                match entry {
                    Some(value) => println!("{:?}", value),
                    None => break,
                }
            }
        },
        Err(err) => println!("Could not open directory '{}': {}", path_from_user, err),
    }
}

