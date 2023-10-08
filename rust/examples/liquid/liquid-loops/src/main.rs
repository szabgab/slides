fn main() {
    let result = render("direct: {% for item in items %}{{item}} {% endfor %}");
    println!("{}", result);
}

fn render(tmpl: &str) -> String {
    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(tmpl).unwrap();

    let globals = liquid::object!({
        "items": vec![2, 3, 4, 5, 6, 7, 8],
    });
    template.render(&globals).unwrap()
}

#[test]
pub fn test_reverse() {
    let result = render("direct: {% for item in items %}{{item}} {% endfor %}");
    assert_eq!(result, "direct: 2 3 4 5 6 7 8 ");

    let result = render("limit: {% for item in items limit: 4 %}{{item}} {% endfor %}");
    assert_eq!(result, "limit: 2 3 4 5 ");

    let result = render("offset: {% for item in items offset: 2 %}{{item}} {% endfor %}");
    assert_eq!(result, "offset: 4 5 6 7 8 ");

    let result = render("offset and limit: {% for item in items offset: 2 limit: 4 %}{{item}} {% endfor %}");
    assert_eq!(result, "offset and limit: 4 5 6 7 ");

    // https://github.com/cobalt-org/liquid-rust/issues/274
    // let result = render("continue: {% for item in items limit: 3 %}{{item}} {% endfor %}new: {% for item in items offset:continue limit: 3 %}{{item}} {% endfor %}");
    // assert_eq!(result, "continue: 2 3 4 new: 5 6 7 ");

    let result = render("reversed: {% for item in items reversed %}{{item}} {% endfor %}");
    assert_eq!(result, "reversed: 8 7 6 5 4 3 2 ");
}
