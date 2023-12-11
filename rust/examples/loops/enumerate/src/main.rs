fn main() {
    let animals = vec!["cat", "snake", "camel"];
    for animal in &animals {
        println!("{animal}");
    }
    println!();

    #[allow(clippy::needless_range_loop)]
    for ix in 0..animals.len() {
        println!("{ix} {}", animals[ix]);
    }
    println!();

    for (ix, animal) in animals.iter().enumerate() {
        println!("{ix} {animal}");
    }
}
