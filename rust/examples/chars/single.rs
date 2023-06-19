fn main() {
    let chars = ['1', 'a', 'א', 'Ω', '😇', '😈'];
    for ch in chars {
        dbg!(ch);
        let num = ch as usize;
        dbg!(num);

        let num = ch as u32;
        dbg!(num);

        let back = char::from_u32(num).expect("Could not convert to char");
        dbg!(back);
        dbg!(ch == back);
    }
}
