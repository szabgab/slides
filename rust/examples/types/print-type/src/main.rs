fn main() {
    let an_integer = 42;
    print_type(&an_integer);

    let a_float   = 4.2;
    print_type(&a_float);

    let an_str = "Hello";
    print_type(&an_str);

    let a_string = "World".to_string();
    print_type(&a_string);

    let a_vector = vec![3, 4, 5];
    print_type(&a_vector);

    // An iterator
    let readdir = std::path::Path::new(".").read_dir().unwrap();
    print_type(&readdir);
}

fn print_type<T>(_: &T) {
    println!("{:?}", std::any::type_name::<T>());
}


