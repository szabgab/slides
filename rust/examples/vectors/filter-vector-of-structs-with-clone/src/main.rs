#[derive(Debug)]
#[derive(Clone)]
#[allow(dead_code)]
struct Something {
    number: i32,
    text: String,
    numbers: Vec<i32>,
}

fn main() {
    let va: Vec<Something> = vec![
        Something {number: 1, text: "small".to_string(), numbers: vec![1, 2, 3]},
        Something {number: 11, text: "medium".to_string(), numbers: vec![11, 12]},
        Something {number: 101, text: "large".to_string(), numbers: vec![101]},
    ];
    dbg!(&va);

    // This needs the Clone trait above and I am not sure if this does not mean that we duplicate
    // the data.
    let v_big = va.iter().filter(|thing| thing.number > 20).cloned().collect::<Vec<Something>>();
    //let v_big = &va.into_iter().filter(|thing| thing.number > 20).collect::<Vec<Something>>();
    dbg!(&v_big);
    dbg!(&va);
}
