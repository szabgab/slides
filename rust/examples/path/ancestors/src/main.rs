use std::path::Path;

fn main() {
    let path = Path::new("one/two/three/four.rs");
    println!("{}", path.display());

    for p in path.ancestors() {
        println!("{}", p.display());
    }
}
