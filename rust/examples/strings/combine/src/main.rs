fn main() {
    let fname = "Foo".to_string();
    let lname = "Bar".to_string();
    println!("{fname}");
    println!("{lname}");

    let res = combine(&fname, &lname);

    println!("Combined name {res}");
    println!("{fname}");
    println!("{lname}");
}

fn combine(fname: &str, lname: &str) -> String {
    //format!("{fname} {lname}")
    fname.to_string() + " " + lname
}

