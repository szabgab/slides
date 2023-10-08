use regex::Regex;

fn main() {
    let text = "There is the number 23 and another number here: 19";
    println!("{}", text);

    let re = Regex::new(r"[0-9]+").unwrap();

    let mut results = vec![];
    for capture in re.captures_iter(text) {
        println!("{}", &capture[0]);

        results.push(capture[0].to_string());
    }

    println!("{:?}", results);
}
