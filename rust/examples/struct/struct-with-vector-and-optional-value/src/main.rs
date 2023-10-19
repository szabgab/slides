struct Course<'a> {
    name: &'a str,
    grades: Vec<i32>,
    final_grade: Option<i32>,
}

fn main() {
    let mut c = Course { name: "Programming Rust", grades: vec![78, 80], final_grade: None };
    println!("{}", c.name);
    println!("{:?}", c.grades);
    println!("{:?}", c.final_grade);
    // println!("{:?}", c.final_grade.unwrap()); // thread 'main' panicked at 'called `Option::unwrap()` on a `None` value'

    match c.final_grade {
        Some(value) => println!("Final grade is {value}"),
        None => println!("There is no final grade yet"),
    };

    c.grades.push(100);
    c.final_grade = Some(82);
    println!("{:?}", c.grades);
    println!("{:?}", c.final_grade);
    println!("{:?}", c.final_grade.unwrap());

    match c.final_grade {
        Some(value) => println!("Final grade is {value}"),
        None => println!("There is no final grade yet"),
    };
}
