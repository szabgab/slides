use chrono::{DateTime, Utc, Local};

fn main() {
    let utc: DateTime<Utc> = Utc::now();
    println!("{}", utc);
    println!("{}", utc.timestamp());

    let local: DateTime<Local> = Local::now();
    println!("{}", local);
    println!("{}", local.timestamp());
}
