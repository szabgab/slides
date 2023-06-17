fn main() {
    let row: (&str, u32, u32, u8) = ("Blue", 300, 500, 3);
    println!("{:?}", row);

    println!("{}", row.0);
    println!("{}", row.1);
    let (name, x, y, z) = row;
    println!("{name} x={x} y={y} z={z}");
}
