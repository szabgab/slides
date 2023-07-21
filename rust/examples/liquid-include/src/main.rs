fn main() {
    let header_template = "
        <title>{{title}}</title>
    ";

    let template = "
       {% include 'header.txt' %}
       <h1>{{title}}</h1>
       <h2>{{name}}</h2>
    ";

    let header_template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(header_template).unwrap();

    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(template).unwrap();

    let globals = liquid::object!({
        "title": "Liquid",
        "name": "Page",
//        "header": 'header_template',
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}
