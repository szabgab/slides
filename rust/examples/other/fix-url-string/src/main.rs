fn main() {
    for url in [
        "https://rust.code-maven.com".to_string(),
        "https://rust.code-maven.com/".to_string(),
    ] {
        process_rec(&url);
        process_mut(&url);
        pre_process(&url);
        trim_if_needed(&url);
    }
}

fn trim_if_needed(url: &str) {
    process(url.trim_end_matches('/'));
}

fn process_rec(url: &str) {
    if url.ends_with('/') {
        return process_rec(&url[0..url.len() - 1]);
    }
    process(url);
}

fn process_mut(mut url: &str) {
    if url.ends_with('/') {
        url = &url[0..url.len() - 1];
    }
    process(url);
}

fn pre_process(url: &str) {
    if url.ends_with('/') {
        return process(&url[0..url.len() - 1]);
    }
    process(url)
}

fn process(url: &str) {
    fetch(url);
    fetch(&format!("{}/page", url));
}

fn fetch(url: &str) {
    println!("Process '{}'", url);
}
