use std::fmt;

struct Animal<'a> {
    name: &'a str,
    size: &'a str,
    weight: i32,
}

impl std::fmt::Debug for Animal<'_> {
    fn fmt(&self, format: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(format, "Animal {{ name: {}, size: {}, weight: {} }}", self.name, self.size, self.weight)
    }
}

fn main() {
    let a = Animal {name: "elephant", size: "huge", weight: 100};
    println!("{:?}", a);
    dbg!(a);
}


