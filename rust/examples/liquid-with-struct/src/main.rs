#[derive(Debug)]
struct Car {
    manufacturer: String,
    electric: bool,
}

fn main() {
    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse("Car {{car.manufacturer}}").unwrap();

    let car = Car {
        manufacturer: "Ford".to_string(),
        electric: false,
    };
    // dbg!(car);

;
    let globals = liquid::object!({
        "car": liquid::to_object(&car)?,
    });
    let output = template.render(&globals).unwrap();

    println!("{}", output);
}
