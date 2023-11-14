//macro_rules! set_random_number {
//    () => {
//        println!("Hello World!");
//    };
//}


// const RANDOM_CONSTANT: u16 = 42;
// This is not very random, is it?
//
// const RANDOM_CONSTANT: u16 = rand::random();
// cannot call non-const fn `random::<u16>` in constants


extern crate random_constant_macro;
use random_constant_macro::get_random;

//const RANDOM_CONSTANT: u16 = get_random!(u16);
const RANDOM_CONSTANT: i32 = get_random!(i32);

fn main() {
    let random_number: u16 = rand::random();
    println!("random_number: {random_number}");

    println!("random_constant: {RANDOM_CONSTANT}");

}
