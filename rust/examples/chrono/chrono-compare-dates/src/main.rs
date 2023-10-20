use chrono::{DateTime, Duration, Utc};

fn main() {
    let now: DateTime<Utc> = Utc::now();
    println!("{}", now);

    let later = now + Duration::seconds(1);
    println!("{}", later);

    println!("later is bigger: {}", now < later);
    println!("later is not smaller: {}", now > later);
    println!("later is not the same as now: {}", now == later);
    println!();
    println!("{:?}", now.cmp(&later));
    println!();

    let now2 = later - Duration::seconds(1);
    println!("{}", now2);
    println!("now is now: {}", now == now2);

}
