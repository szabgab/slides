use std::error::Error;
use std::fs::File;
use std::collections::HashMap;

type Record = HashMap<String, String>;

fn main() {
    let filepath = "planets.csv";
    let result = read_file(filepath);
    match result {
        Ok(rows) => {
            for row in &rows {
                println!("{:?}", row);
                println!("{}", row["Planet name"]);
            }
            println!("---");
            println!("{}", rows[3]["Planet name"]);
        },
        Err(err) => panic!("Error: {}", err)
    }
}

fn read_file(filepath: &str) -> Result<Vec<Record>, Box<dyn Error>> {
    let mut records:Vec<Record> = vec![];
    match File::open(filepath) {
        Ok(file) => {
            let mut rdr = csv::Reader::from_reader(file);
            for result in rdr.deserialize() {
                let record: Record = result?;
                records.push(record);
            }
        },
        Err(error) => panic!("Error opening file {}: {}", filepath, error),
    }
    Ok(records)
}
