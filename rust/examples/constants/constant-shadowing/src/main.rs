fn main() {
    const NAME: &str = "Foo";
    println!("name={NAME}");

    {
        println!("name={NAME}");
        const NAME: &str = "Bar";
        println!("name={NAME}");
    }
    println!("name={NAME}");
}


