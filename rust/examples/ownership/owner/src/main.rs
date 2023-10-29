fn main() {
    ex1();
    ex2();
    ex3();
}

fn ex1() {
    let text = "abc";
    println!("{text}");
    let other = text;
    println!("{text}");
    println!("{other}");
    println!();
}

fn ex2() {
    let text = String::from("abc");
    println!("{text}");
    let other = text;
    //println!("{text}");  // borrow of moved value: `text`
    println!("{other}");
    println!();
}

fn ex3() {
    let text = String::from("abc");
    println!("{text}");
    let other = text.clone();
    println!("{text}");
    println!("{other}");
    println!();
}


