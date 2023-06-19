use std::{error::Error, io, process};
//use std::fs::File;


fn main() {
    let filepath = "planets.csv";
    if let Err(err) = example(filepath) {
        println!("error running example: {}", err);
        process::exit(1);
    }
}

//fn read_file(filepath: &str) {
//    match File::open(filepath.to_string()) {
//        Ok(mut file) => {
//            //let mut content = String::new();
//            //file.read_to_string(&mut content).unwrap();
//
//            let mut rdr = csv::Reader::from_reader(file);
//            for result in rdr.records() {
//                let record = result?;
//                println!("{:?}", record);
//            }
//        },
//        Err(error) => {
//            println!("Error opening file {}: {}", filepath, error);
//        },
//    }
//}

fn example(filepath: &str) -> Result<(), Box<dyn Error>> {
    // Build the CSV reader and iterate over each record.
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.records() {
        // The iterator yields Result<StringRecord, Error>, so we check the
        // error here.
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

