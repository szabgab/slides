fn main() {
    let integers = vec![1, 2, 3];
    println!("{:?}", integers);

    let joined = integers.iter().map(|num| format!("{num}")).collect::<Vec<_>>().join(",");
    println!("{}", joined);
    assert_eq!(joined, "1,2,3");
}
