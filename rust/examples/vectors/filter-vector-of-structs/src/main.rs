#[derive(Debug)]
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

    //let vb = &va.iter().collect::<Vec<&Something>>();
    let vb = &va.iter().collect::<Vec<_>>();

    let v_big = &vb.iter().filter(|thing| thing.number > 20).collect::<Vec<_>>();
    //let v_big = &vb.into_iter().filter(|thing| thing.number > 20).collect::<Vec<_>>();
    dbg!(&v_big);
    dbg!(&vb);
}
