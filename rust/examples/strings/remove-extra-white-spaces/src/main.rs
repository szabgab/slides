fn main() {
    let text = "   Some      white \n  \n    \n spaces   \ntext \t \n with tabs   \n";
    println!("'{}'", text);

    let short = text
        .replace(['\n', '\t'], " ")
        .trim()
        .split(' ')
        .filter(|short| !short.is_empty())
        .collect::<Vec<_>>()
        .join(" ");
    println!("'{}'", short);

    let other = text
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ");
    println!("'{}'", other);
}
