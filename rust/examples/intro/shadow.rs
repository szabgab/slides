fn main() {
    let answer = "42";
    println!("{}", answer);
    // println!("{}", answer + 1);  // cannot add `{integer}` to `&str`

    let answer: i32 = answer.parse().expect("Oh");
    println!("{}", answer);
    println!("{}", answer + 1);
}

