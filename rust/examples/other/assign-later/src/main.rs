fn main() {
    let r;

    {
        r = "one";
    }
    // r = "two"; // cannot assign twice to immutable variable `r`

    println!("r: {}", r);
}


