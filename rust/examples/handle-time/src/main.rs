//use time::PrimitiveDateTime as DateTime;
use time::Date;

//    DateTime::new(
//        Date::from_calendar_date(year, month.try_into().unwrap(), day).unwrap(),
//        Time::from_hms(hour, minute, second).unwrap(),
//    )


fn main() {
    println!("Hello, world!");
    let year = 2023;
    let month = 6;
    let day = 18;
    let date = Date::from_calendar_date(year, month.try_into().unwrap(), day).unwrap();
    println!("{:?}", date);
}
