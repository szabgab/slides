use std::io;
use std::io::Write;
use std::collections::HashMap;

fn main() {

    let mut age = String::new();
    print!("How old are you? ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut age)
        .expect("Faild to get input");
    let age: f32 = age.trim().parse().unwrap_or_else(|_| panic!("Could not convert '{age}' to floating point number"));

    let mut country = String::new();
    print!("Which country are you in? ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut country)
        .expect("Faild to get input");
    let country = country.trim();

    let age_limit = HashMap::from([
        ("Australia", 18.0),
        ("Austria", 16.0),  // Actually it depends on the type of alcohol
        ("Hungary", 18.0),
        ("Israel", 18.0),
        ("Pakistan", 21.0), // Prohibited for muslims, 21 for others
        ("Paraguay", 20.0),
        ("USA", 21.0),
    ]);

    if age_limit.contains_key(&country) {
        if age_limit[&country] <= age {
            println!("Congratulations, you can legally drink alcohol in {country}.");
        } else {
            println!("Sorry. You are under {}. You cannot legally drink alcohol in {}!", age_limit[country], country);
        }
    } else {
        println!("You typed in '{country}'. Unfortunately we don't have that name in our database");
    }
}
