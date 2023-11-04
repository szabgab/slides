
fn main() {
    let animals = Vec::from_iter(["mouse", "elephant", "cat", "dog", "giraffe"].map(|animal| animal.to_string()));
    println!("{:?}", animals);
    std::thread::scope(|s| {
        s.spawn(|| list_animals(&animals) );
    });

    println!("{:?}", animals);
}

fn list_animals(animals: &Vec<String>) {
    for animal in animals {
        println!("{}", animal);
    }
}
