
macro_rules! hello_world {
    () => {
        println!("Hello World!");
    };
}

fn main() {
    hello_world!();

    // hello_world!(apple);
    // hello_world!("apple");
    // ^ no rules expected this token in macro call
}
