use std::path::Path;

//trait MyPath {
//}
//
//impl MyPath for Path {
//}
//
//impl MyPath {
//    fn parentn(self: &Path, n: i32) {
//        println!("huh");
//    }
//}


fn main() {
    let path = Path::new("one/two/three/four/five/six.rs");
    println!("{}", path.display());


    match ancestor(&path, 0) {
        Some(val) => println!("ancestor: '{}'", val.display()),
        None => println!("No such ancestor"),
    }
    match ancestor(&path, 1) {
        Some(val) => println!("ancestor: '{}'", val.display()),
        None => println!("No such ancestor"),
    }
    match ancestor(&path, 5) {
        Some(val) => println!("ancestor: '{}'", val.display()),
        None => println!("No such ancestor"),
    }
    match ancestor(&path, 6) {
        Some(val) => println!("ancestor: '{}'", val.display()),
        None => println!("No such ancestor"),
    }
    match ancestor(&path, 7) {
        Some(val) => println!("ancestor: '{}'", val.display()),
        None => println!("No such ancestor"),
    }
}

fn ancestor(mut path: &Path, mut n: i32) -> Option<&Path> {
    while n > 0 {
        match path.parent() {
            Some(value) => path = value,
            None => return None,
        }
        n = n - 1;
    }
    return Some(path);
}

//fn ancestor(path: &Path, n: i32) -> Option<&Path> {
//    if n == 0 {
//        return Some(path);
//    }
//    match path.parent() {
//        Some(value) => ancestor(value, n-1),
//        None => None,
//    }
//}


