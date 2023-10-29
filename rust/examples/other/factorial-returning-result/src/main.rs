fn main() {
    let numbers = vec![0, 1, 2, 3, 4, -1];
    for number in numbers {
        let res = factorial(number);
        println!("{}! = {:?}", number, res);
    }
    println!();

    //for number in numbers {
    //    match factorial(number) {
    //        Ok(res) => {
    //            println!("{}! = {}", number, res);
    //        },
    //        Err(err) => {
    //            println!("Error {}", err);
    //        }
    //    }
    //}
}

fn factorial(number: i32) -> Result<i32, &'static str> {
    if number < 0 {
        return Err("Factorial requires a non-negative integer");
    }
    let mut num = 1;
    for n in 1..=number {
        num *= n;
    }
    Ok(num)
}
