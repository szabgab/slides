struct Animal<'a> {
    name: &'a str,
    size: &'a str,
    weight: i32,
}

fn main() {
    let mut animals = vec![
        Animal {name: "elephant", size: "huge", weight: 100},
        Animal {name: "snake",    size: "long", weight: 3},
    ];

    for animal in &animals {
        println!("{} - {} - {}", animal.name, animal.size, animal.weight);
    }

    animals[0].weight += 10;
    for animal in &animals {
        println!("{} - {} - {}", animal.name, animal.size, animal.weight);
    }
}

