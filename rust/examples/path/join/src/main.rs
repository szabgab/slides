use std::path::Path;

fn main() {
    let path = Path::new("/home/foo");
    println!("{}", path.display());

    let child = path.join("work");
    println!("{}", child.display());

    let grand_child = child.join("slides");
    println!("{}", grand_child.display());

    let rel_path = Path::new("osdc/project");
    let other = path.join(rel_path);
    println!("{}", other.display());
}
