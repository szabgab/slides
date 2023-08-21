
#[derive(Debug)]
#[allow(dead_code)]
struct Something {
    name: String,
    input: Input,
}

#[derive(Debug)]
#[allow(dead_code)]
struct Input {
    name: String,
}


impl Something {
    pub fn new() -> Something {
        Something {
            name: "".to_string(),
            input: Input::new(),
        }
    }
}

impl Input {
    pub fn new() -> Input {
        Input {
            name: "".to_string(),
        }
    }
}


impl Default for Something {
    fn default() -> Something {
        Something {
            name: "".to_string(),
            input: Input {
                ..Input::default()
            },
        }
    }
}

impl Default for Input {
    fn default() -> Input {
        Input {
            name: "".to_string(),
        }
    }
}

fn main() {
    let sg = Something {
        name: "Foo Bar".to_string(),
        input: Input { name: "input text".to_string() },
    };
    dbg!(sg);

    let new = Something::new();
    dbg!(new);

    let empty = Something {
        ..Something::default()
    };
    dbg!(empty);


    let with_name = Something {
        name: "Hello".to_string(),
        ..Something::default()
    };
    dbg!(with_name);

}
