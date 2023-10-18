fn main() {
    let animals = ["snake", "mouse", "cat", "elephant"];
    println!("{:?}", animals);


    let max = animals.iter().max().unwrap();
    println!("{}", max);
    let min = animals.iter().min().unwrap();
    println!("{}", min);


    let longest = animals.iter().max_by(|x, y| x.len().cmp(&y.len())).unwrap();
    println!("{}", longest);


    let shortest = animals.iter().min_by(|x, y| x.len().cmp(&y.len())).unwrap();
    println!("{}", shortest);

}
