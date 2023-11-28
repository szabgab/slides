fn main() {
    for site in [
        "https://rust.code-maven.com".to_string(),
        "https://rust.code-maven.com/".to_string(),
    ] {
        process(url::Url::parse(&site).unwrap());
    }
}

fn process(site: url::Url) {
    fetch(&site);
    fetch(&site.join("page").unwrap());
}

fn fetch(site: &url::Url) {
    println!("Process '{}'", site);
}
