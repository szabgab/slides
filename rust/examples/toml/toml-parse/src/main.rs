use toml::Table;


fn main() {
    parse_toml_pairs();
}

fn parse_toml_pairs() {
    let value = "name = 'bar'\nyear = 2023".parse::<Table>().unwrap();

    assert_eq!(value["name"].as_str(), Some("bar"));
    println!("{}", value["name"].as_str().unwrap());

    assert_eq!(value["year"].as_integer(), Some(2023));
    println!("{}", value["year"].as_integer().unwrap());
}
