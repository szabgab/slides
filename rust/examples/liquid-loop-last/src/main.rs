fn main() {
    let result = render("direct: {% for item in items %}{{item}}, {% endfor %}");
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
    let result = render("direct: {% for item in items %}{{item}}, {% endfor %}");
    assert_eq!(result, "direct: 2, 3, 4, 5, 6, 7, 8, ");

    let result = render("direct: {% for item in items %}{{item}}{% if forloop.last %}{% else %}, {% endif %}{% endfor %}");
    assert_eq!(result, "direct: 2, 3, 4, 5, 6, 7, 8");
}
