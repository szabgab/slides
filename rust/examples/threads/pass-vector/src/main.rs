use std::sync::Arc;

fn main() {
    let animals = Arc::new(Vec::from_iter(["mouse", "elephant", "cat", "dog", "giraffe"].map(|animal| animal.to_string())));
    println!("{:?}", animals);
    let handle = std::thread::spawn({
        let animals = animals.clone();
        move || {
            list_animals(&animals);
        }
    });
    handle.join().unwrap();
     
    println!("{:?}", animals);
}

fn list_animals(animals: &Vec<String>) {
    for animal in animals {
        println!("{}", animal);
    }
}
