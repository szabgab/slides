fn main() {
    for number in [5, 10, 0, -1, 3] {
        let fact = factorial(number);
        println!("{number}! is {fact}");
    }
}

fn factorial(n:i64) -> i64 {
    if n == 0 {
        return 1;
    }
    n * factorial(n-1)
}
