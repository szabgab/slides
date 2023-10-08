use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Car {
    manufacturer: String,
    electric: bool,
    gears: i8,
    names: Vec<String>,
}

fn main() {
    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse("
            Car manufacturer: {{car.manufacturer}}
            {% if car.electric %}
                electric
            {% endif %}
            Gears: {{car.gears}}
            {% for name in car.names %}
               {{name}}
            {% endfor %}
        ").unwrap();

    let car = Car {
        manufacturer: "Ford".to_string(),
        electric: false,
        gears: 5,
        names: vec!["Mustang".to_string(), "Anglia".to_string()],
    };
    //println!("manufacturer: {}", car.manufacturer);
    //println!("electric: {}", car.electric);

    let globals = liquid::object!(
    {
        "car": car, //liquid::to_object(&car),
    });
    let output = template.render(&globals).unwrap();

    println!("{}", output);
}
