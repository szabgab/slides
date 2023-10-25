fn main() {
    let mut joe = Person {name: "Joe".to_string(), partner: None};
    #[allow(unused_mut)]
    let mut jane = Person {name: "Jane".to_string(), partner: None};
    dbg!(&joe);
    dbg!(&jane);
    joe.partner = Some(&jane);
    //jane.partner = Some(&joe);
    dbg!(&joe);
    dbg!(&jane);

}

#[derive(Debug)]
#[allow(dead_code)]
struct Person<'a> {
    name: String,
    partner: Option<&'a Person<'a>>,
}

