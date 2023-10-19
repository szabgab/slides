#[derive(Debug)]
#[allow(dead_code)]
struct Something {
    name: String,
    number: i32,
}

impl Something {
    pub fn qqrq() -> Something {
        Something {
            name: "".to_string(),
            number: 0,
        }
    }
}

fn main() {
    let sg = Something {
        name: "Foo Bar".to_string(),
        number: 42,
    };
    dbg!(sg);

    let new = Something::qqrq();
    dbg!(new);
}
