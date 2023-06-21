fn main() {
    let answer = "42";
    println!("{}", answer);

    let answer: i32 = answer.parse().expect("Oh");
    println!("{}", answer);
    println!("{}", answer + 1);
}

