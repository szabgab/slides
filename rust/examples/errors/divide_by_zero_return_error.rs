fn div(a: i32, b: i32) -> Result<i32, &'static str> {
    if b == 0 {
        return Err("Cannot divide by 0");
    }
    Ok(a / b)
}

fn main() {
    for number in [2, 4, 0, 20] {
        let res = div(100, number);
        match res {
            Ok(result) => println!("{result}"),
            Err(err) => println!("{err}"),
        }
    }
}
