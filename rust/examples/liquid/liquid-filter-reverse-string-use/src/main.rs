use liquid_filter_reverse_string::ReverseStr;

fn main() {

    let template = "reversed: {{text | reversestr}}";
    let text = "Hello World!";

    let result = render(template, text);
    println!("{}", result);
    assert_eq!(result, "reversed: !dlroW olleH");
}


fn render(tmpl: &str, text: &str) -> String {
    let globals = liquid::object!({
        "text": text,
    });

    let template = liquid::ParserBuilder::with_stdlib()
        .filter(ReverseStr)
        .build()
        .unwrap()
        .parse(tmpl).unwrap();

    template.render(&globals).unwrap()
}

