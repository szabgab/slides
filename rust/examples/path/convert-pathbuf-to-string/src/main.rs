fn main() {
    let cwd = std::env::current_dir().unwrap();
    println!("{:?}", cwd);
    //if cwd == "/home/gabor/work/slides/rust/examples/path/convert-pathbuf-to-string" {
    //    ^^ no implementation for `PathBuf == &str`

    if cwd.clone().into_os_string().into_string().unwrap() == "/home/gabor/work/slides/rust/examples/path/convert-pathbuf-to-string" {
        println!("at home");
    } else {
        println!("somewhere else");
    }
}
