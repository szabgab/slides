fn main() {
    for n in 1..10 {
        let fibo = fibonacci(n);
        println!("The {n}th Fibonacci number is {fibo}");
    }
}

fn fibonacci(n:i32) -> i32 {
    if n == 0 {
        return 1;
    }
    if n == 1 {
        return 1;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}
