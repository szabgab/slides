fn main() {
    ex1();
    ex2();
    ex3();
    ex4();
    ex5();
}

fn ex1() {
    let mut names = vec![];
    names.push("abc");
    names.push("def");
    println!("{:?}", names);
    for name in names {
        println!("{}", name);
    }
    println!("");
}

fn ex2() {
    let mut names = vec!["abc"];
    names.push("def");
    println!("{:?}", names);
    for name in names {
        println!("{}", name);
    }
    println!("");
}

fn ex3() {
    let names = vec!["abc", "def"];
    println!("{:?}", names);
    for name in names {
        println!("{}", name);
    }
    println!("");
}

fn ex4() {
    let mut names = vec![];
    names.push(23);
    // names.push("hello"); // error
    println!("{:?}", names);
    for name in names {
        println!("{}", name);
    }
    println!("");
}

fn ex5() {
    let mut names:Vec<&str> = vec![];
    //names.push(23);  // error
    names.push("hello");
    println!("{:?}", names);
    for name in names {
        println!("{}", name);
    }
    println!("");
}
