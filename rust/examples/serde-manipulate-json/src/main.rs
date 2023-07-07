use serde_json::json;

fn main() {
    let mut object = json!({ "A": 1, "B": 2, "C": 3 });
    dbg!(&object);

    *object.get_mut("A").unwrap() = json!(100);
    dbg!(&object);

    object["D"] = json!(200);
    dbg!(&object);

    object["E"] = json!("text");
    dbg!(&object);

    object["F"] = json!(vec!["apple", "banana"]);
    dbg!(&object);
}

