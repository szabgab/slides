
use std::collections::VecDeque;

fn main() {

    let mut doctor = VecDeque::new();
    println!("len: {} capacity: {} empty:  {}", doctor.len(), doctor.capacity(), doctor.is_empty());

    doctor.push_back("cat".to_string());
    println!("len: {} capacity: {} empty:  {}", doctor.len(), doctor.capacity(), doctor.is_empty());

    doctor.push_back("dog".to_string());
    doctor.push_back("rat".to_string());
    doctor.push_back("squirrel".to_string());
    doctor.push_back("snake".to_string());
    println!("len: {} capacity: {} empty:  {}", doctor.len(), doctor.capacity(), doctor.is_empty());

    println!("{:?}", doctor); // I can print the whole queue, but there is probably no point for that

    let next = doctor.pop_front();
    println!("{}", next.unwrap());
    println!("len: {} capacity: {} empty:  {}", doctor.len(), doctor.capacity(), doctor.is_empty());

}
