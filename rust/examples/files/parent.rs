use std::path::Path;

fn main() {
    let path = Path::new("one/two/three/four.rs");
    println!("{}", path.display());

    println!("{}", path.parent().unwrap().display());

    match Path::new("/a/b").parent() {
        Some(val) => println!("ok {}", val.display()),
        None => println!("No parent"),
    }

    match Path::new("/a").parent() {
        Some(val) => println!("ok {}", val.display()),
        None => println!("No parent"),
    }

    match Path::new("/").parent() {
        Some(val) => println!("ok {}", val.display()),
        None => println!("No parent"),
    }

    match Path::new("").parent() {
        Some(val) => println!("ok {}", val.display()),
        None => println!("No parent"),
    }


}
