fn main() {
    let animals: Vec<String> = vec![
        "elephant".to_string(),
        "cat".to_string(),
        "snake".to_string(),
        "dog".to_string(),
    ];
    dbg!(&animals);

    let same_animals: Vec<String> = animals.iter().filter(|_animal| true).cloned().collect();
    dbg!(&same_animals);

    let short_animals: Vec<String> = animals.iter().filter(|animal| animal.len() < 4).cloned().collect();
    dbg!(&short_animals);
}
