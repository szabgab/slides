#[derive(Debug)]
//#[allow(dead_code)]
struct Counter {
    current: u32,
}

impl Counter {
    fn new() -> Counter {
        Counter {
            current: 0,
        }
    }
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        self.current += 1;
        Some(self.current)
    }

}

fn main() {
    let cnt = Counter::new();
    println!("{:?}", &cnt);
    for x in cnt {
        println!("{}", x);
        if 10 <= x {
            break;
        }
    }
}


