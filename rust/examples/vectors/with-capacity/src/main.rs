fn main() {
    // Create vector of 5 elements initialized to 0
    let vec = vec![0; 5];
    println!("{:?}", vec);

    // Create vector of 5 elements initialized to 42
    let vec = vec![42; 5];
    println!("{:?}", vec);

    // Creata an empty vector that can hold up to 5 elements.
    let mut vec: Vec<i32> = Vec::with_capacity(5);
    vec.resize(3, 19);
    println!("{:?}", vec);
    println!("len:      {:?}", vec.len());
    println!("capacity: {:?}", vec.capacity());
    println!();

    vec.resize(6, 23);
    println!("{:?}", vec);
    println!("len:      {:?}", vec.len());
    println!("capacity: {:?}", vec.capacity());
    println!();

    let mut vec: Vec<i32> = vec![];
    println!("{:?}", vec);
    println!("len:      {:?}", vec.len());
    println!("capacity: {:?}", vec.capacity());
    println!();

    vec.push(42);
    println!("{:?}", vec);
    println!("len:      {:?}", vec.len());
    println!("capacity: {:?}", vec.capacity());
    println!();
}
