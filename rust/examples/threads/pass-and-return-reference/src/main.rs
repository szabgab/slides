fn main() {
    let animals = Vec::from_iter(["mouse", "elephant", "cat", "dog", "giraffe"].map(|animal| animal.to_string()));
    println!("{:?}", animals);

    let handle = std::thread::spawn(move || {
        list_animals(&animals);
        animals
    });
    let animals = handle.join().unwrap();
    println!("{:?}", animals);
}

fn list_animals(animals: &Vec<String>) {
    for animal in animals {
        println!("{}", animal);
    }
}
