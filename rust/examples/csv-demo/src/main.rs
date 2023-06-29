use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let point = Point { x: 1, y: 2 };

    // Convert the Point to a JSON string.
    let serialized = serde_json::to_string(&point).unwrap();

    // Prints serialized = {"x":1,"y":2}
    println!("serialized = {}", serialized);

    // Convert the JSON string back to a Point.
    let deserialized: Point = serde_json::from_str(&serialized).unwrap();

    // Prints deserialized = Point { x: 1, y: 2 }
    println!("deserialized = {:?}", deserialized);
}


//
//
// //use std::{error::Error, io, process};
// use std::fs::File;
// use serde::Deserialize;
// 
// #[derive(Debug, Deserialize)]
// struct Record {
//     name: String,
//     distance: f32,
//     mass: f32,
// }
// 
// 
// fn main() {
//     let filepath = "planets.csv";
//     //println!("{}", filepath);
//     read_file(filepath);
//     //for row in rows {
//     //    println!("{:?}", row);
//     //}
// }
// 
// fn read_file(filepath: &str) {
//     //let mut rows:Vec<csv::StringRecord> = vec![];
//     match File::open(filepath.to_string()) {
//         Ok(file) => {
//             //let mut content = String::new();
//             //file.read_to_string(&mut content).unwrap();
//             let mut rdr = csv::Reader::from_reader(file);
//             for result in rdr.deserialize() {
//                 match result {
//                     Ok(row) => {
//                         //rows.push(row.clone());
//                         println!("{:?}", row);
//                         //println!("{}", row.len());
//                         //println!("{}", &row[0]);
//                     },
//                     Err(err) => panic!("Error {}", err)
//                 };
//                 //let record = result?;
//                 //println!("{:?}", record);
//             }
//         },
//         Err(error) => panic!("Error opening file {}: {}", filepath, error),
//     }
// 
//     //rows
// }
