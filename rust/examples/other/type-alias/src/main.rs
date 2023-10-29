type Meters = u32;
type Kilograms = u32;

fn main() {
    let m: Meters = 3;
    let k: Kilograms = 4;
    calc(m);
    calc(k);
}

fn calc(y: Meters) {
    dbg!(y);
}


