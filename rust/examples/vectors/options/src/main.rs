#[allow(clippy::needless_range_loop)]
#[allow(clippy::nonminimal_bool)]
fn main() {
    let numbers_real: Vec<Option<i32>> = vec![Some(3),  None, None,     Some(7), Some(9)];
    println!("{:?}", numbers_real);

    let numbers_ref: Vec<Option<&i32>> = vec![Some(&3), None, Some(&5), None,    Some(&9)];
    println!("{:?}", numbers_ref);
    println!();

    for i in 0..numbers_real.len() {
        println!("{:?}", numbers_real[i]);
        println!("{:?}", numbers_ref[i]);
    }
    println!();

    for i in 0..numbers_real.len() {
        if !numbers_real[i].is_none() {
            println!("{}", numbers_real[i].unwrap());
        }
    }
    println!();

    for i in 0..numbers_real.len() {
        if !numbers_ref[i].is_none() && !numbers_real[i].is_none() {
            println!("{:?}", &numbers_real[i].unwrap() == numbers_ref[i].unwrap());
        }
    }
}
