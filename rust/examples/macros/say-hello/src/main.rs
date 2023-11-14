macro_rules! say_hello {
    ($name: expr) => {
        println!("Hello {}!", $name);
    };
}

fn main() {
    say_hello!("Foo");
    say_hello!("Bar");
}
