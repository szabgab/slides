fn main() {
    for path in [
        "hello.rs",
        ".hello.swp",
        "hello.and.swp",
        ".github",
        ".bashrc",
        "dotless",
    ] {
        let path = std::path::Path::new(path);
        match path.extension() {
            Some(extension)
                => println!("{:15} {:?}", path.display(), extension),
            None => println!("{:15} None", path.display()),
        }
    }
}
