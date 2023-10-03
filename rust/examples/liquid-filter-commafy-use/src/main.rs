use liquid_filter_commafy::Commafy;

fn main() {
    assert_eq!(
        "2,345",
        render("{{value | commafy}}", liquid::object!({ "value": 2345 }))
    );
    assert_eq!(
        "123,456",
        render("{{value | commafy}}", liquid::object!({ "value": 123456 }))
    );
    assert_eq!(
        "123,456",
        render(
            "{{value | commafy}}",
            liquid::object!({ "value": "123456" })
        )
    );
}

fn render(tmpl: &str, glob: liquid::Object) -> String {
    let template = liquid::ParserBuilder::with_stdlib()
        .filter(Commafy)
        .build()
        .unwrap()
        .parse(tmpl)
        .unwrap();

    template.render(&glob).unwrap()
}
