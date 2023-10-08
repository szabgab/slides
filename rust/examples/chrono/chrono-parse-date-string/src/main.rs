use chrono::{DateTime, Utc, TimeZone, NaiveDateTime};

fn main() {
    let ts1 = "2023-09-19T08:00:01Z".parse::<DateTime<Utc>>().unwrap();
    let ts2 = "2023-09-19T08:00:02Z".parse::<DateTime<Utc>>().unwrap();
    println!("{}", ts1 < ts2);

    let dt1 = Utc.with_ymd_and_hms(2023, 9, 19, 8, 0, 1).unwrap();
    println!("{}", ts1 == dt1);

    //let ts3 = DateTime::parse_from_str("2023-09-18", "%Y-%m-%d").unwrap();
    //let ts3 = DateTime::parse_from_str("2023-09-18 01:44:10 ", "%Y-%m-%d %H:%M:%S").unwrap();
    let ts3 = NaiveDateTime::parse_from_str("2023-09-19 08:00:02", "%Y-%m-%d %H:%M:%S").unwrap();
    println!("{}", ts3);

    let ts4 = NaiveDateTime::parse_from_str("2023-09-19 08:00:02 UTC", "%Y-%m-%d %H:%M:%S %Z").unwrap();
    println!("{}", ts4);

    println!("{}", ts3 == ts4);

    let ts5 = DateTime::parse_from_str("2023-09-19 08:00:02 +00:00", "%Y-%m-%d %H:%M:%S %z").unwrap();
    println!("{}", ts5);

    println!("{}", ts3 ==  ts5.naive_utc());

}

