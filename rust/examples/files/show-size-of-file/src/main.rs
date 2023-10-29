fn main() {
    let path = "du.rs";
    let meta = match std::fs::metadata(path) {
        Ok(val) => val,
        Err(_) => panic!("error"),
    };
    dbg!(meta.len());
}
