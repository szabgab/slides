use tempdir::TempDir;
use std::fs::File;
use std::io::Write;
//use std::thread;
//use std::time::Duration;


fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        println!("Usage: {} NUMBER_OF_FILES", args[0]);
        std::process::exit(1);
    }
    let number_of_files = args[1].parse::<i32>().unwrap();

    let temp_dir = TempDir::new("demo").unwrap();
    println!("{:?}", temp_dir);
    for ix in 1..=number_of_files {
        let file_path = temp_dir.path().join(format!("{}.txt", ix));
        println!("{:?}", file_path);
        let mut file = File::create(file_path).unwrap();
        writeln!(&mut file, "{}.txt", ix).unwrap();
    }
    let content = temp_dir.path().read_dir().unwrap().count() as i32;
    assert_eq!(number_of_files, content);
    
    

    println!("Number of files {}, {:?}", number_of_files, args);


}
