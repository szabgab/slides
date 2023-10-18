fn main() {
    let names = vec!["Foo", "Bar", "Baz"];
    println!("{:?}", names);

    let joined = names.join("");
    println!("{}", joined);

    let csv = names.join(",");
    println!("{}", csv);
}
