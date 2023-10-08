use std::error::Error;
use std::fs::File;

#[derive(Debug, serde::Deserialize)]
struct Record {
    #[serde(rename = "Planet name")]
    name: String,

    #[serde(rename = "Distance (AU)")]
    distance: f32,

    #[serde(rename = "Mass")]
    mass: f32,
}

fn main() {
    let filepath = "planets.csv";
    let result = read_file(filepath);
    match result {
        Ok(rows) => {
            for row in &rows {
                println!("{:?}", row);
            }
            println!("---");
            println!("{}", rows[3].name);
            println!("{}", rows[3].distance);
            println!("{}", rows[3].mass);
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
