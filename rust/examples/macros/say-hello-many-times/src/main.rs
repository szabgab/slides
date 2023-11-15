macro_rules! say_hello {
    ($( $name: expr ),*) => {
        $(
            println!("Hello {}!", $name);
        )*
    };
}

fn main() {
    println!("----");
    say_hello!();
    println!("----");

    say_hello!("Foo", "Bar", "Jane", "Joe");
    // generates code with 4 print statements

    println!("----");
    say_hello!("Rust", "Perl", "Python");
    // generates code with 3 print statements
    println!("----");
}
