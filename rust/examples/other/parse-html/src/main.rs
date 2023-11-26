use scraper::{Html, Selector};

fn main() {

    let html = r#"
        <!DOCTYPE html>
        <meta charset="utf-8">
        <title>Hello, world!</title>
        <h1 class="foo">Hello, <i>world!</i></h1>
    "#;

    let document = Html::parse_document(html);
    let selector = Selector::parse("h1").unwrap();
    for element in document.select(&selector) {
        assert_eq!(element.value().name(), "h1");
        assert_eq!(element.attr("class").unwrap(), "foo");
        assert_eq!(element.inner_html(), "Hello, <i>world!</i>");       
        assert!(element.has_children());
        let x = element.has_children();
        //let x = element.inner_html();
        println!("{:?}", x);

        // The text content of an elemnet after removing all the markup
        let text = element.text().collect::<Vec<_>>().join("");
        assert_eq!(text, "Hello, world!");
    }

    let selector = Selector::parse("i").unwrap();
    for element in document.select(&selector) {
        assert_eq!(element.value().name(), "i");
        assert_eq!(element.inner_html(), "world!");
        assert!(element.has_children());
        let x = element.has_children();
        //let x = element.inner_html();
        println!("{:?}", x);
    }

}
