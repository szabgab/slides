use regex::Regex;
use regex::Captures;

fn main() {
    let text = "The black cat climbed the green tree";
    println!("'{}'", &text);

    let re = Regex::new(r"cat").unwrap();
    let result = re.replace_all(text, "dog");
    println!("'{}'", &result);



    // We can use the captured substring by location
    let text = "abcde";
    println!("'{}'", &text);
    let re = Regex::new(r"(.)(.)").unwrap();
    let result = re.replace_all(text, r"$2$1");
    println!("'{}'", &result);


    // We can use named captured and then the result might be clearer and adding another pair of ()
    // won't impact the code.
    let re = Regex::new(r"(?<first>.)(?<second>.)").unwrap();
    let result = re.replace_all(text, r"$second$first");
    println!("'{}'", &result);


    let text = "12345";
    println!("'{}'", &text);
    let re = Regex::new(r"(.)(.)").unwrap();
    let result = re.replace_all(text, |caps: &Captures| {
        let a: i32 = caps[1].parse().unwrap();
        let b: i32 = caps[2].parse().unwrap();
        format!("{} ", a+b)
    });
    println!("'{}'", &result);
}
