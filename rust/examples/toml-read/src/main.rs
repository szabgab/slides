use toml::Table;
use serde::Deserialize;


#[derive(Deserialize)]
#[allow(dead_code)]
struct Config {
   name: String,
   year: u16,
   input: Input,
   output: Output,
   dependencies: Table,
}

#[derive(Deserialize)]
#[allow(dead_code)]
struct Input {
   name: String,
   year: Option<u16>,
}

#[derive(Deserialize)]
#[allow(dead_code)]
struct Output {
   name: String,
   year: Option<u16>,
}


fn main() {
    parse_toml();
}

fn parse_toml() {
    let text = "
name = 'bar'
year = 2023

[input]
name = \"some input\"
year = 1024

[output]
name = 'other thing'

[dependencies]
toml = '0.5'
yaml = '0.9'
serde = { version = '1.0', features = ['derive'] }
    ".to_string();


    let config: Config = toml::from_str(&text).unwrap();

    println!("{}", config.name);
    println!("{}", config.year);
    println!("{}", config.input.name);
    match config.input.year {
        Some(value) => println!("input.year: {}", value),
        None => println!("input.year is missing"),
    };
    println!("{}", config.output.name);

    match config.output.year {
        Some(value) => println!("output.year: {}", value),
        None => println!("output.year is missing"),
    };

    //println!("{}", config.dependencies);
    for (k, v) in config.dependencies.iter() {
        println!("{} -> {}", k, v);
    }

    println!("{}", config.dependencies["serde"]["features"][0]);
    println!("{}", config.dependencies["serde"]["version"]);
}

