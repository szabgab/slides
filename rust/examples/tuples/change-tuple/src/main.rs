fn main() {
    let mut row = ("Blue", 300, 3.67);
    println!("{:?}", row);
    row.0 = "Green";

    row.1 = 99;

    println!("{:?}", row);
}
