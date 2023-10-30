fn main() {
    let mut row: (&str, i32, f32);

    row = ("Purple", 300, 3.45);
    println!("{:?}", row);

    row.0 = "Green";
    row.1 = 99;

    println!("{:?}", row);
}
