fn main() {
    let n = 10;
    let fact = recursive_factorial(n);
    println!("Factorial of {n} is {fact}");
    let fact = factorial(n);
    println!("Factorial of {n} is {fact}");
}

fn recursive_factorial(n:i64) -> i64 {
    if n == 0 {
        return 1;
    }
    n * recursive_factorial(n-1)
}

fn factorial(n:i64) -> i64 {
    let mut fact = 1;
    for i in 1..=n {
        fact *= i;
    }
    fact
}
