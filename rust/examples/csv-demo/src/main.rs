//use std::{error::Error, io, process};
use std::fs::File;


fn main() {
    let filepath = "planets.csv";
    //println!("{}", filepath);
    let rows = read_file(filepath);
    for row in rows {
        println!("{:?}", row);
    }
}

fn read_file(filepath: &str) -> Vec<csv::StringRecord> {
    let mut rows:Vec<csv::StringRecord> = vec![];
    match File::open(filepath.to_string()) {
        Ok(file) => {
            //let mut content = String::new();
            //file.read_to_string(&mut content).unwrap();
            let mut rdr = csv::Reader::from_reader(file);
            for result in rdr.records() {
                match result {
                    Ok(row) => {
                        rows.push(row.clone());
                        //println!("{:?}", row);
                        //println!("{}", row.len());
                        //println!("{}", &row[0]);
                    },
                    Err(err) => panic!("Error {}", err)
                };
                //let record = result?;
                //println!("{:?}", record);
            }
        },
        Err(error) => panic!("Error opening file {}: {}", filepath, error),
    }

    rows
}
