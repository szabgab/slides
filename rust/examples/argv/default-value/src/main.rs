fn main() {
    let argv: Vec<String> = std::env::args().collect();

    let config_file = if argv.len() == 2 {
        &argv[1]
    } else {
        //""
        "config.yaml"
    };

    println!("'{}'", config_file);
}
