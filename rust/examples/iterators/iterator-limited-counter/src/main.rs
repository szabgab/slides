#[derive(Debug)]
struct Counter {
    current: u32,
    limit: u32,
}

impl Counter {
    fn new(limit: u32) -> Counter {
        Counter {
            current: 0,
            limit,
        }
    }
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        self.current += 1;
        if self.current > self.limit {
            return None;
        }
        Some(self.current)
    }

}

fn main() {
    let cnt = Counter::new(5);
    println!("{:?}", &cnt);
    for x in cnt {
        println!("{}", x);
    }
}


