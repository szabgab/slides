// cargo add html-to-string-macro
// https://crates.io/crates/html-to-string-macro
//

use html_to_string_macro::html;

fn main() {
    let html = html!(
<div>
<h2>"Title"</h2>
<hr />
</div>
);

    println!("{}", html);
    assert_eq!(html, "<div><h2>Title</h2><hr></div>");




    let name = "Foo".to_string();

    let html = html!(<div>"hello "{name}</div>);
    println!("{}", html);
    assert_eq!(html, "<div>hello Foo</div>");
}
