fn main() {
    let planets: Vec<&str> = vec!["Mercury", "Venus", "Earth"];
    println!("{}", planets.len());
    println!("{}", planets[ planets.len()-1 ]);
    // println!("{}", planets[ 5 ]);  // thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 5'
    println!("{}", planets.last().unwrap());

    let planets: Vec<&str> = vec![];
    //println!("{}", planets[ planets.len()-1 ]);  // thread 'main' panicked at 'attempt to subtract with overflow'
    println!("{:?}", planets.last()); // None
}
