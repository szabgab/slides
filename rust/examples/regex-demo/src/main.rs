use regex::Regex;

fn main() {
    let text = "The black cat climbed the green tree";
    println!("{}", text);

    let re = Regex::new(r"cat").unwrap();
    let number = re.captures(&text).unwrap();
    println!("Full match: '{}'", &number[0]);

    // unwrap would panic here so we used the full expression
    let re = Regex::new(r"dog").unwrap();
    match re.captures(&text) {
        Some(value) => println!("Full match: '{}'", &value[0]),
        None => println!("No match"),
    };


    let text = "There is the number 23 and another number here: 19".to_string();
    println!("{}", text);

    let re = Regex::new(r"[0-9]+").unwrap();
    let number = re.captures(&text).unwrap();
    println!("Full match: '{}'", &number[0]);

    let re = Regex::new(r": [0-9]+").unwrap();
    let number = re.captures(&text).unwrap();
    println!("Full match: '{}'", &number[0]);

    let re = Regex::new(r": ([0-9]+)").unwrap();
    let number = re.captures(&text).unwrap();
    println!("Full match: '{}'", &number[0]);
    println!("Matched: '{}'", &number[1]);
}
