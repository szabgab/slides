fn main() {
    let text = "Some text";
    let animals = vec!["cat", "dog", "snake"];
    println!("{}", text.len());
    println!("{}", animals.len());
    assert_eq!(text.len(), 9);
    assert_eq!(animals.len(), 3);

    let template = "text: {{ text.size }} animals: {{ animals.size }}. The string is {% if text.size > 10 %}long{% else %}short{% endif %}.";

    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(template)
        .unwrap();

    let globals = liquid::object!({
        "text": text,
        "animals": animals,
    });
    let output = template.render(&globals).unwrap();

    println!("{}", output);
    assert_eq!(output, "text: 9 animals: 3. The string is short.");
}
