use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader, Write};
use std::env;
use std::process::exit;

type Counter = HashMap<String, u32>;
const FILENAME: &str = "counter.csv";


fn main() {
    let name = get_name();
    //println!("{}", name);

    let mut counters: Counter = read_the_csv_file();
    if counters.contains_key(&name) {
        counters.insert(name.clone(), counters[&name] + 1);
    } else {
        counters.insert(name.clone(), 1);
    }
    // the above 5 lines could be replaced with this one:
    //*counters.entry(name.clone()).or_insert(0) += 1;

    println!("{}: {}", &name, counters[&name]);
    save_the_csv_file(counters)
}

/// Get name from command line
fn get_name() -> String {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} NAME", args[0]);
        exit(1);
    }
    args[1].clone()
}

fn read_the_csv_file() -> Counter {
    let mut counters: Counter = HashMap::new();
    match File::open(FILENAME) {
        Ok(file) => {
            let reader = BufReader::new(file);
            for line in reader.lines() {
                let line = line.unwrap();
                let line = line.trim();
                let parts: Vec<&str> = line.split('=').collect();
                let name = parts[0];
                let count: u32 = parts[1].parse().unwrap();
                counters.insert(name.to_string(), count);
            }
        },
        Err(error) => {
            println!("Error opening file {}: {}", FILENAME, error);
        },
    }
    counters
}

fn save_the_csv_file(counters: Counter) {
    let mut file = File::create(FILENAME).unwrap();
    for (name, count) in counters.iter() {
        writeln!(&mut file, "{}={}", name, count).unwrap();
    }
    
}
