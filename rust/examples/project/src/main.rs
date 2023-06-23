pub mod helper;

fn main() {
    println!("main");
    same_file();
    helper::public_in_helper();
    //helper::private_in_helper();
}

fn same_file() {
    println!("same file");
}
