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
    println!("----");
    say_hello!("Rust", "Perl", "Python");
    println!("----");
}
