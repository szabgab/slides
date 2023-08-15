use serde_json::json;
use chrono::{DateTime, Utc};

fn main() {
    let name = "Foo Bar";
    let number = 42;
    let numbers = vec![19, 23];

    let utc: DateTime<Utc> = Utc::now();
    println!("{}", utc);

    let json_str = &json!({
        "name": name,
        "number": number,
        "vector of numbers": numbers,
        "now": utc.timestamp(),
    });
    println!("{}", json_str);
}
