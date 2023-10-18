fn main() {
    let mut fruits1 = vec!["apple", "banana"];
    dbg!(&fruits1);
    dbg!(fruits1.capacity());

    let fruits2 = vec!["peach", "kiwi"];
    dbg!(&fruits2);

    fruits1.extend(&fruits2);
    dbg!(&fruits1);
    dbg!(&fruits2);
    fruits1[2] = "egg";
    dbg!(&fruits1);
    dbg!(&fruits2);
}
