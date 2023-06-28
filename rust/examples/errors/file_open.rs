use std::fs::File;

fn main() {
    let filename = "rust.json";
    let res = File::open(filename);
    println!("{:?}", res);

    //let filename = "hello.txt";
    //let res = File::open(filename);
    //println!("{:?}", res);

    match res {
        Ok(file) => println!("{:?}", file),
        Err(error) => println!("problem {:?}", error),
    }
}
