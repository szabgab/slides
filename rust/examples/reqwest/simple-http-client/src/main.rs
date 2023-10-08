
fn main() {
    let res = match reqwest::blocking::get("https://httpbin.org/ip") {
        Ok(res) => res,
        Err(err) => {
            println!("Error {}", err);
            std::process::exit(1);
        }
    };
    println!("{:?}", res.status());
    println!("{:?}", res);
}
