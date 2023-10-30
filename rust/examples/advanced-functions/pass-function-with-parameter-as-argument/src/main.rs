
fn main() {
    call(hello);
}

fn hello(text: &str) {
    println!("Hello {}", text);
}

fn call(my_function: fn(text: &str) -> ()) {
    my_function("Foo");

    my_function("Bar");
}


