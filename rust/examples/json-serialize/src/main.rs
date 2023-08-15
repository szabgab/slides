use serde_json::json;


fn main() {
    let name = "Foo Bar";
    let number = 42;
    let numbers = vec![19, 23];
    let json_str = &json!({"name": name, "number": number, "vector of numbers": numbers});
    println!("{}", json_str);
}
