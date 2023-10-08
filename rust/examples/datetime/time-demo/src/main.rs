//use time::PrimitiveDateTime as DateTime;
use time::Date;
use time::Month;

//    DateTime::new(
//        Date::from_calendar_date(year, month.try_into().unwrap(), day).unwrap(),
//        Time::from_hms(hour, minute, second).unwrap(),
//    )


fn main() {
    let date = Date::from_calendar_date(2023, Month::June, 18);
    println!("{:?}", date);

    one();
    two();
    three();

    other();
}

fn one() {
    let year = 2023;
    let month = 6;
    let day = 18;
    let date = Date::from_calendar_date(year, month.try_into().unwrap(), day).unwrap();
    print_date(date);
}

fn two() {
    let year = 2023;
    let month = Month::June;
    let day = 18;
    let date = Date::from_calendar_date(year, month, day).unwrap();
    print_date(date);
}

fn three() {
    let year = 2023;
    let month = 6;
    let month: Month = month.try_into().unwrap();
    let day = 18;
    let date = Date::from_calendar_date(year, month, day).unwrap();
    print_date(date);
}

fn other() {
    let date = Date::from_calendar_date(2023, Month::June, 18).unwrap();
    println!("{:?}", date.midnight());
}

fn print_date(date: Date) {
    println!("{:?}", date);
    println!("{}", date.year());
    println!("{}", date.month());
    println!("{}", date.day());
    println!();
}


