use chrono::prelude::*;

fn main() {
    let utc: DateTime<Utc> = Utc::now();
    println!("{}", utc);

    let local: DateTime<Local> = Local::now();
    println!("{}", local);
}
