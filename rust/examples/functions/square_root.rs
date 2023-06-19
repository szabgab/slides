fn main() {
    println!("{}", square_root(4.0));
    println!("{}", square_root(-1.0));
}

fn square_root(number: f64) -> f64 {
    match number.sqrt() {
        Ok(res) => {
            res
        },
        Err(_) => {
            println!("err");
        },
    }
}
