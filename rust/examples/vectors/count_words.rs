fn main() {
    let text = "mouse cat cat oliphant";
    let parts = text.split_whitespace();
    let mut words:Vec<&str> = vec![];
    let mut count:Vec<i32> = vec![];

    for word in parts {
        let mut found = false;
        for ix in 0..words.len() {
            if words[ix] == word {
                count[ix] += 1;
                found = true;
            }
        }
        if ! found {
            words.push(word);
            count.push(1);
        }
    }

    // report
    for ix in 0..words.len() {
        println!("{}: {}", words[ix], count[ix])
    }
}
