fn main() {

    let x = 12345i16;
    let y = 2345678i32;
    //println!("{}", x as i64 + y as i64);
    let z = any_number(x);
    println!("{}", z);
    println!("{}", any_number(y));
    println!("{}", any_number(5i8));
    //println!("{}", any_number(5i64));
    println!("{}", any_number(5.1));
}

//fn any_number<Integer: Into<i64> +  Copy + std::fmt::Debug + std::fmt::Display>(num: Integer) -> i64 {
//    //println!("{:?}", num);
//    num.into()
//}

//fn any_number<Integer: Into<i32> +  Copy + std::fmt::Debug + std::fmt::Display>(num: Integer) -> i32 {
//    //println!("{:?}", num);
//    num.into()
//}


fn any_number<Integer: Into<f64> +  Copy + std::fmt::Debug + std::fmt::Display>(num: Integer) -> f64 {
    //println!("{:?}", num);
    num.into()
}
