use serde_json::json;


fn main() {
    let name = "Foo Bar";
    let json_str = &json!({"name": name});
    println!("{}", json_str);
}
