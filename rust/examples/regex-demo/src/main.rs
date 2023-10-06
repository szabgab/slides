use regex::Regex;

fn main() {
    let text = "There is the number 23 and another number here: 19".to_string();
    println!("{}", text);

    let re = Regex::new(r"[0-9]+").unwrap();

    let number = match re.captures(&text) {
        Some(value) => value,
        None => {
            println!("No match");
            return
        }
    };
    println!("Number of matches: {}", number.len());
    println!("Full match: '{}'", &number[0]);


    // match the number that comes after colon (:)
    // but the match now includes the : as well
    let re = Regex::new(r": [0-9]+").unwrap();
    let number = match re.captures(&text) {
        Some(value) => value,
        None => {
            println!("No match");
            return
        }
    };
    println!("Full match: '{}'", &number[0]);

    // Use parentheses to capture parts of the string
    let re = Regex::new(r": ([0-9]+)").unwrap();
    let number = match re.captures(&text) {
        Some(value) => value,
        None => {
            println!("No match");
            return
        }
    };
    println!("Full match: '{}'", &number[0]);
    println!("Matched: '{}'", &number[1]);
}
