struct Course {
    name: String,
}

fn main() {
    let courses :Vec<Course> = vec![
        Course { name: "Programming Rust".to_string() },
        Course { name: "Git".to_string() },
    ];
    for course in &courses {
        println!("{}", course.name);
    }

    let courses:Vec<Course> = courses.into_iter().map(|mut course| { course.name.push_str(" and more"); course }).collect();

    for course in &courses {
        println!("{}", course.name);
    }

}
