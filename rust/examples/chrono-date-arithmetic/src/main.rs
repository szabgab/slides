use chrono::{DateTime, Duration, Utc};

fn main() {
    let now: DateTime<Utc> = Utc::now();
    println!("{}", now);

    let tomorrow = now + Duration::days(1);
    println!("{}", tomorrow);

    let yesterday = now - Duration::days(1);
    println!("{}", yesterday);


    let two_hours_later = now + Duration::hours(2);
    println!("{}", two_hours_later);
}
