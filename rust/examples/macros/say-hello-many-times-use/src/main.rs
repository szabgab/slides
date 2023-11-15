extern crate say_hello_many_times_macro;
use say_hello_many_times_macro::say_hello;

fn main() {
    say_hello!(Joe);
    println!("---");
    say_hello!(cat, dog,   elephant );
}

