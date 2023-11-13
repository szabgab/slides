use std::fs::File;
use std::io::Read;

use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct Point {
    x: i32,
    y: i32,
    text: String,
}

fn main() {
    first_read_file();
}

fn first_read_file() {
    let filename = "data.json";
    match File::open(filename) {
        Ok(mut file) => {
            let mut content = String::new();
            file.read_to_string(&mut content).unwrap();
            let data: serde_json::Value = serde_json::from_str(&content).expect("JSON parsing error");
            dbg!(&data);

            let text = match data.get("text") {
                Some(val) => val.as_str().unwrap(),
                None => panic!("Field text does not exist"),
            };
            println!("{}", text);

            let x = match data.get("x") {
                Some(val) => val.as_i64().unwrap(),
                None => panic!("Field x does not exist"),
            };
            let y = match data.get("y") {
                Some(val) => val.as_i64().unwrap(),
                None => panic!("Field y does not exist"),
            };
            println!("{}", x+y);


            let data: Point = serde_json::from_str(&content).unwrap();
            println!("data = {:?}", data);
            println!("{}", data.x + data.y);
            println!("{}", data.text);
        },
        Err(error) => {
            println!("Error opening file {}: {}", filename, error);
        },
    }
}

