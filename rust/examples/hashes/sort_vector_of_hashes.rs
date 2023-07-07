use std::collections::HashMap;

fn main() {
    let joe = HashMap::from([
        ("name", "Joe"),
        ("birthyear", "1993"),
    ]);
    println!("{:?}", joe);

    let mary = HashMap::from([
        ("name", "Mary"),
        ("birthyear", "1994"),
    ]);
    println!("{:?}", mary);

    let lue = HashMap::from([
        ("name", "Lue"),
        ("birthyear", "1992"),
    ]);
    println!("{:?}", lue);


    let mut people:Vec<_> = vec![joe];
    people.push(mary);
    people.push(lue);

    println!("{:?}", people);

    people.sort_by(|a, b| a["birthyear"].cmp(b["birthyear"]));
    println!("{:?}", people);
}
