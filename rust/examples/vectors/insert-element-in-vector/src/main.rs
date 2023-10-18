//fn main() {
//    let text = "5678";
//    let rev: Vec<_> = text.chars().rev().collect();
//    //let rev: String = text.chars().rev().collect();
//    //println!("{rev}");
//    println!("{:?}", rev);
//}

fn main() {
    let mut values = vec!["1", "2", "3", "4"];
    println!("{:?}", values);
    values.insert(3, ",");
    println!("{:?}", values);
}
