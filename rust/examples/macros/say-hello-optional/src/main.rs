macro_rules! say_hello {
    () => {
        println!("Hello World!");

        // alternatively we could re-use the macro:
        //say_hello!("World");
    };
    ($name: expr) => {
        println!("Hello {}!", $name);
    };
}

fn main() {
    say_hello!("Foo");
    say_hello!("Bar");
    say_hello!("Foo Bar");

    say_hello!();
}
