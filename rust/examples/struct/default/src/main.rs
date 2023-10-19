
#[derive(Debug)]
#[allow(dead_code)]
struct Something {
    name: String,
    number: i32,
}

impl Default for Something {
    fn default() -> Something {
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

    let empty = Something {
        ..Something::default()
    };
    dbg!(empty);

    let with_name = Something {
        name: "Hello".to_string(),
        ..Something::default()
    };
    dbg!(with_name);

    let with_number = Something {
        number: 42,
        ..Something::default()
    };
    dbg!(with_number);

}
