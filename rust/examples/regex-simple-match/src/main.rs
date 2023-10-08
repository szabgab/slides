use regex::Regex;

fn main() {
    let text = "The black cat climbed the green tree";
    println!("{}", text);

    let re = Regex::new(r"cat").unwrap();
    match re.captures(text) {
        Some(value) => println!("Full match: '{}'", &value[0]),
        None => println!("No match"),
    };


    let re = Regex::new(r"dog").unwrap();
    match re.captures(text) {
        Some(value) => println!("Full match: '{}'", &value[0]),
        None => println!("No match"),
    };
}
