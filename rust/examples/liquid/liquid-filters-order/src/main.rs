fn main() {
    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse("
           plain: {{text}}
           first: {{text | first}}
           last: {{text | last}}

           plain: {{words}}
           first: {{words | first}}
           last: {{words | last}}

           plain: {{numbers}}
           first: {{numbers | first}}
           last: {{numbers | last}}

           plain: {{tpl}}
           first: {{tpl | first}}
           last: {{tpl | last}}
       ").unwrap();

    let text = "This is some text";
    let words = ["These", "are", "words", "in", "an", "array"];
    let numbers = vec![7, 3, 19, 4];
    let tpl = ("foo", 42, "bar", 3.4);

    let globals = liquid::object!({
        "text": text,
        "words": words,
        "numbers": numbers,
        "tpl": tpl,
    });
    let output = template.render(&globals).unwrap();

    println!("{}", output);
}
