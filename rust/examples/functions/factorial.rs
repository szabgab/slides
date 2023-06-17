fn main() {
    for n in 1..10 {
        let fact = factorial(n);
        println!("Factorial of {n} is {fact}");
    }
}

fn factorial(n:i64) -> i64 {
    if n == 0 {
        return 1;
    }
    return n * factorial(n-1);
}
