
fn main() {
    //hello();
    call(hello);
    call(world);
}

fn hello() {
    println!("Hello");
}

fn world() {
    println!("World");
}


fn call(my_function: fn() -> ()) {
    my_function();
}


