#[derive(PartialEq)]
#[allow(dead_code)]
enum Weekday {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday,
}

fn main() {
    println!("Hello");

    let today = Weekday::Sunday;
    let other_day = Weekday::Monday;
    println!("{:?}", today == other_day);
}

