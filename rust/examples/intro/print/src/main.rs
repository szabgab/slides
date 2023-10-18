fn main() {
    let fname = "Foo";
    let lname = "Bar";

    println!("{} {}", fname, lname);
    println!("{fname} {lname}");
    print!("{fname} {lname}\n");

    eprintln!("error in {} {}", fname, lname);
    eprint!("error in {} {}\n", fname, lname);

    let full_name = format!("{fname} {lname}");
    println!("{full_name}");
    dbg!(full_name);
}
