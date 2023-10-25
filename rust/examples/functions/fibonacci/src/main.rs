fn main() {
    let n = 15;
    let fibo = recursive_fibonacci(n);
    println!("The {n}th Fibonacci number is {fibo}");
    let fibo = fibonacci(n);
    println!("The {n}th Fibonacci number is {fibo}");
}

fn recursive_fibonacci(n:i32) -> i32 {
    if n == 1 || n == 2 {
        return 1;
    }
    recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
}



fn fibonacci(n:i32) -> i32 {
    let mut fib = vec![1, 1];
    if n == 1 || n == 2 {
        return 1;
    }
    for _ in 3..=n {
        fib.push(fib[fib.len()-1] + fib[fib.len()-2]);
    }
    fib[fib.len()-1]
}
