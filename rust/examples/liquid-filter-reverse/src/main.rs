fn main() {
    let result = render("direct: {{ items }}");
    println!("{}", result);
}

fn render(tmpl: &str) -> String {
    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(tmpl).unwrap();

    let globals = liquid::object!({
        "items": vec![2, 3, 4],
    });
    template.render(&globals).unwrap()
}

#[test]
pub fn test_reverse() {
    let result = render("direct: {{ items }}");
    assert_eq!(result, "direct: 234");

    let result = render("reversed: {{ items | reverse }}");
    assert_eq!(result, "reversed: 432");

    let result = render("direct: {% for item in items %}{{item}} {% endfor %}");
    assert_eq!(result, "direct: 2 3 4 ");

    let result = render("reversed: {% assign ritems = items | reverse %}{% for item in ritems %}{{item}} {% endfor %}");
    assert_eq!(result, "reversed: 4 3 2 ");

    let result = render("reversed: {% for item in items reversed %}{{item}} {% endfor %}");
    assert_eq!(result, "reversed: 4 3 2 ");
}
