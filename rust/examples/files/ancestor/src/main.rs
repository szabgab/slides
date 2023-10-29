use std::path::Path;

#[allow(clippy::iter_nth_zero)]
fn main() {
    let path = Path::new("one/two/three/four/five/six.rs");


    //match ancestor(&path, 0) {
    //    Some(val) => println!("ancestor: '{}'", val.display()),
    //    None => println!("No such ancestor"),
    //}
    assert_eq!(ancestor(path, 0), Some(Path::new("one/two/three/four/five/six.rs")));
    assert_eq!(ancestor(path, 1), Some(Path::new("one/two/three/four/five")));
    assert_eq!(ancestor(path, 5), Some(Path::new("one")));
    assert_eq!(ancestor(path, 6), Some(Path::new("")));
    assert_eq!(ancestor(path, 7), None);

    assert_eq!(parentn(path, 0), Some(Path::new("one/two/three/four/five/six.rs")));
    assert_eq!(parentn(path, 1), Some(Path::new("one/two/three/four/five")));
    assert_eq!(parentn(path, 5), Some(Path::new("one")));
    assert_eq!(parentn(path, 6), Some(Path::new("")));
    assert_eq!(parentn(path, 7), None);


    assert_eq!(path.ancestors().next(), Some(Path::new("one/two/three/four/five/six.rs")));
    assert_eq!(path.ancestors().nth(0), Some(Path::new("one/two/three/four/five/six.rs")));
    assert_eq!(path.ancestors().nth(1), Some(Path::new("one/two/three/four/five")));
    assert_eq!(path.ancestors().nth(5), Some(Path::new("one")));
    assert_eq!(path.ancestors().nth(6), Some(Path::new("")));
    assert_eq!(path.ancestors().nth(7), None);

}

//fn ancestor(mut path: &Path, mut n: u16) -> Option<&Path> {
//    while n > 0 {
//        match path.parent() {
//            Some(value) => path = value,
//            None => return None,
//        }
//        n = n - 1;
//    }
//    return Some(path);
//}

// improved by Alice Ryhl
fn ancestor(mut path: &Path, n: u16) -> Option<&Path> {
    for _ in 0..n {
        path = path.parent()?
    }
    Some(path)
}


// recursive
fn parentn(path: &Path, n: u16) -> Option<&Path> {
    if n == 0 {
        return Some(path);
    }
    match path.parent() {
        Some(value) => parentn(value, n-1),
        None => None,
    }
}


