use chrono::{DateTime, Utc, TimeZone};

fn main() {
    let ts1 = "2023-09-19T08:00:01Z".parse::<DateTime<Utc>>().unwrap();
    let ts2 = "2023-09-19T08:00:02Z".parse::<DateTime<Utc>>().unwrap();
    println!("{}", ts1 < ts2);

    let dt1 = Utc.with_ymd_and_hms(2023, 9, 19, 8, 0, 1).unwrap();
    println!("{}", ts1 == dt1);
}

